import json
from security.security import *
from status import nowOnline
from pymongo import MongoClient
from bson import ObjectId
class Signup:
    @classmethod
    def on_post(cls,req,resp):
        request=req.media
        uname=request.get("uname")
        email=request.get("email")
        password=encoder(request.get("password"))
        try:
            cluster = MongoClient("mongodb://localhost:27017/nicepages")
            db=cluster["nicepages"]
            collection=db["users"]
            print(collection.find())
            if collection.find({"uname":uname}):
                credentials={"Error":"Username already Exists"}
                json_object = json.dumps(credentials, indent=4)
            else:    
                data = {"uname": f"{uname}", "email":f"{email}","password":f"{password}" }
                collection.insert_one(data)
                credentials = {"Success":"Your have succesfully signed up"}
                json_object = json.dumps(credentials, indent=4)
        except Exception as es:

            error=es
            
            json_object =json.dumps(error,indent=4)
        finally:
            resp.text=json_object
            return resp
class Login:
    @classmethod
    def on_post(cls,req,resp):
        request=req.media
        uname=request.get("uname")
        password=request.get("password")
        try:
            cluster = MongoClient("mongodb://localhost:27017/nicepages")
            db=cluster["nicepages"]
            collection=db["users"]
            collections=collection.find({"uname":f"{uname}"})
            for result in collections:
                uid = result["_id"]
                encoded_pass=result["password"]
            decoded_pass=decoder(encoded_pass)
            decoded_pass = decoded_pass["some"]
            if decoded_pass == password :
                nowOnline(uid)
                credentials = {"Success":"Your have succesfully logged in"}
                json_object = json.dumps(credentials, indent=4)
            else :
                credentials = {"Error":"Invalid Password"}
                json_object = json.dumps(credentials, indent=4)


        except Exception as es:
            error=es
            json_object =json.dumps(error,indent=4)
        finally:
            resp.text=json_object
            return resp 


class Update:
    @classmethod
    def on_post(cls,req,resp):
        request=req.media
        email=request.get("email")
        password=request.get("password")
        try:
            with open("credentials.json",'r+',encoding="utf-8") as file:
                read=json.load(file)
                uid=read.get('uid')
                uid = ObjectId(uid)
            cluster = MongoClient("mongodb://localhost:27017/nicepages")
            db=cluster["nicepages"]
            collection=db["users"]
            

            if email or password:
                if email:
                    collection.update_one({"_id":uid},{"$set":{"email":email}})
                  
                if password:
                    password=encoder(password)
                    collection.update_one({"_id":uid},{"$set":{"password":password}})
                  


            credentials = {"Success":"Update Successfull"}
            json_object = json.dumps(credentials, indent=4)
        except Exception as es:

            error=es
            
            json_object =json.dumps(error,indent=4)
        finally:
            resp.text=json_object
            return resp

