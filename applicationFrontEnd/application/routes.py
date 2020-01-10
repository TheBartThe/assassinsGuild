from application import app
from flask import render_template, request
from application.forms import MissionForm
import requests

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/mission', methods=["GET", "POST"])
def mission():
    form = MissionForm()
    targetService = "http://127.0.0.1:5002/"
    return render_template('mission.html', title = 'Mission', form = form)
