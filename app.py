
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


# MEMBER 1: GET ALL TEAMS
@app.route("/api/teams", methods=["GET"])
def get_all_teams():
    return jsonify({
        "success": True,
        "teams": teams
    }), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
