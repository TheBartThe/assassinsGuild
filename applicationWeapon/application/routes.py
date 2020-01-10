from application import app
from getWeapon import selectWeapon

@app.route('/', methods=["GET"])
def correctAnswer():
    return selectWeapon()
