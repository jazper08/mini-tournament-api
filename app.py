
from flask import Flask, jsonify, request

app = Flask(__name__)

teams = [
    {
        "team_id": 1,
        "team_name": "Blue Warriors",
        "wins": 3,
        "losses": 1,
        "points": 9
    },
    {
        "team_id": 2,
        "team_name": "Red Dragons",
        "wins": 2,
        "losses": 2,
        "points": 6
    },
    {
        "team_id": 3,
        "team_name": "Green Eagles",
        "wins": 1,
        "losses": 3,
        "points": 3
    }
]



@app.route("/api/teams", methods=["GET"])
def get_all_teams():
    return jsonify({
        "success": True,
        "teams": teams
    }), 200

@app.route("/api/teams/<int:team_id>", methods=["GET"])
def get_team_by_id(team_id):
    for team in teams:
        if team["team_id"] == team_id:
            return jsonify({
                "success": True,
                "team_id": team["team_id"],
                "team_name": team["team_name"],
                "wins": team["wins"],
                "losses": team["losses"],
                "points": team["points"]
            }), 200

    return jsonify({
        "success": False,
        "message": "Team not found"
    }), 404
if __name__ == "__main__":
    app.run(debug=True, port=5000)
