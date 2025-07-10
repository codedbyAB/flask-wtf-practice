from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email



class UserForm(FlaskForm): #created one form class
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    ss = StringField("Social Security", validators=[DataRequired()])



