import os

from flask import Flask, request, redirect, url_for, flash
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
# upload folder for input files
UPLOAD_FOLDER = 'input_files'

# allowed extensions for the input files
ALLOWED_EXTENSIONS = {'csv'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)

#
def validate_extension(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET','POST'])
def upload_files():
    if request.method == 'POST':
        
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
            #return redirect(url_for('uploaded_file', filename=filename))
            return 'Saved the files to input folder'
    return "Returning after Post"

if __name__ == '__main__':
    app.run(debug = True)