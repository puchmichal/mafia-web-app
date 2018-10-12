from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Let's start the game"

#!flask/bin/python
if __name__ == '__main__':
    app.run()
