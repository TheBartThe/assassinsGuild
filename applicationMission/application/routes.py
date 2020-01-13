from application import app
from application.mission import getMission, requestTarget, requestWeapon
from flask import jsonify

@app.route('/', methods=["GET"])
def mission():
    targetService = "http://target:5002/"
    weaponService = "http://weapon:5003/"
    targetList = requestTarget(targetService)
    weaponList = requestWeapon(weaponService)
    return jsonify(getMission(targetList, weaponList))
