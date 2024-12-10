import random
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import DataRequired
from wtforms import StringField
from flask_wtf import FlaskForm
from flask import Flask, redirect, render_template, request, url_for
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, select

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Url(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    url: Mapped[str] = mapped_column(String, unique=True)
    code: Mapped[str] = mapped_column(String)


with app.app_context():
    db.create_all()


class Form(FlaskForm):
    url = StringField('url', validators=[DataRequired()])


@app.route('/', defaults={'code': None}, methods=['GET', 'POST'])
@app.route('/<code>', methods=['GET', 'POST'])
def home(code):
    if code:
        exist_url = Url.query.filter_by(code=code).scalar()
        return redirect(exist_url.url)

    form = Form()
    if form.validate_on_submit():
        exist_url = Url.query.filter_by(url=form.url.data).scalar()
        print(exist_url)
        if exist_url == None:
            code = "%032x" % random.getrandbits(128)
            print(code)
            new_url = Url(url=form.url.data, code=code)
            db.session.add(new_url)
            db.session.commit()
            exist_url = new_url

        return redirect(url_for('url_display', code=exist_url.code))

    return render_template('index.html', form=form)


@app.route('/url')
def url_display():
    code = request.args['code']
    return render_template('url.html', url=f'http://127.0.0.1:5000/{code}')


if __name__ == '__main__':
    app.run(debug=True)
