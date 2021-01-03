from flask import Flask

import os

twitter_diary = Flask(__name__)

twitter_diary.debug = True if os.environ.get("APP_DEBUG") == 'true' else False

import index

import refresh

if __name__ == '__main__':
    twitter_diary.run()
