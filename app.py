from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    random_element = random.randint(0,9)
    radomised_class = "Gnagster" if random_element > 7  else "Policeman" if random_element > 6 else "Citizen"
    user = {'class': radomised_class}
    return '''
<html>
    <head>
        <title>Mafia Game - Your class</title>
    </head>
    <body>
        <h1>You are a ''' + user['class'] + '''!</h1>
    </body>
</html>'''


#!flask/bin/python
if __name__ == '__main__':
    app.run()
