from flask_wtf import FlaskForm
from wtforms import SubmitField

class MissionForm(FlaskForm):
    submit = SubmitField("Receive your mission")
