import random

metal_claw = {
    "type_": "Metal",
    "damage": 50,
    "accuracy": 0.95,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 14))/10,
}

iron_tail = {
    "type_": "Metal",
    "damage": 80,
    "accuracy": 0.75,
    "critical_chance": 0.15,
    "critical_multiplier": (random.randint(11, 14))/10,
}
