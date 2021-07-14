import hashlib

from .app import app, login_manager
from flask import render_template, redirect, url_for, flash, request
from .model import Movie, Users, Ratings , Admin
from flask_login import login_user, logout_user, current_user, login_required
#from .forms import RegisterForm, LoginForm, PurchaseForm, GameForm, GameEditForm, GameDeleteForm
from .forms import LoginFormAdmin, LoginForm, RegisterForm

@login_manager.user_loader
def load_user(userId):
    if userId == '1234':
        return Admin.get(userId)
    return Users.get(userId)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html", active_home="active")

@app.route("/test")
def test_page():
    return render_template('test.html')

@app.route("/admin_login", methods=['GET', 'POST'])
def admin_login_page():
    form = LoginFormAdmin()
    if form.validate_on_submit():
        admin = Admin.get(form.adminId.data)
        if Admin.check_password(form.adminId.data, form.password.data):
            login_user(admin)
            flash(
                f"Logged in Successfully!! Welcome {current_user.username}", category="success")
            return redirect(url_for('test_page'))
        else:
            flash('Invalid credentials, Please try again', category="danger")
    return render_template("admin_login.html", form=form, active_admin_login="active")

@app.route("/user_login", methods=['GET', 'POST'])
def user_login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.get(form.userId.data)
        password = form.password.data
        password = hashlib.md5(password.encode('utf8')).hexdigest()
        if user.password == password:
            login_user(user)
            flash(
                f"Logged in Successfully!! Welcome {current_user.username}", category="success")
            return redirect(url_for('test_page'))
        else:
            flash('Invalid credentials, Please try again', category="danger")
    return render_template("user_login.html", form=form, active_login="active")

@app.route("/registration", methods=['GET', 'POST'])
def registration_page():
    form = RegisterForm()
    if form.validate_on_submit():
        Users.uinsert(request.form.get('userId'), request.form.get('name'),
                      form.date.data,request.form.get('gender'),request.form.get('password'))
        flash(
                f"Registered succesfully, Please Log In", category="success")
        return redirect(url_for('user_login_page'))
    else:
        flash('Invalid credentials, Please try again', category="danger")
        return render_template("registration.html", form=form, active_register="active")