from flask import Flask,jsonify,request
import ipl
import ipl_2

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "message": "Welcome to the IPL API Service!",
        "status": "running",
        "endpoints": ["/teams", "/teamvteam", "/team-record","/batting-record","/bowling-record"]
    }

@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)

@app.route('/api/teamvteam')
def teamvteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')

    response = ipl.teamVteamAPI(team1,team2)

    return jsonify(response)

@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = ipl_2.teamAPI(team_name)
    return response

@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    response = ipl_2.batsmanAPI(batsman_name)
    return response

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = ipl_2.bowlerAPI(bowler_name)
    return response


app.run(debug=True)