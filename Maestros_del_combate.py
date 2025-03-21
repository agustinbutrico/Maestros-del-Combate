import random
from time import sleep
from os import system
from readchar import readchar

CLS = "cls"
system(CLS)

# VARIABLES >

rock_done = False
water_done = False
electric_done = False
fighting_done = False
locations_true = False
game_true = False
true_1 = False
true_2 = False
true_3 = False
true_4 = False
true_5 = False
true_6 = False
playing = True
limiter = 0
new_position = None
rock_gym = None
water_gym = None
electric_gym = None
fighting_gym = None
hospital_1 = None
hospital_2 = None
locations = []

## snake
MAP_WIDTH = 20
MAP_HEIGHT = random.randint(MAP_WIDTH -5, MAP_WIDTH +10)
POS_X = 0 # pos 1* of list
POS_Y = 1 # pos 2* of list

pikachu = {
    "name": "Pikachu",
    "damage": random.randint(16, 23),
    "level": random.randint(30, 32),
    "base_hp": 51,
}
# Calculate max HP based on level
pikachu["max_hp"] = pikachu["base_hp"] + pikachu["level"] * 3
pikachu["hp"] = pikachu["max_hp"]  # Current HP starts at max

nuzzle = {
    "name": "Nuzzle",
    "damage": int(pikachu["damage"] * 1.5),
    "accuracy": 0.95,
    "critical_chance": 0.33,
    "critical_multiplier": (random.randint(14, 20))/10,
}
thunder_shock = {
    "name": "Thunder shock",
    "damage": int(pikachu["damage"] * 3),
    "accuracy": 0.65,
    "critical_chance": 0.18,
    "critical_multiplier": (random.randint(14, 20))/10,
}
quick_attack = {
    "name": "Quick attack",
    "damage": int(pikachu["damage"] * 2.5),
    "accuracy": 0.75,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(14, 20))/10,
}
feint = {
    "name": "Feint",
    "damage": int(pikachu["damage"] * 2),
    "accuracy": 0.85,
    "critical_chance": 0.26,
    "critical_multiplier": (random.randint(14, 20))/10,
}

squirtle = {
    "name": "Squirtle",
    "damage": random.randint(10, 12),
    "level": random.randint(26, 30),
    "base_hp": 70,
}
# Calculate max HP based on level
squirtle["max_hp"] = squirtle["base_hp"] + squirtle["level"] * 3
squirtle["hp"] = squirtle["max_hp"]  # Current HP starts at max

tackle = {
    "name": "Tackle",
    "damage": int(squirtle["damage"] * 4),
    "accuracy": 0.75,
    "critical_chance": 0.15,
    "critical_multiplier": (random.randint(11, 15))/10,
}
water_gun = {
    "name": "Water gun",
    "damage": int(squirtle["damage"] * 4),
    "accuracy": 0.75,
    "critical_chance": 0.15,
    "critical_multiplier": (random.randint(11, 15))/10,
}
rapid_spin = {
    "name": "Rapid spin",
    "damage": int(squirtle["damage"] * 5),
    "accuracy": 0.65,
    "critical_chance": 0.13,
    "critical_multiplier": (random.randint(11, 15))/10,
}
bite = {
    "name": "Bite",
    "damage": int(squirtle["damage"] * 6),
    "accuracy": 0.55,
    "critical_chance": 0.11,
    "critical_multiplier": (random.randint(11, 15))/10,
}
water_pulse = {
    "name": "Water pulse",
    "damage": int(squirtle["damage"] * 6),
    "accuracy": 0.60,
    "critical_chance": 0.12,
    "critical_multiplier": (random.randint(11, 15))/10,
}

lairon = {
    "name": "Lairon",
    "damage": random.randint(10, 12),
    "level": random.randint(29, 32),
    "base_hp": 84,
}
# Calculate max HP based on level
lairon["max_hp"] = lairon["base_hp"] + lairon["level"] * 3
lairon["hp"] = lairon["max_hp"]  # Current HP starts at max

