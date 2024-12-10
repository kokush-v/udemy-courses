from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
response.raise_for_status
posts = [Post(post['id'], post['title'], post['subtitle'], post['body'])
         for post in response.json()]


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route('/post/<id>')
def post(id):
    return render_template('post.html', post=posts[int(id) - 1])


if __name__ == "__main__":
    app.run(debug=True)
