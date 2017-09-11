import os
from .. import app
from flask import Blueprint, render_template, request, make_response
from werkzeug.utils import secure_filename
import pdfkit

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

input = Blueprint('input_mod', __name__)


@input.route('/', methods=['GET'])
def show_main():
    if request.method == 'GET':
        return render_template('index.html')


@input.route('/downloads/', methods=['POST'])
def convert_to_pdf():
    if request.method == 'POST':
        images = []
        size = (300, 300)
        for i in range(4):
            image = request.files.get("{}{}".format("image", i))
            if allowed_file(image.filename):
                new_path = os.path.join(app.config['UPLOAD_IMAGES_FOLDER'],
                                        secure_filename(image.filename))
                image.save(new_path)
                images.append(new_path)

        rendered = render_template("pdf.html", imgList=images)
        css = [
            'app/static/node_modules/bootstrap/dist/css/bootstrap.min.css',
            'app/static/styles.css'
        ]
        pdf = pdfkit.from_string(rendered, False, css=css, configuration=config)
        response = make_response(pdf)
        response.headers['Content-type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
        file_list = [f for f in os.listdir(app.config['UPLOAD_IMAGES_FOLDER'])]
        for f in file_list:
            os.remove(os.path.join(app.config['UPLOAD_IMAGES_FOLDER'], f))
        return response


# check if uploaded file is allowed
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
