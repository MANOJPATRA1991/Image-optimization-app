import os
from .. import app
from flask import Blueprint, render_template, request, make_response
from werkzeug.utils import secure_filename
import pdfkit

# Configure pdfkit for path to wkhtmltopdf installation folder
config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

# Create new Blueprint instance
input = Blueprint('input_mod', __name__)


@input.route('/', methods=['GET'])
def show_main():
    """
    Renders index.html template file
    Returns:
         Rendered template page
    """
    if request.method == 'GET':
        return render_template('index.html')


@input.route('/downloads/', methods=['POST'])
def convert_to_pdf():
    """
    Optimize images and creates a pdf file containing the resized images
    Returns:
         Returns response object
    """
    if request.method == 'POST':
        images = []
        for i in range(4):
            image = request.files.get("{}{}".format("image", i))
            if allowed_file(image.filename):
                # Store the image in uploads folder
                # if it has allowed file extension
                new_path = os.path.join(app.config['UPLOAD_IMAGES_FOLDER'],
                                        secure_filename(image.filename))
                image.save(new_path)
                # Add the image to the images list
                images.append(new_path)
        # Render pdf.html with images stored in images list object
        rendered = render_template("pdf.html", imgList=images)
        css = [
            'app/static/node_modules/bootstrap/dist/css/bootstrap.min.css',
            'app/static/styles.css'
        ]
        # Create pdf
        pdf = pdfkit.from_string(
            rendered, False, css=css, configuration=config)
        response = make_response(pdf)
        response.headers['Content-type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
        # Remove the image files from the uploads directory
        # once the pdf file is generated
        file_list = [f for f in os.listdir(app.config['UPLOAD_IMAGES_FOLDER'])]
        for f in file_list:
            if(allowed_file(f)):
                os.remove(os.path.join(app.config['UPLOAD_IMAGES_FOLDER'], f))
        return response


def allowed_file(filename):
    """
    Checks if file is valid image file
    Args:
        filename: Image file name
    Returns:
        A Boolean value indicating a valid/invalid file
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower(
           ) in app.config['ALLOWED_EXTENSIONS']
