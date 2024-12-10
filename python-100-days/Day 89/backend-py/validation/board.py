from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm


class CreateBoardForm(FlaskForm):
    name = StringField('name', validators=[InputRequired()])


class UpdateBoardForm(CreateBoardForm):
    id = IntegerField('id', validators=[InputRequired()])
