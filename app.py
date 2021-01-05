from flask import Flask
from task import refresh
import os

twitter_diary = Flask(__name__)

twitter_diary.debug = (
    True if os.environ.get("TWITTER_DIARY_APP_DEBUG") == "true" else False
)


@twitter_diary.route("/")
def hello_world():
    return "Hello World!"


@twitter_diary.route("/refresh", methods=["GET"])
def refresh_route():
    return refresh(), 200


if __name__ == "__main__":
    twitter_diary.run()
