import requests, os, sys, time
def menu() :
    print("\033[91m1.\033[0m \033[92mSend anonymous sms\033[0m")
    print("\033[91m2.\033[0m \033[92mCheck status of sms\033[0m")
def control() :
    ctrl = input("Your Choice : ")
    if ctrl == "1" :
        sms()
    elif ctrl == "2" :
        status()
    else :
        print("\033[91mInvalid number\033[0m")
def sms() :
   cc = input("\tEnter Your Country Code: ")
   phone_no = input("\tEnter Target Number: +"+ cc +" ")
   if phone_no == '9940152460':
           os.system('clear')
           sys.exit("\t\t\t\033[91m    I'LL NOT BETRAY MY MASTER")
   if phone_no == '7305574234':
           os.system('clear')
           sys.exit("\t\t\t\033[91m    I'LL NOT BETRAY MY MASTER")
   msg = input("message to send : ")

   resp = requests.post('https://textbelt.com/text',{
	'phone' : phone_no,
	'message' : msg ,
	'key' : 'textbelt'
   })
   if 'true' in resp.text :
	   print("\033[92m Message is sent :) \033[0m")
   if 'false' in resp.text :
	   print("\033[91m Maximum Limmit Reached Today :( ")



def status() :
  textID = input("Enter textID of sms : ") 
  os.system(f"curl https://textbelt.com/status/{textID}")

menu()
control()