metal_claw = {
    "name": "Metal claw",
    "damage": int(lairon["damage"] * 5),
    "accuracy": 0.95,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 14))/10,
}
rock_tomb = {
    "name": "Rock tomb",
    "damage": int(lairon["damage"] * 6),
    "accuracy": 0.95,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 14))/10,
}
headbutt = {
    "name": "Headbutt",
    "damage": int(lairon["damage"] * 7),
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 14))/10,
}
rock_slide = {
    "name": "Rock slide",
    "damage": int(lairon["damage"] * 7.5),
    "accuracy": 0.90,
    "critical_chance": 0.18,
    "critical_multiplier": (random.randint(11, 14))/10,
}
iron_tail = {
    "name": "Iron tail",
    "damage": int(lairon["damage"] * 8),
    "accuracy": 0.75,
    "critical_chance": 0.15,
    "critical_multiplier": (random.randint(11, 14))/10,
}

zapdos = {
    "name": "Zapdos",
    "damage": random.randint(10, 12),
    "level": random.randint(32, 34),
    "base_hp": 70,
}
# Calculate max HP based on level
zapdos["max_hp"] = zapdos["base_hp"] + zapdos["level"] * 3
zapdos["hp"] = zapdos["max_hp"]  # Current HP starts at max

peck = {
    "name": "Peck",
    "damage": int(zapdos["damage"] * 3.5),
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 12))/10,
}
pluck = {
    "name": "Pluck",
    "damage": int(zapdos["damage"] * 5),
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 12))/10,
}
ancient_power = {
    "name": "Ancient power",
    "damage": int(zapdos["damage"] * 6),
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 12))/10,
}
thunder = {
    "name": "Thunder",
    "damage": int(zapdos["damage"] * 9),
    "accuracy": 0.70,
    "critical_chance": 0.14,
    "critical_multiplier": (random.randint(11, 12))/10,
}
zap_cannon = {
    "name": "Zap cannon",
    "damage": int(zapdos["damage"] * 10),
    "accuracy": 0.50,
    "critical_chance": 0.10,
    "critical_multiplier": (random.randint(11, 12))/10,
}

hitmonchan = {
    "name": "Hitmonchan",
    "damage": random.randint(10, 12),
    "level": random.randint(33, 36),
    "base_hp": 74,
}
# Calculate max HP based on level
hitmonchan["max_hp"] = hitmonchan["base_hp"] + hitmonchan["level"] * 3
hitmonchan["hp"] = hitmonchan["max_hp"]  # Current HP starts at max

drain_punch = {
    "name": "Drain punch",
    "damage": int(hitmonchan["damage"] * 7.5),
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 13))/10,
}
power_up_punch = {
    "name": "Power up punch",
    "damage": int(hitmonchan["damage"] * 4),
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 13))/10,
}
fire_punch = {
    "name": "Fire punch",
    "damage": int(hitmonchan["damage"] * 7.5),
    "accuracy": 1.00,
    "critical_chance": 0.20,
    "critical_multiplier": (random.randint(11, 13))/10,
}
mega_punch = {
    "name": "Mega punch",
    "damage": int(hitmonchan["damage"] * 8),
    "accuracy": 0.85,
    "critical_chance": 0.17,
    "critical_multiplier": (random.randint(11, 13))/10,
}
focus_punch = {
    "name": "Focus punch",
    "damage": int(hitmonchan["damage"] * 12),
    "accuracy": 0.40,
    "critical_chance": 0.08,
    "critical_multiplier": (random.randint(11, 13))/10,
}

