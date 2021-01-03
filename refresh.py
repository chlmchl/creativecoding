from __main__ import twitter_diary

@twitter_diary.route('/refresh', methods=['GET'])
def refresh():
    return 'refresh placeholder'