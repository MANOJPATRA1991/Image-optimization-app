from flask import Flask
from config import UPLOAD_IMAGES_FOLDER

app = Flask(__name__)

from .input_module.input import input

app.register_blueprint(input)

app.config.from_object('config')

app.config['UPLOAD_IMAGES_FOLDER'] = UPLOAD_IMAGES_FOLDER
