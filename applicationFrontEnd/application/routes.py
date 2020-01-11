from application import app
from flask import render_template, request
from application.forms import MissionForm
import requests

@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html', title = 'Home')

@app.route('/mission', methods=["GET"])
def mission():
    form = MissionForm()
    missionService = "http://mission:5001/"
    if request.method == 'GET':
        response = requests.get(missionService).json()
        return render_template('mission.html', title = 'Mission', form = form, data = response)
#    if request.method == 'POST':
#        response = requests.get(missionService).json()
#        return render_template('mission.html', title = 'Mission', form = form, data = response)
#    elif request.method == 'GET':
#        return render_template('missionRequest.html', title = 'Mission', form = form)
