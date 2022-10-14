import os
import falcon_jsonify
dbcfg = {
    'host': 'localhost', # or external server address
    'port': 27017,
    'username': os.environ.get('MONGO_USER'),
    'password': os.environ.get('MONGO_PASS'),
}
middleware = [
    falcon_jsonify.Middleware(help_messages=True),
]