from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[validators.DataRequired()])
    submit = SubmitField('Submit')