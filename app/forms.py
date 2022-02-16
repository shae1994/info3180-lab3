from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], description="Please enter your full name")
    email = StringField('E-mail', validators=[DataRequired(), Email()], description="Please enter your email")
    subject = StringField('Subject', validators=[DataRequired()], description="Please enter the subject for your message.")
    message = TextAreaField('Message', validators=[DataRequired()], description="Please enter the message you would like to send.")
