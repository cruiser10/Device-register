import markdown
import os
import shelve
from flask import Flask , g

app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database= shelve.open("devices.db")
    return db

@app.teardown_appcontext
def teardown_db(Exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()    


@app.route('/')
def index():

    with open(os.path.dirname(app.root_path) +'/Readme.md', 'r') as markdown_file:
        content = markdown_file.read()

        return markdown.markdown(content)

class DeviceList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in devices:
            device.append(shelf[key])

            return {'message': "success", "data": "devices"}        