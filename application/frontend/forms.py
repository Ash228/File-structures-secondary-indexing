from flask_wtf import FlaskForm
from wtforms import widgets, StringField, PasswordField, SubmitField, SelectField, SelectMultipleField, TextAreaField, IntegerField
from wtforms.validators import Length, DataRequired, ValidationError
from .model import Users, Movie, Ratings, Admin
from wtforms.fields.html5 import DateField

class RegisterForm(FlaskForm):

    def validate_uid(form, field):
        if not Users.check_userId(field.data):
            raise ValidationError("UserId is already taken.")

    userId = StringField(label="User Id", validators=[Length(min=1, max=10), DataRequired(), validate_uid])
    date = DateField(label="Date", format='%d-%m-%Y', validators=[DataRequired()])
    gender = StringField(label="Gender", validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[Length(min=1), DataRequired()])
    submit = SubmitField(label='Sign Up')

class LoginForm(FlaskForm):

    userId = StringField(label="userId", validators=[Length(min=1, max=10), DataRequired()])
    password = PasswordField(label='password', validators=[Length(min=1), DataRequired()])
    submit = SubmitField(label='LogIn')

    def validate(self, extra_validators=None):
        if super().validate(extra_validators):

            # your logic here e.g.
            if not (self.field1.data or self.field2.data):
                self.field1.errors.append('At least one field must have a value')
                return False
            else:
                return True

        return False

    if Users.check_password(userId, password):
        raise ValidationError('UserId or Password invalid')

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