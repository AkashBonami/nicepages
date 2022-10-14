from turtle import title
import falcon
from app.controllers.notes import NotesController
from app import db
from app.models.notes_model import NoteModel
class GetNotes(object):
    def on_get(self, req, resp, id):
        resp.status = falcon.HTTP_200
        notes = []
        notes_obj = NoteModel.objects(title)
        for object in notes_obj:
            notes.append(object)
        resp.json = {
            'notes': notes
        }
class UploadNotes(object):
    def on_post(self, req, resp):
        title = resp.get_json('title', dtype=str)
        body = resp.get_json('body', dtype=str)
        notes_obj = NoteModel(
            title=title, body=body
        )
        notes_obj.save()
        resp.status = falcon.HTTP_201
        resp.json = {
            'message': 'Your Note Has Been Posted!',
            'status': 200,
            'successful': True
        }