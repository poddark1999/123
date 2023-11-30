from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from models.user import is_strong

def strong_password_check(form, field):
    """
    Checks if the password is strong enough

    Params
    ------
        :param form: form to check
        :type form: FlaskForm
        :param field: field to check
        :type field: PasswordField

    Raises
    ------
        :raises ValidationError: if the password is not strong enough

    """
    if not is_strong(field.data):
        raise ValidationError('Password is not strong enough')

class LoginForm(FlaskForm):
    """
    Form for logging in
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    """
    Form for registering
    """
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First_name', validators=[DataRequired()])
    last_name = StringField('Last_name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), strong_password_check])
    password2 = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField('Register')
