import requests

def getMission(targetService, weaponService):
    weaponList = request.get(weaponService)
    targetList = request.get(targetService)
    weapon = weaponList[0]
    target = targetList[0]
    points = (weaponList[1] * targetList[1])
    return ("Your target is " + target + ". You must use a " + weapon + ". Good luck.")
