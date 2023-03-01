from flask import Blueprint, render_template, request
from ..models import db, Tournament, Player

bp = Blueprint('tournament', __name__)

@bp.route('/add-tournament', methods=['POST'])
def add_tournament():
    code = request.form['code']
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    tournament = Tournament(code=code, start_date=start_date, end_date=end_date)
    db.session.add(tournament)
    db.session.commit()
    return 'Tournament successfully created !'

@bp.route('/add-player', methods=['POST'])
def add_player():
    code = request.form['code']
    name = request.form['name']
    team = request.form['team']
    player = Player(name=name, team=team, code=code)
    db.session.add(player)
    db.session.commit()
    return 'You successfully joined the tournament!'

@bp.route('/<int:tournament_id>/players')
def tournament_players(tournament_id):
    tournament = Tournament.query.get_or_404(tournament_id)
    players = Player.query.filter_by(code=tournament.code).all()
    return render_template('tournament_players.html', tournament=tournament, players=players)

@bp.route('/tournament-list')
def tournament_list():
    tournaments = Tournament.query.all()
    return render_template('tournament_list.html', tournaments=tournaments)
