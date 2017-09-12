from flask import Flask

# Create Flask app
app = Flask(__name__)

from .input_module.input import input

# Register input blueprint on app
app.register_blueprint(input)

# Enable configuration for the app
app.config.from_object('config.Config')
