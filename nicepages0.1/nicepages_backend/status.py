import json
def nowOnline(uid):  
    uid=str(uid)
    data={"uid":uid}
    data=json.dumps(data,indent=4)
    with open('credentials.json','w+') as online:
        online.write(data)