# < VARIABLES
def intro():
    location = ""
    while location not in ["1", "2", "3", "4"]:
        print(
            f"(i) Hospitals [H] restores HP\n\n(i) WASD to move\n\n"
            f"Pikachu {pikachu['hp']} HP            LVL {pikachu['level']}\n"
            f"{life_indicator(pikachu)}\n\n"
            "Pikachu know 4 movements\n  Nuzlle\n  Thunder Shock\n  Quick Attack\n  Feint\n"
        )
        location = input(
            "Where are you coming from:\n  North (1)\n  South (2)\n  East  (3)\n  West  (4)\n\n"
        )
        system(CLS)

        match location:
            case "1":
                my_position = [
                    random.randint(0, MAP_WIDTH - 1), random.randint(0, round(MAP_HEIGHT - ((MAP_HEIGHT - 1) / 1.5))),
                ]
            case "2":
                my_position = [
                    random.randint(0, MAP_WIDTH - 1), random.randint(round((MAP_HEIGHT + 1) / 1.5), MAP_HEIGHT - 1),
                ]
            case "3":
                my_position = [
                    random.randint(round((MAP_WIDTH + 1) / 1.5), MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1),
                ]
            case "4":
                my_position = [
                    random.randint(0, round(MAP_WIDTH - ((MAP_WIDTH - 1) / 1.5))), random.randint(0, MAP_HEIGHT - 1),
                ]
    return my_position

def time_battle_end(): # time
    sleep(2)

def obstacles_creation():
    obstacles = []
    for _ in range(MAP_HEIGHT):
        current_row = ""
        current_width = 0
        while current_width < MAP_WIDTH:
            possible_obstacles = [",,,", ",,", " "]
            weights = [2, 3, 95]
            obstacle = random.choices(possible_obstacles, weights=weights, k=1)[0]
            
            # Check if the obstacle fits in the remaining width
            if current_width + len(obstacle) > MAP_WIDTH:
                # If the obstacle doesn't fit, fill with a space
                current_row += " "
                current_width += 1
            else:
                current_row += obstacle
                current_width += len(obstacle)
        # Appends the current row to the grid
        obstacles.append(list(current_row))
    # returns the map with same dimentions with obstacles
    return obstacles

def battle_starts(enemy):
    print(
        f"{enemy['name']} {enemy['hp']} HP\n{life_indicator(enemy)}\n\n"
        f"Pikachu {pikachu['hp']} HP\n{life_indicator(pikachu)}\n\n"
        f"Pikachu's LVL {pikachu['level']}\n\n"
        f"Pikachu's Damage: {pikachu['damage']}\n\n"
    )

def attack_selection():
    message = ("Select your attack:\n\n"
    f"1.Nuzzle\n    {nuzzle['damage']} damage\n    {round(nuzzle['accuracy'] * 100)} accuracy\n    {round(nuzzle['critical_chance'] * 100)} critical chance\n\n"
    f"2.Thunder Shock\n    {thunder_shock['damage']} damage\n    {round(thunder_shock['accuracy'] * 100)} accuracy\n    {round(thunder_shock['critical_chance'] * 100)} critical chance\n\n"
    f"3.Quick Attack\n    {quick_attack['damage']} damage\n    {round(quick_attack['accuracy'] * 100)} accuracy\n    {round(quick_attack['critical_chance'] * 100)} critical chance\n\n"
    f"4.Feint\n    {feint['damage']} damage\n    {round(feint['accuracy'] * 100)} accuracy \n    {round(feint['critical_chance'] * 100)} critical chance\n\n")
    return message

def life_indicator(pokemon): # Health Bar
    if pokemon["hp"] >= 0:
        health_bar = int(pokemon["hp"] * 30 / pokemon["max_hp"])
        health_bar_print = "[{}{}]".format("#" * health_bar, " " *(30 - health_bar))
    elif pokemon["hp"] < 0:
        health_bar = int(-1 *(pokemon["hp"] * 30 / pokemon["max_hp"]))
        health_bar_print = "[{}{}]".format(" " *(30 - health_bar), "/" * health_bar)
    return health_bar_print

