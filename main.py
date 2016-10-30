from flask import *
import time

app = Flask(__name__)
schedule = {'enabled'         : False,
            'sunday'          : False,
            'monday'          : False,
            'tuesday'         : False,
            'wednesday'       : False,
            'thursday'        : False,
            'friday'          : False,
            'saturday'        : False,
            'startTimeHour'   : "01",
            'startTimeMinute' : "00",
            'frontTime'       : 1,
            'backTime'        : 1,}
frontTimeRemaining = 0
backTimeRemaining  = 0

@app.route('/')
def mainPage():
    return render_template("main.html", **schedule)

@app.route('/action_stop_sprinklers/', methods=['POST'])
def action_stop_sprinklers():
    return make_response(redirect(url_for('mainPage')))

@app.route('/action_run_once/', methods=['POST'])
def action_run_once():
    frontTimeString = request.form['frontTime']
    backTimeString  = request.form['backTime']
    return make_response(redirect(url_for('mainPage')))

@app.route('/action_set_schedule/', methods=['POST'])
def action_set_schedule():
    schedule['enabled']         = 'enabled'   in request.form
    schedule['sunday']          = 'sunday'    in request.form
    schedule['monday']          = 'monday'    in request.form
    schedule['tuesday']         = 'tuesday'   in request.form
    schedule['wednesday']       = 'wednesday' in request.form
    schedule['thursday']        = 'thursday'  in request.form
    schedule['friday']          = 'friday'    in request.form
    schedule['saturday']        = 'saturday'  in request.form
    schedule['startTimeHour']   = request.form['startTime'][0:2]
    schedule['startTimeMinute'] = request.form['startTime'][3:5]
    schedule['frontTime']       = request.form['frontTime']
    schedule['backTime']        = request.form['backTime']
    return make_response(redirect(url_for('mainPage')))
    