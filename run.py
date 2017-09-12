import os
from app import app


if __name__ == '__main__':
    # Secret key
    app.secret_key = open('secret_key', 'r').read()
    # To enable just the interactive debugger without the code reloading
    app.debug = True
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
