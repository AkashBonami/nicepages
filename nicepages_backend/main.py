import falcon
from wsgiref.simple_server import make_server
from app import Signup,Login,Update


app = falcon.App()

signup =  Signup()
login = Login()
update=Update()

app.add_route('/signup', signup)
app.add_route('/login', login)
app.add_route('/update',update)


if __name__ == "__main__":
    with make_server('', 8001, app) as httpd:

        print("server running on 8001")
        httpd.serve_forever()