import random

targets = {
    "Mr Bean": 1,
    "Bruce Lee": 2,
    "Stringer Bell": 3,
    "John Wick": 4,
    "Batman": 5
    }

def selectTarget():
    target = random.choice(list(targets.keys()))
    points = targets.get(target)
    return {"target": target,
            "targetPoints": points}
