from application import app
from application.getTarget import selectTarget

@app.route('/', methods=["GET"])
def target():
    return selectTarget()
