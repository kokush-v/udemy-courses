from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import DateTime, Integer, String, Text
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime
from form import CreateBlogPostForm


'''
Make sure the required packages are installed:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)
ckeditor = CKEditor(app)

# CONFIGURE TABLE


class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(
        String(250), nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(
        String(250), default=datetime.now().strftime(format="%d-%m-%y"))
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    result = db.session.execute(db.select(BlogPost).order_by(BlogPost.id))
    all_posts = result.scalars().all()
    return render_template('index.html', all_posts=all_posts)

# TODO: Add a route so that you can click on individual posts.


@app.route('/')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = "Grab the post from your database"
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post

@app.route('/add', methods=["GET", "POST"])
def add_post():
    form = CreateBlogPostForm()
    if form.validate_on_submit():
        new_blog = BlogPost(title=form.title.data, subtitle=form.subtitle.data,
                            body=form.body.data, author=form.author.data, img_url=form.bg_url.data)

        db.session.add(new_blog)
        db.session.commit()
        return redirect('/')

    return render_template('make-post.html', form=form)

# TODO: edit_post() to change an existing blog post


@app.route('/edit/<blog_id>', methods=["GET", "POST"])
def edit_post(blog_id):
    exist_blog = db.session.execute(
        db.select(BlogPost).where(BlogPost.id == blog_id)).scalar()

    form = CreateBlogPostForm(title=exist_blog.title,
                              subtitle=exist_blog.subtitle,
                              body=exist_blog.body,
                              author=exist_blog.author,
                              bg_url=exist_blog.img_url)

    if form.validate_on_submit():
        new_blog = BlogPost(title=form.title.data, subtitle=form.subtitle.data,
                            body=form.body.data, author=form.author.data, img_url=form.bg_url.data)

        exist_blog.title = new_blog.title
        exist_blog.subtitle = new_blog.subtitle
        exist_blog.body = new_blog.body
        exist_blog.author = new_blog.author
        exist_blog.img_url = new_blog.img_url

        db.session.commit()
        return redirect('/')

    return render_template('make-post.html', form=form, is_edit=True)

# TODO: delete_post() to remove a blog post from the database

# Below is the code from previous lessons. No changes needed.


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
