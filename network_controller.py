import requests as req
import json
def get_ticket():
    url="http://10.215.26.61/api/v1/ticket"
    headers={
        "Content-Type":"application/json"
    }
    body={
        "username":"admin",
        "password":"vnpro@123"
    }

    data=req.post(url=url,json=body,headers=headers,verify=False).json()
    return data["response"]["serviceTicket"]   
def get_device():
    url="https://10.215.26.61/api/v1/network-device"
    headers={
        "Content-Type":"application/json",
        "X-Auth-Token":get_ticket()}
    data=req.get(url=url,headers=headers,verify=False).json()
    return data["response"]
if __name__=="__main__":
    print(json.dumps(get_device(), indent=2))
