import os

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Folder to store the uploaded files
UPLOAD_IMAGES_FOLDER = os.path.join(BASE_DIR, 'app/uploads/')