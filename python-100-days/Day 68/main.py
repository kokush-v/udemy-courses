from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, insert, Boolean
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['UPLOAD_FOLDER'] = 'static/files'
# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def get(id):
        exist_user = db.get_or_404(User, id)
        return exist_user


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form["password"])
        user = User(email=request.form["email"], name=request.form["name"],
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template("register.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        exist_user = db.session.query(User).filter_by(
            email=request.form['email']).scalar()
        if check_password_hash(exist_user.password, request.form['password']):
            login_user(exist_user)

        return redirect('/secrets')
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/download')
@login_required
def download():
    try:
        return send_from_directory(
            app.config['UPLOAD_FOLDER'], 'cheat_sheet.pdf', as_attachment=True)
    except FileNotFoundError:
        return "File not found", 404


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
