from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import widgets, StringField, PasswordField, SubmitField, SelectField, SelectMultipleField, TextAreaField, \
    IntegerField, FileField
from wtforms.validators import Length, DataRequired, ValidationError
from .model import Users, Movie, Ratings, Admin
from wtforms.fields.html5 import DateField

class RegisterForm(FlaskForm):


    userId = StringField(label="User Id", validators=[Length(min=1, max=10,), DataRequired()])
    name = StringField(label="Name", validators=[Length(min=1, max=20), DataRequired()])
    date = DateField(label="Date")
    gender = StringField(label="Gender", validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=1), DataRequired()])
    submit = SubmitField(label='Sign Up')

class LoginForm(FlaskForm):

    userId = StringField(label="userId", validators=[Length(min=1, max=10)])
    password = PasswordField(label='password', validators=[Length(min=1)])
    submit = SubmitField(label='LogIn')

    def validate(self, extra_validators=None):
        if super().validate(extra_validators):

            # your logic here e.g.
            if not (self.userId.data or self.password.data):
                self.userId.errors.append('At least one field must have a value')
                self.password.errors.append('At least one field must have a value')
                return False
            else:
                return True

        return False

class LoginFormAdmin(FlaskForm):

    adminId = StringField(label="Admin Id", validators=[Length(min=1, max=10), DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=1), DataRequired()])
    submit = SubmitField(label='Log In')

    if Admin.check_password(adminId, password):
        raise ValidationError('AdminId or Password invalid')

class SearchForm(FlaskForm):

    movieId_or_title = StringField(label='Field 1')
    genre = StringField(label='Field 2')

    def validate(self, extra_validators=None):
        if super().validate(extra_validators):

            # your logic here e.g.
            if not (self.field1.data or self.field2.data):
                self.field1.errors.append('At least one field must have a value')
                return False
            else:
                return True

        return False

class LibraryForm(FlaskForm):

    title_movId = StringField(label='Title or MovieId' )
    genre = StringField(label='Genre')
    submit = SubmitField(label='Search')



'''class AdminForm(FlaskForm):
    uadd = SubmitField('Add User')
    umod = SubmitField('Modify User')
    udel = SubmitField('Delete User')
    madd = SubmitField('Add Movie')
    mmod = SubmitField('Modify Movie')
    mdel = SubmitField('Delete Movie')'''

class AddUserForm(FlaskForm):

    userId = StringField(label="User Id", validators=[Length(min=1, max=10), DataRequired()])
    name = StringField(label="Name", validators=[Length(min=1, max=20), DataRequired()])
    date = DateField(label="Date")
    gender = StringField(label="Gender", validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=1), DataRequired()])
    submit = SubmitField(label='Insert User')

class ModifyUserForm1(FlaskForm):
    name = StringField(label="Username", validators=[Length(min=1, max=20), DataRequired()])
    check = SubmitField(label='Check Uid')
    selectuid = SelectField(label='SelectUID',choices=[])
    submit = SubmitField(label='Modify User')

class ModifyUserForm2(FlaskForm):
    name = StringField(label="Name", validators=[Length(min=1, max=20), DataRequired()])
    date = DateField(label="Date")
    gender = StringField(label="Gender", validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=1), DataRequired()])
    submit = SubmitField(label='Modify User')

class DeleteUserForm(FlaskForm):
    pass

class AddMovieForm(FlaskForm):
    movieId = StringField(label="Movie Id", validators=[Length(min=1, max=10, ), DataRequired()])
    title = StringField(label="Title", validators=[Length(min=1, max=20), DataRequired()])
    description = StringField(label="Description", validators=[DataRequired()])
    genre = StringField(label="Genre", validators=[DataRequired()])
    imageupload = FileField(label='Image Upload', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField(label='Insert Movie')

class ModifyMovieForm(FlaskForm):
    pass

class DeleteMovieForm(FlaskForm):
    pass


