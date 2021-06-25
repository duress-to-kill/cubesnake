from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "The app is running!! :)"

@app.route('/cube/all')
def list_cubes():
    return "The app is running!! :)\nlist_cubes()"

@app.route('/cube/new')
def new_cube():
    return "The app is running!! :)\nnew_cube()"

@app.route('/cube/<uuid:cube_id>')
def get_cube(cube_uuid):
    return "The app is running!! :)\nget_cube()"

@app.route('/cube/<uuid:cube_id>/edit')
def edit_cube(cube_uuid):
    return "The app is running!! :)\nedit_cube()"

@app.route('/cube/<uuid:cube_id>/delete')
def delete_cube(cube_uuid):
    return "The app is running!! :)\ndelete_cube()"
