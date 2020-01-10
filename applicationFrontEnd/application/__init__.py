from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "HkAuRfVgEtY2G0AtY"

from application import routes
