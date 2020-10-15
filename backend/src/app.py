import os
import sys
from os import listdir
from os.path import isfile

from flask import Flask, request, redirect, url_for, flash, send_file, send_from_directory, abort, url_for, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

from afaaRunner import afaaRunner

app = Flask(__name__, static_folder='output_files')
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

# upload folder for input files
UPLOAD_FOLDER = 'input_files'

# download folder for output files
DOWNLOAD_FOLDER = 'output_files'

# allowed extensions for the input files
ALLOWED_EXTENSIONS = {'csv'}
DO_NOT_DELETE_EXTENSIONS = {'md'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
CORS(app)


def validate_extension(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        # logic to clean the folder
        #clean_directory(os.path.join(app.config['UPLOAD_FOLDER']))
        #clean_directory(os.path.join(app.config['DOWNLOAD_FOLDER']))
        # check if the request comes with the input file
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        # if file exists and is with right extension
        if file and validate_extension(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # call the driver function
            print(os.path.join(app.config['UPLOAD_FOLDER'], file.filename)) 
            print('input file')
            print(app.config['DOWNLOAD_FOLDER'])
            print('download path')
            filelist = []
            for file in listdir(app.config["UPLOAD_FOLDER"]):
                absolute_name = os.path.join(app.config["UPLOAD_FOLDER"],file)
                if(absolute_name not in filelist):
                    filelist.append(absolute_name)
            print(filelist)
            ar = afaaRunner(filelist, app.config['DOWNLOAD_FOLDER'])
            
            response = jsonify({'message': 'files saved and runner function called'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

    return "Returning after Post"


# this method contains the code to clean up the files from the directory if there are any
def clean_directory(directory):
    print(directory)
    # get all the file names in files
    for file in listdir(directory):
        absolute_name = os.path.join(directory, file)
        if isfile(absolute_name) & (file.rsplit('.', 1)[1].lower() not in DO_NOT_DELETE_EXTENSIONS):
            print("Clearing stale files"+file.rsplit('.', 1)[1].lower())
            os.remove(absolute_name)


@app.route('/analysis', methods=['GET'])
def get_match_summary():
    image_name = 'fieldgoal_block.png'
    responses = []
    counter = 0

    for file in listdir(app.config['DOWNLOAD_FOLDER']):
        if isfile(os.path.join(app.config['DOWNLOAD_FOLDER'], file)) & (file.rsplit('.', 1)[1].lower() not in DO_NOT_DELETE_EXTENSIONS):
            link = "http://" + request.host + url_for('static', filename=file)
            counter += 1
            responses.append({"id": counter, "link": link})

    return jsonify(responses)
    # try:
    #     return send_from_directory(app.config['DOWNLOAD_FOLDER'], mimetype='image/png', filename=image_name, as_attachment=False)
    # except FileNotFoundError:
    #     abort(404)


if __name__ == '__main__':
    app.run(debug = True)