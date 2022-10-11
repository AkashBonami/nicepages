import json
import mysql.connector
from db_configuration.config import  *
from security.security import *
from status import nowOnline

class Signup:
    @classmethod
    def on_post(cls,req,resp):
        request=req.media
        uname=request.get("uname")
        email=request.get("email")
        password=encoder(request.get("password"))
        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            data = (uname,email,password)
            query = "INSERT INTO nicepages.users (uname, email, password) VALUES (%s,%s,%s);"
            cursor.execute(query, data)
            cnx.commit()
            cursor.close()
            cnx.close()
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
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            query1 = f"SELECT UID from users where uname = \'{uname}\';"
            cursor.execute(query1)
            uid = cursor.fetchall()
            uid = uid[0][0]
            query = f"SELECT password from users where UID={uid};"
            cursor.execute(query)
            encoded_pass = cursor.fetchall()
            data2 = encoded_pass[0][0]
            decoded_pass= decoder(data2)
            decoded_pass = decoded_pass["some"]

            cursor.close()
            if decoded_pass == password:
                credentials = {"Success":"Your have succesfully Logged in"}
                json_object = json.dumps(credentials, indent=4)
            else:
                credentials = {"Error":"Invalid Username or Password"}
                json_object = json.dumps(credentials, indent=4)
            nowOnline(uid)

        except Exception as es:
            error=es
            json_object =json.dumps(error,indent=4)

        finally:
            print(json_object)
            resp.text=json_object
            return resp 
class Update:
    @classmethod
    def on_post(cls,req,resp):
        request=req.media
        uname=request.get("uname")
        email=request.get("email")
        password=encoder(request.get("password"))
        try:
            cnx = mysql.connector.connect(**config)
            cursor = cnx.cursor()
            query1 = f"SELECT UID from users where uname = \'{uname}\';"
            cursor.execute(query1)
            uid = cursor.fetchall()
            uid = uid[0][0]
            if email != "":
                query2=f"SELECT email from users where UID = {uid};"
                cursor.execute(query2)
                db_email=cursor.fetchall()
                db_email=db_email[0][0]
                if db_email==email:
                    pass
                else:
                    query3=f"UPDATE users SET email=\'{email}\' where UID = {uid};"
                    cursor.execute(query3)
                    credentials={"Success":"Email has changed Successfully"}
                    json_object = json.dumps(credentials, indent=4)

            else:    
                # query4=f"SELECT password from users where UID = {uid};"
                # cursor.execute(query4)
                # db_password=cursor.fetchall()
                # db_password=db_password[0][0]
                # if db_password==password:
                #     pass
                # else:
                query5=f"UPDATE users SET password=\'{password}\' where UID = {uid};"
                cursor.execute(query5)
                credentials={"Success":"Password has changed Successfully"}
                json_object = json.dumps(credentials, indent=4)


            



        except Exception as es:
            error=es
            json_object =json.dumps(error,indent=4)
        finally:
            resp.text=json_object
            return resp
            

