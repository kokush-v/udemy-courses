from flask import Flask, request
from flask_cors import CORS
from database.db_models import db
from controllers.task import *
from controllers.board import *

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['WTF_CSRF_ENABLED'] = False

CORS(app, origins=["http://localhost:5173"], supports_credentials=True)


db.init_app(app)

with app.app_context():
    db.create_all()

# task routes


@app.route('/task/create', methods=['POST'])
def create_task():
    if request.method == 'POST':
        data = request.json
        return create_task_controller(data)


@app.route('/task/update', methods=['PUT'])
def update_task():
    if request.method == 'PUT':
        data = request.json
        return update_task_controller(data)


@app.route('/task/delete/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    if request.method == "DELETE":
        return delete_task_controller(task_id)


@app.route('/task/<int:board_id>', methods=['GET'])
def get_task(board_id):
    if request.method == "GET":
        return get_tasks_by_board_controller(board_id)


# board routes

@app.route('/board/<string:board_name>', methods=["GET"])
def get_board(board_name):
    if request.method == 'GET':
        return get_board_controller(board_name)


@app.route('/board/create', methods=['POST'])
def create_board():
    if request.method == 'POST':
        data = request.json
        return create_board_controller(data)


@app.route('/board/update', methods=["PUT"])
def update_board():
    if request.method == 'PUT':
        data = request.json
        return update_board_controller(data)


if __name__ == '__main__':
    app.run(debug=True)
