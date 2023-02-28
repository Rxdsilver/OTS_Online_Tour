from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('home.html')


@bp.route('/declare-tournament')
def create_tournament_page():
    return render_template('create_tournament.html')


@bp.route('/join-tournament')
def join_tournament_page():
    return render_template('join_tournament.html')
