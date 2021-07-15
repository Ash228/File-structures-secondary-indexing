import hashlib

from .app import app, login_manager
from flask import render_template, redirect, url_for, flash, request
from .model import Movie, Users, Ratings , Admin
from flask_login import login_user, logout_user, current_user, login_required
#from .forms import RegisterForm, LoginForm, PurchaseForm, GameForm, GameEditForm, GameDeleteForm
from .forms import LoginFormAdmin, LoginForm, RegisterForm, LibraryForm, DetailsForm

@login_manager.user_loader
def load_user(userId):
    if userId == '1234':
        return Admin.get(userId)
    return Users.get(userId)

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html", active_home="active")

@app.route("/registration", methods=['GET', 'POST'])
def registration_page():
    form = RegisterForm()
    if form.validate_on_submit():
        if not Users.check_userId(request.form.get('userId')):
            Users.uinsert(request.form.get('userId'), request.form.get('name'),
                      form.date.data,request.form.get('gender'),request.form.get('password'))
            flash(
                    f"Registered succesfully, Please Log In", category="success")
            return redirect(url_for('user_login_page'))
        else:
            flash('User Id already exists', category="danger")
    else:
        flash('Invalid credentials, Please try again', category="danger")

    return render_template("registration.html", form=form, active_register="active")

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
        if user:
            password = form.password.data
            password = hashlib.md5(password.encode('utf8')).hexdigest()
            if user.password == password:
                login_user(user)
                flash(
                    f"Logged in Successfully!! Welcome {current_user.username}", category="success")
                return redirect(url_for('library_page'))
            else:
                flash('Invalid credentials, Please try again', category="danger")
        else:
            flash('Invalid credentials, Please try again', category="danger")
    return render_template("user_login.html", form=form, active_login="active")

@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    flash('Logged out successfully', category='info')
    return redirect(url_for('home_page'))

@app.route('/library', methods=['GET', 'POST'])
@login_required
def library_page():
    movieId = False
    form = LibraryForm()
    detailform = DetailsForm()
    if form.submit.data:
        title_movId = request.form.get('title')
        genre = request.form.get('genre')
        if title_movId:
            if title_movId.isnumeric():
                print('search1')
                # return redirect(url_for('search_display_page',movieId=title_movId))
            else:
                print('search2')
                # return redirect(url_for('search_display_page', title=title_movId))
        elif genre:
            print('search3')
            # return redirect(url_for('search_display_page', genre=genre))
        else:
            print('search4')
            pass
    if detailform.submit1.data:
        movieId = request.form.get('movId')
        if movieId:
            if Movie.check_movie(movieId=movieId):
                return redirect(url_for('test_page'))
            else:
                flash(f"Error rendering movie", category="danger")

    top_rec = Movie.recommendationtop()
    allmov = Movie.get_all_movies()

    return render_template("library.html", top_rec=top_rec, allmov=allmov, form=form, detailform=detailform, active_lib="active")

'''@app.route('/librarysearch', methods=['GET', 'POST'])
@login_required
def library_search_page():

    top_rec = Movie.recommendationtop()
    allmov = Movie.get_all_movies()
    return render_template("library.html", top_rec=top_rec, allmov=allmov, form=form, active_lib="active")
'''




#@app.route('/search')
#@login_required
#def search_display_page(title=False, genre=False):


