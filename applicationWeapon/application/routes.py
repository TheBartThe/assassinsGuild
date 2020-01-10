from application import app
from application.getWeapon import selectWeapon, weapons
from flask import jsonify

@app.route('/', methods=["GET"])
def correctAnswer():
    return jsonify(selectWeapon())