def damages(attacker, attack, enemy):
    print(f"{attacker} uses {attack['name']}\n")
    
    if random.random() < attack["accuracy"]:
        if random.random() < attack["critical_chance"]:
            damage_dealt = int(attack["damage"] * attack["critical_multiplier"])
            print(f"Critical hit! -{damage_dealt}\n")
        else:
            damage_dealt = attack["damage"]
            print(f"-{damage_dealt}\n")
        enemy["hp"] -= damage_dealt
    else:
        print("Miss___\n")
        
    print(f"{enemy['name']} {enemy['hp']} HP\n{life_indicator(enemy)}\n")

obstacles = obstacles_creation()
my_position = intro()

while not locations_true: # Locations creation
    while 0 <= limiter <= 5: 
        new_location = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
        if new_location not in locations and new_location != my_position and obstacles[new_location[POS_Y]][new_location[POS_X]] != ",":
            locations.append(new_location)
            if limiter == 0: # Rock Gym
                water_gym = new_location
                true_1 = True
            elif limiter == 1: # Water Gym
                rock_gym = new_location
                true_2 = True
            elif limiter == 2: # Electric Gym
                electric_gym = new_location
                true_3 = True
            elif limiter == 3: # Fighting Gym
                fighting_gym = new_location
                true_4 = True
            elif limiter == 4: # Hospital 1
                hospital_1 = new_location
                true_5 = True
            elif limiter == 5: # Hospital 2
                hospital_2 = new_location
                true_6 = True
            limiter += 1
        if true_1 and true_2 and true_3 and true_4 and true_5 and true_6:
            locations_true = True
    true_1 = False; true_2 = False; true_3 = False; true_4 = False; true_5 = False; true_6 = False; limiter = 0

