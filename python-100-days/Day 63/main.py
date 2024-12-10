from flask import Flask, render_template, request, redirect
from models import Book, db

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.execute(
        db.select(Book).order_by(Book.id)).scalars().all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book = Book(
            name=request.form["name"], author=request.form["author"], rating=request.form["rating"])
        db.session.add(book)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
