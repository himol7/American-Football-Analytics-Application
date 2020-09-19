import os
from os import listdir
from os.path import isfile

from flask import Flask, request, redirect, url_for, flash, send_file, send_from_directory, abort
from flask_cors import CORS
from werkzeug.utils import secure_filename

from src.afaaRunner import afaaRunner

app = Flask(__name__)

# upload folder for input files
UPLOAD_FOLDER = 'input_files'

# download folder for output files
DOWNLOAD_FOLDER = 'output_files'

# allowed extensions for the input files
ALLOWED_EXTENSIONS = {'csv'}
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
        clean_directory(os.path.join(app.config['UPLOAD_FOLDER']))

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
            # return redirect(url_for('uploaded_file', filename=filename))
            return 'Saved the files to input folder'

        # call the driver function
        ar = afaaRunner(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

    return "Returning after Post"


# this method contains the code to clean up the files from the directory if there are any
def clean_directory(directory):
    # get all the file names in files
    for file in listdir(directory):
        absolute_name = os.path.join(directory, file)
        if isfile(absolute_name):
            os.remove(absolute_name)


@app.route('/analysis', methods=['GET'])
def get_match_summary():
    image_name = 'abc.png'
    files = []
    for file in listdir(app.config['DOWNLOAD_FOLDER']):
        if isfile(os.path.join(app.config['DOWNLOAD_FOLDER'], file)):
            files.extend(file)

    try:
        return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename=image_name, as_attachment=False)
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run(debug = True)