# In The Name Of God
# ========================================
# [] File Name : hello-flask.py
#
# [] Creation Date : 11-08-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import flask


app = flask.Flask('Hello')


@app.route('/hello')
def hello():
    return '<h1>Hello world</h1>'


app.run()
