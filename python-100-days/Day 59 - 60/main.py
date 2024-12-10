from flask import Flask, render_template, request
import requests

app = Flask(__name__)

response = requests.get('https://api.npoint.io/0b553b626494d008bb4b')
response.raise_for_status
posts = response.json()


@app.route('/')
def home():
    return render_template('index.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\n"\
        f"Email: {email}\nPhone: {phone}\nMessage:{message}"

    print(email_message)


@app.route('/post/<id>')
def post(id):
    return render_template('post.html', post=posts[int(id) - 1])


if __name__ == '__main__':
    app.run(debug=True)
