from application import app
from application.mission import getMission
from flask import jsonify

@app.route('/', methods=["GET"])
def mission():
    targetService = "http://target:5002/"
    weaponService = "http://weapon:5003/"
    return jsonify(getMission(targetService, weaponService))
