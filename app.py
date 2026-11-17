
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


@app.route("/api/teams", methods=["POST"])
def create_team():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "success": False,
            "message": "Invalid JSON data"
        }), 400

    name = data.get("team_name")
    wins = data.get("wins")
    losses = data.get("losses")

    if (
        not isinstance(name, str)
        or not name.strip()
        or type(wins) is not int
        or type(losses) is not int
        or wins < 0
        or losses < 0
    ):
        return jsonify({
            "success": False,
            "message": "Invalid team information"
        }), 400

    new_id = max(
        (team["team_id"] for team in teams),
        default=0
    ) + 1

    new_team = {
        "team_id": new_id,
        "team_name": name.strip(),
        "wins": wins,
        "losses": losses,
        "points": wins * 3
    }

    teams.append(new_team)

    return jsonify({
        "success": True,
        "message": "Team created successfully",
        **new_team
    }), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)
