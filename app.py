from flask import Flask

import os

app = Flask(__name__)

app.debug = True if os.environ.get("APP_DEBUG") == 'true' else False

import index

import refresh

if __name__ == '__main__':
    app.run()
