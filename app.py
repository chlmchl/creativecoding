from flask import Flask
from task import refresh, diary
from flask_cors import CORS
import os

twitter_diary = Flask(__name__)
CORS(twitter_diary, resources={"*": {"origins": "*"}})

twitter_diary.debug = (
    True if os.environ.get("TWITTER_DIARY_APP_DEBUG") == "true" else False
)


@twitter_diary.route("/")
def hello_world():
    return "twitter diary api"


@twitter_diary.route("/ping")
def ping():
    return "pong"


@twitter_diary.route("/refresh", methods=["GET"])
def refresh_route():
    return refresh(), 200


@twitter_diary.route("/diary", methods=["GET"])
def get_diary():
    return diary(), 200


if __name__ == "__main__":
    twitter_diary.run()
