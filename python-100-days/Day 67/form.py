
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField
from wtforms.validators import DataRequired
from flask_ckeditor import CKEditorField


class CreateBlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    bg_url = URLField('Background URL', validators=[DataRequired()])
    body = CKEditorField('Blog content', validators=[DataRequired()])
    submit = SubmitField()
