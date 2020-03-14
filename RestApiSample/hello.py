from flask import Flask
from flask import render_template
from app import templates

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    user = {'username': 'Eric'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

@app.route('/index2')
def index2():
    user = {'username':'haha'}
    return render_template('templates/index.html',title='Home Index2', user=user)




if __name__ == "__main__":
    app.run(debug=True, port=8080)