while not game_true:
    system(CLS)
    # DRAW MAP >
    print("-"*(MAP_WIDTH* 2 + 3)) # Top

    for coordinate_y in range(MAP_HEIGHT): # Map and Fights
        print("|", end="") # left side

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "

            # LOCATIONS PRINT >
            if rock_gym[POS_X] == coordinate_x and rock_gym[POS_Y] == coordinate_y: # rock gym print
                char_to_draw = " R"
            if water_gym[POS_X] == coordinate_x and water_gym[POS_Y] == coordinate_y: # water gym print
                char_to_draw = " W"
            if electric_gym[POS_X] == coordinate_x and electric_gym[POS_Y] == coordinate_y: # electric gym print
                char_to_draw = " E"
            if fighting_gym[POS_X] == coordinate_x and fighting_gym[POS_Y] == coordinate_y: # fighting gym print
                char_to_draw = " F"
            if hospital_1[POS_X] == coordinate_x and hospital_1[POS_Y] == coordinate_y: # hospital 1 print
                char_to_draw = " H"
            if hospital_2[POS_X] == coordinate_x and hospital_2[POS_Y] == coordinate_y: # hospital 2 print
                char_to_draw = " H"
            # < LOCATIONS PRINT

            # YOU >
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y: # your position
                char_to_draw = " @" # you

                if hospital_1[POS_X] == coordinate_x and hospital_1[POS_Y] == coordinate_y: # enter hospital 1
                    true_1 = True
                if hospital_2[POS_X] == coordinate_x and hospital_2[POS_Y] == coordinate_y: # enter hospital 2
                    true_1 = True

                # GYMS FIGHTS >
                if not water_done: # Water Gym

                    if water_gym[POS_X] == coordinate_x and water_gym[POS_Y] == coordinate_y:
                        print(); system(CLS); input("You entered -Cerulean Water Gym-\n\n"); system(CLS)

                        while not water_done: # water gym fight

                            if pikachu["hp"] > 0:
                                my_turn = None
                                while my_turn not in ["1", "2", "3", "4", "exit"]:
                                    battle_starts(squirtle)
                                    my_turn = input(attack_selection()); system(CLS)

                                if my_turn == "1":
                                    damages(pikachu, nuzzle, squirtle)
                                elif my_turn == "2":
                                    damages(pikachu, thunder_shock, squirtle)
                                elif my_turn == "3":
                                    damages(pikachu, quick_attack, squirtle)
                                elif my_turn == "4":
                                    damages(pikachu, feint, squirtle)
                                elif my_turn == "exit":
                                    game_true = True; water_done = True; playing = False
                                time_battle_end(); system(CLS)

                            if playing:
                                if squirtle["hp"] > 0:
                                    turn = random.randint(1, 5)

                                    if turn == 1:
                                        damages(squirtle, tackle, pikachu)
                                    elif turn == 2:
                                        damages(squirtle, water_gun, pikachu)
                                    elif turn == 3:
                                        damages(squirtle, rapid_spin, pikachu)
                                    elif turn == 4:
                                        damages(squirtle, bite, pikachu)
                                    elif turn == 5:
                                        damages(squirtle, water_pulse, pikachu)
                                    time_battle_end(); system(CLS)

                            if squirtle["hp"] < 1:
                                true_2 = True
                                water_done = True

                                pikachu["max_hp"] += random.randint(6, 12)
                                pikachu["damage"] += 1
                                pikachu["level"] += 3

                                # pikachu_critical = ((pikachu_critical * 10) + 1)/10
                                # nuzzle["damage"] = int((pikachu["damage"]) * 2.5)
                                # thunder_shock["damage"] = int((pikachu["damage"]) * 4.5)
                                # quick_attack["damage"] = int((pikachu["damage"]) * 4)
                                # feint["damage"] = int((pikachu["damage"]) * 3)
                            elif pikachu["hp"] < 1:
                                true_3 = True
                                water_done = True

                if not rock_done: # Rock Gym

                    if rock_gym[POS_X] == coordinate_x and rock_gym[POS_Y] == coordinate_y:
                        print(); system(CLS); input("You entered -Pewter Rock Gym-\n\n"); system(CLS)

                        while not rock_done: # rock gym fight

                            if pikachu["hp"] > 0:
                                my_turn = None
                                while my_turn not in ["1", "2", "3", "4", "exit"]:
                                    battle_starts(lairon)
                                    my_turn = input(attack_selection()); system(CLS)

                                if my_turn == "1":
                                    damages(pikachu, nuzzle, lairon)
                                elif my_turn == "2":
                                    damages(pikachu, thunder_shock, lairon)
                                elif my_turn == "3":
                                    damages(pikachu, quick_attack, lairon)
                                elif my_turn == "4":
                                    damages(pikachu, feint, lairon)
                                elif my_turn == "exit":
                                    game_true = True; rock_done = True; playing = False
                                time_battle_end(); system(CLS)

                            if playing:
                                if lairon["hp"] > 0:
                                    turn = random.randint(1, 5)

                                    if turn == 1:
                                        damages(lairon, metal_claw, pikachu)
                                    elif turn == 2:
                                        damages(lairon, rock_tomb, pikachu)
                                    elif turn == 3:
                                        damages(lairon, headbutt, pikachu)
                                    elif turn == 4:
                                        damages(lairon, rock_slide, pikachu)
                                    elif turn == 5:
                                        damages(lairon, iron_tail, pikachu)
                                    time_battle_end(); system(CLS)

                            if lairon["hp"] < 1:
                                true_2 = True
                                rock_done = True

                                pikachu["max_hp"] += random.randint(7, 13)
                                pikachu["damage"] += 1
                                pikachu["level"] += 3

                                # pikachu_critical = ((pikachu_critical * 10) + 1)/10
                                # nuzzle["damage"] = int((pikachu["damage"]) * 2.5)
                                # thunder_shock["damage"] = int((pikachu["damage"]) * 4.5)
                                # quick_attack["damage"] = int((pikachu["damage"]) * 4)
                                # feint["damage"] = int((pikachu["damage"]) * 3)
                            elif pikachu["hp"] < 1:
                                true_3 = True
                                rock_done = True

                if not electric_done: # Electric Gym

                    if electric_gym[POS_X] == coordinate_x and electric_gym[POS_Y] == coordinate_y:
                        print(); system(CLS); input("You entered -Vermilion Electric Gym-\n\n"); system(CLS)

                        while not electric_done: # electric gym fight

                            if pikachu["hp"] > 0:
                                my_turn = None
                                while my_turn not in ["1", "2", "3", "4", "exit"]:
                                    battle_starts(zapdos)
                                    my_turn = input(attack_selection()); system(CLS)

                                if my_turn == "1":
                                    damages(pikachu, nuzzle, zapdos)
                                elif my_turn == "2":
                                    damages(pikachu, thunder_shock, zapdos)
                                elif my_turn == "3":
                                    damages(pikachu, quick_attack, zapdos)
                                elif my_turn == "4":
                                    damages(pikachu, feint, zapdos)
                                elif my_turn == "exit":
                                    game_true = True; electric_done = True; playing = False
                                time_battle_end(); system(CLS)

                            if playing:
                                if zapdos["hp"] > 0:
                                    turn = random.randint(1, 5)

                                    if turn == 1:
                                        damages(zapdos, peck, pikachu)
                                    elif turn == 2:
                                        damages(zapdos, pluck, pikachu)
                                    elif turn == 3:
                                        damages(zapdos, ancient_power, pikachu)
                                    elif turn == 4:
                                        damages(zapdos, thunder, pikachu)
                                    elif turn == 5:
                                        damages(zapdos, zap_cannon, pikachu)
                                    time_battle_end(); system(CLS)

                            if zapdos["hp"] < 1:
                                true_2 = True
                                electric_done = True

                                pikachu["max_hp"] += random.randint(8, 14)
                                pikachu["damage"] += 2
                                pikachu["level"] += 3

                                # pikachu_critical = ((pikachu_critical * 10) + 1)/10
                                # nuzzle["damage"] = int((pikachu["damage"]) * 2.5)
                                # thunder_shock["damage"] = int((pikachu["damage"]) * 4.5)
                                # quick_attack["damage"] = int((pikachu["damage"]) * 4)
                                # feint["damage"] = int((pikachu["damage"]) * 3)
                            elif pikachu["hp"] < 1:
                                true_3 = True
                                electric_done = True

                if not fighting_done: # Fighting Gym

                    if fighting_gym[POS_X] == coordinate_x and fighting_gym[POS_Y] == coordinate_y:
                        print(); system(CLS); input("You entered -Cianwood Fighting Gym\n\n"); system(CLS)

                        while not fighting_done: # fighting gym fight

                            if pikachu["hp"] > 0:
                                my_turn = None
                                while my_turn not in ["1", "2", "3", "4", "exit"]:
                                    battle_starts(hitmonchan)
                                    my_turn = input(attack_selection()); system(CLS)

                                if my_turn == "1":
                                    damages(pikachu, nuzzle, hitmonchan)
                                elif my_turn == "2":
                                    damages(pikachu, thunder_shock, hitmonchan)
                                elif my_turn == "3":
                                    damages(pikachu, quick_attack, hitmonchan)
                                elif my_turn == "4":
                                    damages(pikachu, feint, hitmonchan)
                                elif my_turn == "exit":
                                    game_true = True; fighting_done = True; playing = False
                                time_battle_end(); system(CLS)

                            if playing:
                                if hitmonchan["hp"] > 0:
                                    turn = random.randint(1, 5)

                                    if turn == 1:
                                        damages(hitmonchan, drain_punch, pikachu)
                                    elif turn == 2:
                                        damages(hitmonchan, power_up_punch, pikachu)
                                    elif turn == 3:
                                        damages(hitmonchan, fire_punch, pikachu)
                                    elif turn == 4:
                                        damages(hitmonchan, mega_punch, pikachu)
                                    elif turn == 5:
                                        damages(hitmonchan, focus_punch, pikachu)
                                    time_battle_end(); system(CLS)

                            if hitmonchan["hp"] < 1:
                                true_2 = True
                                fighting_done = True

                                pikachu["max_hp"] += random.randint(10, 16)
                                pikachu["damage"] += 2
                                pikachu["level"] += 3

                                # pikachu_critical = ((pikachu_critical * 10) + 1)/10
                                # nuzzle["damage"] = int((pikachu["damage"]) * 2.5)
                                # thunder_shock["damage"] = int((pikachu["damage"]) * 4.5)
                                # quick_attack["damage"] = int((pikachu["damage"]) * 4)
                                # feint["damage"] = int((pikachu["damage"]) * 3)
                            elif pikachu["hp"] < 1:
                                true_3 = True
                                fighting_done = True
      
                # < GYMS FIGHTS
            # < YOU

            # WALLS PRINT >
            if obstacles[coordinate_y][coordinate_x] == ",": # Walls
                if obstacles[my_position[POS_Y]][my_position[POS_X]] == ",": # don't draw walls on you
                    obstacles[my_position[POS_Y]][my_position[POS_X]] = " "
                if obstacles[my_position[POS_Y]][my_position[POS_X]] != ",": # walls print
                    char_to_draw = " #"
            # < WALLS PRINT

            print("{}".format(char_to_draw), end="") # Printer
        print(" |") # right side

    print("-"*(MAP_WIDTH* 2 + 3)) # Bottom
    # < DRAW MAP

    # CONDITIONS >
    if true_1: # Hospital
        pikachu["hp"] = pikachu["max_hp"]
        print(); system(CLS)
        print("Pikachu's HP Restored\n\nMove to Continue\n")
        true_1 = False
    if true_2: # Gym win
        system(CLS); print(f"Pikachu grew to LVL {pikachu['level'] - 2}!\n"
                               f"Pikachu grew to LVL {pikachu['level'] - 1}!\n"
                               f"Pikachu grew to LVL {pikachu['level']}!\n\n"
                               "Gym Cleared\n\nMove to Continue\n")
        true_2 = False
    if true_3: # Gym lost
        system(CLS); print("Gym Fight Losed\n\nYou Lose\n")
        game_true = True
    if rock_done and water_done and electric_done and fighting_done: # win conditions
        system(CLS); print("Congratulations! You win all battles!\n\nYou Win!\n")
        game_true = True
    if not playing: # exit game
        print(); system(CLS)
    # < CONDITIONS

    if not game_true and not true_3:
        direction = readchar() # where user want to move

        if direction.upper() == "W" or direction.upper() == "5": # up movement
            new_position = [my_position[POS_X], my_position[POS_Y] - 1]
            if new_position[POS_Y] < 0:
                new_position[POS_Y] = MAP_HEIGHT - 1

        elif direction.upper() == "S" or direction.upper() == "2": # down movement
            new_position = [my_position[POS_X], my_position[POS_Y] + 1]
            if new_position[POS_Y] > MAP_HEIGHT - 1:
                new_position[POS_Y] = 0

        elif direction.upper() == "A" or direction.upper() == "1": # left movement
            new_position = [my_position[POS_X] - 1, my_position[POS_Y]]
            if new_position[POS_X] < 0:
                new_position[POS_X] = MAP_WIDTH - 1

        elif direction.upper() == "D" or direction.upper() == "3": # right movement
            new_position = [my_position[POS_X] + 1, my_position[POS_Y]]
            if new_position[POS_X] > MAP_WIDTH - 1:
                new_position[POS_X] = 0

        elif direction.upper() == "P": # right movement
            game_true = True

        if new_position: # in-game movement
            if obstacles[new_position[POS_Y]][new_position[POS_X]] != ",":
                my_position = new_position

# End