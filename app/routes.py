from app import app
import random
from flask import render_template, flash, redirect
from app.forms import LoginForm


@app.route('/')
def go_to_login():
    return redirect('/login')

@app.route('/index')
def index():
    random_element = random.randint(0,9)
    radomised_class = "Gangster" if random_element > 7  else "Policeman" if random_element > 6 else "Citizen"
    user = {'class': radomised_class}
    return render_template('class_preview.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('{}'.format(
            form.username.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)