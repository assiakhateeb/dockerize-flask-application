# importing the required libraries
import os
from flask import Flask, render_template, request, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')


# Returns an index.html file.
@app.route('/')
def home():
    return render_template('index.html')


# Provides the time the image was built
@app.route('/creation')
def get_creation_date():
    creation_date = "<h1> Image Creation Time: </h1>" + \
        "<h1>" + os.environ['DATE'] + "</h1>"
    return creation_date


# A dynamic parameters / value provided when the image is built
@app.route('/dynamic')
def get_dynamic_value():
    dynamic_value = "<h1> Dynamic value provided when the image is built: </h1>" + \
        "<h1>" + os.environ['NUMBER'] + "</h1>"
    return dynamic_value


# Provides the dockerfile the image was created with (in the image)
@app.route('/dockerfile')
def dockerfile_content():
    with open('Dockerfile', 'r') as f:
        return render_template('dockerfile_content.html', text=f.read())


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")


# Gets a file and stores it on the image runtime
@app.route('/put', methods=['GET', "POST"])
def upload_file():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data  # First grab the file
        # Then save the file
        file.save(os.path.join(UPLOAD_FOLDER, secure_filename(file.filename)))

    return render_template('upload.html', form=form)

# Check if the uploads folder exist, need it to save the uploaded file.
def check_upload_dir():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# List the already uploaded files 
@app.route('/list', methods=['GET'])
def list_files():
    """Endpoint to list files."""
    uploaded_files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        path = os.path.join(UPLOAD_FOLDER, filename)
        if os.path.isfile(path):
            uploaded_files.append(filename)

    return render_template('list.html', files=uploaded_files)


#  Downloading the file as an attachment in the browser
@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    """Download a file."""
    full_path = os.path.join(app.root_path, UPLOAD_FOLDER)
    return send_from_directory(full_path, filename, as_attachment=True)

# Returns a file from the lcoal store (that was uploaded previously).
@app.route('/get')
def query_example():
    filename = request.args.get('filename')
    uploaded_files = []
    for f in os.listdir(UPLOAD_FOLDER):
        if f == filename:
            path = os.path.join(UPLOAD_FOLDER, f)
            if os.path.isfile(path):
                uploaded_files.append(f)

    return render_template('get_file.html', files=uploaded_files)


if __name__ == '__main__':
    check_upload_dir()
    app.run(debug=True, host='0.0.0.0', port=8080)  # running the flask app