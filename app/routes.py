from app import app
import random

@app.route('/')
@app.route('/index')
def index():
    random_element = random.randint(0,9)
    radomised_class = "Gangster" if random_element > 7  else "Policeman" if random_element > 6 else "Citizen"
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