from flask import Flask, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import main

app = Flask(__name__)

# Define the folder where uploaded PDFs will be stored
UPLOAD_FOLDER = 'sample'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('process.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return main.predict(filename)

if __name__ == '__main__':
    app.run(debug=True)
