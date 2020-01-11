from flask import request
import requests

def getMission(targetService, weaponService):
    weaponList = requests.get(weaponService).json()
    targetList = requests.get(targetService).json()
    weapon = weaponList["weapon"]
    target = targetList["target"]
    points = (weaponList["weaponPoints"] * targetList["targetPoints"])
    credits = "credit" if (points == 1) else "credits"
    message = "Right, here is your mission. Your target is " + target + ". You must use a " + weapon + ". This will earn you " + str(points) + " " + credits + " with The Guild. Good luck. You have 48 hours. This message will now self destruct."
    return {"message": message}
