from curses import raw
import json
from pymongo import MongoClient
from bson import ObjectId

class Data:
    @classmethod
    def on_post(cls,req,resp):
        raw_json = req.bounded_stream.read()
        print(type(raw_json))
        try:
            cluster = MongoClient("mongodb://localhost:27017/nicepages")
            db=cluster["nicepages"]
            datadb=db["data"]
            with open("credentials.json",'r+',encoding="utf-8") as file:
                read=json.load(file)
                uid=read.get('uid')
                uid = ObjectId(uid)
            data={"uid":uid,"data":raw_json}
            datadb.insert_one(data)
            credentials = {"Success":"Successfully Saved",}
            json_object = json.dumps(credentials, indent=4)
            resp.text=json_object
            return resp

        except Exception as es:
            error= {"Error": es} 
            # print(error)        
            json_object =json.dumps(error,indent=4)
            resp.text=json_object
            return resp
class Load:
    @classmethod
    def on_get(cls,req,resp):
        try:
            cluster = MongoClient("mongodb://localhost:27017/nicepages")
            db=cluster["nicepages"]
            datadb=db["data"]
            with open("credentials.json",'r+',encoding="utf-8") as file:
                read=json.load(file)
                uid=read.get('uid')
                uid = ObjectId(uid)
            collections=datadb.find({"uid":uid})
            for result in collections:
                data=result["data"]
                # print(type(data))
                # data=bytes(data,'utf-8')
                # print(type(data))
                # json_object =json.dumps(data)
                resp.text=data
                return resp
            pass
        except Exception as es:
            error= {"Error": es} 
            print(error)        
            # json_object =json.dumps(error,indent=4)
            # resp.text=json_object
            # return res