
from .app import app, login_manager
from flask import render_template, redirect, url_for, flash, request
from .model import Movie, Users, Ratings , Admin
from flask_login import login_user, logout_user, current_user, login_required
#from .forms import RegisterForm, LoginForm, PurchaseForm, GameForm, GameEditForm, GameDeleteForm
from .forms import LoginFormAdmin, LoginForm, RegisterForm

@login_manager.user_loader
def load_user(user_id):
    return Users.get(user_id)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html", active_home="active")

@app.route("/admin_login", methods=['GET', 'POST'])
def admin_login_page():
    form = LoginFormAdmin()
    return render_template("admin_login.html", form=form, active_home="active")

@app.route("/user_login", methods=['GET', 'POST'])
def user_login_page():
    form = LoginForm()
    return render_template("user_login.html", form=form, active_home="active")

@app.route("/registration", methods=['GET', 'POST'])
def registration_page():
    form = RegisterForm()
    return render_template("registration.html", form=form, active_home="active")