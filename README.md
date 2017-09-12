# Image-optimization-app

## Installation and Test requirements

1. Create a folder and clone the repository to that folder.
2. If you haven't installed virtualenv, run `pip install virtualenv`.
3. Create a new virtual environment inside the project folder with the command `virtualenv env`.
4. Install the following packages with `env\Scripts\pip install <package_name>`.
   Replace `<package_name>` with package names.
    The packages used for this project include:
        
        1. flask
        2. Flask-Images
        3. Werkzeug
        4. pdfkit
        
5. Install wkhtmltopdf from [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html).
6. Check the path to **wkhtmltopdf.exe** is correct in **app/input_module/input.py**.
7. Install the following node packages if not already installed in the app/static folder:
    
    Bootstrap: `npm install --prefix ./static bootstrap`
    
    Font-awesome: `npm install --prefix ./static font-awesome`
    
