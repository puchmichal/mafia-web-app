from app import app, db
import random
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user, login_required


@app.route('/')
def go_to_login():
    return redirect('/login')

@app.route('/index')
@login_required
def index():
    random_element = random.randint(0,9)
    radomised_class = "Gangster" if random_element > 7 else "Policeman" if random_element > 6 else "Citizen"
    user = {'class': radomised_class}
    return render_template('class_preview.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None:
            user = User(username=form.username.data, is_host=False)
            db.session.add(user)
            db.session.commit()
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))