from wsgiref.simple_server import make_server
import falcon
import mongoengine as mongo
from app.settings import middleware
app = falcon.API(middleware=middleware)
db = mongo.connect(
    'development', # This will be the name of your database
    host=db['host'],
    port=db['port'],
    username=db['username'],
    password=db['password']
)
from app.resources.notes import *
app.add_route('/notes/', UploadNotes)
app.add_route('/notes/{}', GetNotes)
if __name__ == "__main__":
    with make_server('', 8001, app) as httpd:
        print("server running on 8001")
        httpd.serve_forever()