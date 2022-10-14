from mongoengine import *
import datetime
class NoteModel(Document):
   title = StringField(max_length=200, required=True)
   body = StringField(max_length=32, required=True, unique=True)