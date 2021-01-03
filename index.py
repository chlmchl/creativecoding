from __main__ import twitter_diary

@twitter_diary.route('/')
def hello_world():
    return 'Hello World!'