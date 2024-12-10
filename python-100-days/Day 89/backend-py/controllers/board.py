from database.db_models import Board, db
from validation.board import CreateBoardForm, UpdateBoardForm


def create_board_controller(data):
    form = CreateBoardForm(data=data)

    if form.validate():
        new_board = Board(
            name=form.name.data
        )

        db.session.add(new_board)
        db.session.commit()

        response = Board.query.get(new_board.id).toDict()
        return response

    return {'error': 'Validation failed', 'details': form.errors}, 400


def update_board_controller(data):
    form = UpdateBoardForm(data=data)

    if form.validate():
        board = Board.query.get(form.id.data)
        board.name = form.name.data
        db.session.commit()

        return Board.query.get(form.id.data).toDict()

    return {'error': 'Validation failed', 'details': form.errors}, 400


def get_board_controller(board_name):
    try:
        board = Board.query.filter_by(name=board_name).one_or_404()
        return board.toDict()
    except:
        return {"error": "No board found"}, 404
