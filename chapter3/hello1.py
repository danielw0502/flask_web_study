from datetime import datetime
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment


app = Flask(__name__)
bootstrap = Bootstrap(app)
"""
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name
"""

@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
"""
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')
"""
if __name__ == '__main__':
    app.run(debug=True)
