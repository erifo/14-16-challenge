import os
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename


# Sets up Flask and creates necessary upload folder.
api = Flask(__name__)
api.config['UPLOAD_FOLDER'] = './api_uploaded_images/'
if not os.path.exists(api.config['UPLOAD_FOLDER']):
    os.makedirs(api.config['UPLOAD_FOLDER'])


@api.route("/post/<filename>", methods=["POST"])
def post_file(filename):
    """Creates a file according to filename and data recieved."""
    filename = secure_filename(filename) # Preventing access to files in other directories on the server.
    with open(os.path.join(api.config['UPLOAD_FOLDER'], filename), "wb") as fp:
        fp.write(request.data)
    return "", 201 # Image successfully uploaded


@api.route("/get/<filename>")
def get_file(filename):
    """Returns file in the upload filder based on filename with extension."""
    return send_from_directory(api.config['UPLOAD_FOLDER'], filename)


@api.route("/list")
def list_files():
    """Lists all files uploaded to the server, for debugging."""
    files = []
    for filename in os.listdir(api.config['UPLOAD_FOLDER']):
        path = os.path.join(api.config['UPLOAD_FOLDER'], filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)

# Starts Flask.
api.run(debug=True, port=8000)