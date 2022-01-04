import json
from flask import Flask, render_template, request, redirect, flash, url_for, abort

app = Flask(__name__)
app.secret_key = 'something_special'


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


competitions = load_competitions()
clubs = load_clubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def show_summary():
    club = ""
    try:
        club = [club for club in clubs if club['email'] == request.form['email']][0]
    except IndexError:
        abort(500)

    return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])

    if places_required > 12:
        # It's impossible to reserve more than 12 places in a same tournament
        message = "You cannot reserve more than 12 places sorry !!"
        return render_template('booking.html', club=club, competition=competition, message=message)

    elif places_required > int(club['points']):
        # Club does not have enough points
        message = f"You don't have enough points ! You can reserve {club['points']} places maximum"
        return render_template('booking.html', club=club, competition=competition, message=message)

    elif places_required > int(competition["numberOfPlaces"]):
        # Tournament does not have enough places
        message = f"The competition doesn't have enough places ! " \
                  f"You can reserve {competition['numberOfPlaces']} places maximum"
        return render_template('booking.html', club=club, competition=competition, message=message)

    else:
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions)


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


# ==================
#   ERRORS MANAGER
# ==================

@app.errorhandler(500)
def email_does_not_exist(error):
    print(error)
    message = "This email is invalid or does not exist ! Please try again"
    return render_template('index.html', message=message, clubs=clubs), 500


if __name__ == '__main__':
    app.run(debug=True)
