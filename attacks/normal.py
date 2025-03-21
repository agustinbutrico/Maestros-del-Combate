import random

quick_attack = {
    "type_": "Normal",
    "damage": 40,
    "accuracy": 0.75,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(14, 20))/10,
}

feint = {
    "type_": "Normal",
    "damage": 32,
    "accuracy": 0.85,
    "critical_chance": 0.26,
    "critical_multiplier": (random.randint(14, 20))/10,
}

tackle = {
    "type_": "Normal",
    "damage": 40,
    "accuracy": 0.75,
    "critical_chance": 0.15,
    "critical_multiplier": (random.randint(11, 15))/10,
}

rapid_spin = {
    "type_": "Normal",
    "damage": 50,
    "accuracy": 0.65,
    "critical_chance": 0.13,
    "critical_multiplier": (random.randint(11, 15))/10,
}

headbutt = {
    "type_": "Normal",
    "damage": 70,
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 14))/10,
}

mega_punch = {
    "type_": "Normal",
    "damage": 80,
    "accuracy": 0.85,
    "critical_chance": 0.17,
    "critical_multiplier": (random.randint(11, 13))/10,
}
