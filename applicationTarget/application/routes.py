from application import app
from application.getTarget import selectTarget
from flask import jsonify

@app.route('/', methods=["GET"])
def target():
    return jsonify(selectTarget())
