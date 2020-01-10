import random

weapons = {
    "Machine Gun": 1,
    "Pistol": 2,
    "Sword": 3,
    "Baseball bat": 4,
    "Pencil": 5
    }

def selectWeapon():
    weapon = random.choice(list(weapons.keys()))
    points = weapons.get(weapon)
    return {"weapon": weapon,
            "weaponPoints": points}
