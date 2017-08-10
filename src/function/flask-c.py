import flask


app = flask.Flask('Hello')


@app.route('/hello')
def hello():
    return '<h1>Hello world</h1>'


app.run()
