import os
from flask import Flask, request
from flask import send_from_directory


app = Flask(__name__)

@app.route('/<int:property_id>/<int:room_id>',  methods = ['PUT'])
def get_files(property_id,room_id):
    UPLOAD_FOLDER = '/home/tech/file_uploads/'+str(property_id)+'/'+str(room_id)+'/'

    content = request.files['file']
    if os.path.isfile(UPLOAD_FOLDER+content.filename):
        return 'file already exists'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    content.save(str(UPLOAD_FOLDER)+content.filename)
    return 'file successfully uploaded'


@app.route('/<int:property_id>/<int:room_id>/<string:file_name>',  methods = ['GET'])
def send_files(property_id,room_id,file_name):
    SEND_FOLDER = '/home/tech/file_uploads/'+str(property_id)+'/'+str(room_id)+'/'

    if not os.path.exists(SEND_FOLDER):
        return 'path does not exit'
    return send_from_directory(SEND_FOLDER, file_name)


if __name__ == '__main__':
    app.run(port=8083)