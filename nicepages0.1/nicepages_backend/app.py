import json
import mysql.connector
from db_configuration.config import  *
from security.security import *
from status import nowOnline
from pymongo import MongoClient
class Signup:
    @classmethod
    def on_post(cls,req,resp):
        request=req.media
        uname=request.get("uname")
        email=request.get("email")
        password=encoder(request.get("password"))
        try:
            # cnx = mysql.connector.connect(**config)
            # cursor = cnx.cursor()
            # data = (uname,email,password)
            # query = "INSERT INTO nicepages.users (uname, email, password) VALUES (%s,%s,%s);"
            # cursor.execute(query, data)
            # cnx.commit()
            # cursor.close()
            # cnx.close()
            cluster = MongoClient("mongodb://localhost:27017/nicepages")
            db=cluster["nicepages"]
            collection=db["nicepages"]
            data = {"uname": f"{uname}", "email":f"{email}","password":f"{password}" }
            collection.insert_one(data)
            # print(collection)
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
            collection=db["nicepages"]
            collections=collection.find({"uname":f"{uname}"})
            for result in collections:
                uid = result["_id"]
                print(uid)
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

        
            # nowOnline(uid)

            # cnx = mysql.connector.connect(**config)
            # cursor = cnx.cursor()
            # query1 = f"SELECT UID from users where uname = \'{uname}\';"
            # cursor.execute(query1)
            # uid = cursor.fetchall()
            # uid = uid[0][0]
            # query = f"SELECT password from users where UID={uid};"
            # cursor.execute(query)
            # encoded_pass = cursor.fetchall()
            # data2 = encoded_pass[0][0]
            # decoded_pass= decoder(data2)
            # decoded_pass = decoded_pass["some"]

            # cursor.close()
            # if decoded_pass == password:
            #     credentials = {"Success":"Your have succesfully Logged in"}
            #     json_object = json.dumps(credentials, indent=4)
            # else:
            #     credentials = {"Error":"Invalid Username or Password"}
            #     json_object = json.dumps(credentials, indent=4)
            # nowOnline(uid)

        except Exception as es:
            error=es
            print(error)
            json_object =json.dumps(error,indent=4)
            print(json_object)
        finally:
            print(json_object)
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
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            # query = f"SELECT password from users where UID={uid};"
            # cursor.execute(query)
            # local_password=cursor.fetchall()
            # query1 = f"SELECT email from users where UID={uid};"
            # cursor.execute(query1)
            # local_email=cursor.fetchall()
            if email or password:
                if email:
                    query=f"UPDATE users SET email=\'{email}\' where UID = {uid};"
                    cursor.execute(query)
                    cnx.commit()
                    print("email updated")
                    # credentials = {"Success":"Email Updated"}
                    # json_object = json.dumps(credentials, indent=4)
                    # resp.text(json_object)
                    # return resp

                if password:
                    password=encoder(password)
                    query=f"UPDATE users SET password=\'{password}\' where UID = {uid};"
                    cursor.execute(query)
                    cnx.commit()
                    print("password updated")
                    # credentials = {"Success":"Password Updated"}
                    # json_object = json.dumps(credentials, indent=4)
                    # resp.text(json_object)
                    # return resp
            
                # print(read.get('uid'))
        except Exception as ex:
            print(ex)
            credentials = {"Error":{ex}}
            json_object = json.dumps(credentials, indent=4)
            resp.text(json_object)
            return resp

        finally:
            cursor.close()
            cnx.close()


