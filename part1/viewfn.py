from flask import request
from flask import Flask
from flask import redirect
from flask import abort
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {:s}</p>'.format(user_agent)
    
@app.route('/index')
def index2():
    return '<h1>Hello World!</h1>'
    
@app.route('/br')
def index3():
    return '<h1>Bad Request</h1>', 400
    
@app.route('/coki')
def index4():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/rd')
def index5():
    return redirect('/user/George')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {:s}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
