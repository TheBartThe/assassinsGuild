from application import app
from application.mission import getMission

@app.route('/', methods=["GET"])
def mission():
    targetService = "http://127.0.0.1:5002/"
    weaponService = "http://127.0.0.1:5003/"
    return getMission(targetService, weaponService)
