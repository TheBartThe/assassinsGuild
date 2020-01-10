from application import app
from application.getWeapon import selectWeapon

@app.route('/', methods=["GET"])
def correctAnswer():
    return selectWeapon()
