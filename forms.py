from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo




class UserRegistration(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField ('Password', validators=[DataRequired(), Length(min=5)])
    confirm_password = PasswordField("Confirm_Password", validators=[DataRequired(),
    Length(min=5), EqualTo('password', message='Password must match')])
    submit = SubmitField('Register')


