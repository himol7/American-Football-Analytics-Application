from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
from werkzeug.datastructures import ImmutableMultiDict
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/uploads"
CORS(app)

@app.route('/upload', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        
        uploaded_file = request.files['file']  
        uploaded_file.save(uploaded_file.filename)
        return 'Received the form'
    
    return "Returning after Post"

if __name__ == '__main__':
    app.run(debug = True)