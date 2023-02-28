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
    tournoi = Tournament.query.filter_by(code=code).first()
    joueur = Player(name=name, team=team, tournoi=tournoi)
    db.session.add(joueur)
    db.session.commit()
    return 'You successfully joined the tournament!'

@bp.route('/tournament', methods=['GET'])
def tournoi():
    code = request.args.get('code')
    tournoi = Tournament.query.filter_by(code=code).first()
    joueurs = Player.query.filter_by(tournoi=tournoi).all()
    return render_template('tournament.html', tournoi=tournoi, joueurs=joueurs)
