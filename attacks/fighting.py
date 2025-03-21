import random

drain_punch = {
    "type_": "Lucha",
    "damage": 75,
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 13))/10,
}

power_up_punch = {
    "type_": "Lucha",
    "damage": 40,
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 13))/10,
}

focus_punch = {
    "type_": "Lucha",
    "damage": 120,
    "accuracy": 0.40,
    "critical_chance": 0.08,
    "critical_multiplier": (random.randint(11, 13))/10,
}
