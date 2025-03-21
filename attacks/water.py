import random

water_gun = {
    "type_": "Agua",
    "damage": 40,
    "accuracy": 0.75,
    "critical_chance": 0.15,
    "critical_multiplier": (random.randint(11, 15))/10,
}

water_pulse = {
    "type_": "Agua",
    "damage": 60,
    "accuracy": 0.60,
    "critical_chance": 0.12,
    "critical_multiplier": (random.randint(11, 15))/10,
}
