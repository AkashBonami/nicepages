import mysql.connector
import json
from db_configuration.config import *
def nowOnline(uid):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query1 = f"SELECT uname from users where UID = {uid};"
    cursor.execute(query1)
    uname = cursor.fetchall()
    uname = uname[0][0]
    # data =  {f"{uid}":f"{uname}"}
    data={f"{uid}":{
        "uname":f"{uname}"
        }
    }
    data=json.dumps(data,indent=4)
    print(data)
    with open('credentials.json','w') as online:
        online.write(data)