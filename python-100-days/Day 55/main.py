from flask import Flask
import random

random_number = random.randint(0, 9)
print(random_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>"

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>"
    elif guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"
    else:
        return "<h1 style='color: green'>You found me!</h1>"

if __name__ == "__main__":
    app.run(debug=True)