from __main__ import app

@app.route('/refresh', methods=['GET'])
def refresh():
    return 'refresh placeholder'