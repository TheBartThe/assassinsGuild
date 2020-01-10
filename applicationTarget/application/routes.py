from application import app
from getTarget import selectTarget

@app.route('/', methods=["GET"])
def target():
    return selectTarget()
