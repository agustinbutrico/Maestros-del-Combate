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
odds = [",,,", ",,", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

pikachu_damage = random.randint(16, 23)
pikachu_critical =(random.randint(14, 20))/10
pikachu_lvl = random.randint(30, 32)
pikachu_base_hp = 51
pikachu_hp = pikachu_base_hp + pikachu_lvl*3
PIKACHU_LVL_BASED_HP = pikachu_hp
nuzzle = int(pikachu_damage * 1.5); nuzzle_range = 260 ; nuzzle_posibility = 245                         # damage(24, 34)     95% acurracy     33% critical
thunder_shock = int(pikachu_damage * 3); thunder_shock_range = 340; thunder_shock_posibility = 220       # damage(48, 69)     65% acurracy     18% critical
quick_attack = int(pikachu_damage * 2.5); quick_attack_range = 294; quick_attack_posibility = 220        # damage(40, 57)     75% acurracy     20% critical
feint = int(pikachu_damage * 2); feint_range = 270; feint_posibility = 230                               # damage(32, 46)     85% acurracy     26% critical

squirtle_damage = random.randint(10, 12)
squirtle_critical =(random.randint(11, 15))/10
squirtle_lvl = random.randint(26, 30)
squirtle_base_hp = 70
squirtle_hp = squirtle_base_hp + squirtle_lvl*3
SQUIRTLE_LVL_BASED_HP = squirtle_hp
tackle = int(squirtle_damage * 4); tackle_range = 268; tackle_posibility = 200                           # damage(40, 48)     75% acurracy     15% critical
water_gun = int(squirtle_damage * 4); water_gun_range = 268; water_gun_posibility = 200                  # damage(40, 48)     75% acurracy     15% critical
rapid_spin = int(squirtle_damage * 5); rapid_spin_range = 310; rapid_spin_posibility = 200               # damage(50, 60)     65% acurracy     13% critical
bite = int(squirtle_damage * 6); bite_range = 365; bite_posibility = 200                                 # damage(60, 72)     55% acurracy     11% critical
water_pulse = int(squirtle_damage * 6); water_pulse_range = 336; water_pulse_posibility = 200            # damage(60, 72)     60% acurracy     12% critical

lairon_damage = random.randint(10, 12)
lairon_critical =(random.randint(11, 14))/10
lairon_lvl = random.randint(29, 32)
lairon_base_hp = 84
lairon_hp = lairon_base_hp + lairon_lvl*3
LAIRON_LVL_BASED_HP = lairon_hp
metal_claw = int(lairon_damage * 5); metal_claw_range = 210; metal_claw_posibility = 200                 # damage(50, 60)     95%  acurracy    20% critical
rock_tomb = int(lairon_damage * 6); rock_tomb_range = 210; rock_tomb_posibility = 200                    # damage(60, 72)     95%  acurracy    20% critical
headbutt = int(lairon_damage * 7); headbutt_range = 200; headbutt_posibility = 200                       # damage(70, 84)     100% acurracy    20% critical
rock_slide = int(lairon_damage * 7.5); rock_slide_range = 222; rock_slide_posibility = 200               # damage(75, 90)     90%  acurracy    18% critical
iron_tail = int(lairon_damage * 8); iron_tail_range = 268; iron_tail_posibility = 200                    # damage(80, 96)     75%  acurracy    15% critical

zapdos_damage = random.randint(10, 12)
zapdos_critical =(random.randint(11, 12))/10
zapdos_lvl = random.randint(32, 34)
zapdos_base_hp = 70
zapdos_hp = zapdos_base_hp + zapdos_lvl*3
ZAPDOS_LVL_BASED_HP = zapdos_hp
peck = int(zapdos_damage * 3.5); peck_range = 200; peck_posibility = 200                                 # damage(35, 42)     100% acurracy    20% critical
pluck = int(zapdos_damage * 5); pluck_range = 200; pluck_posibility = 200                                # damage(50, 60)     100% acurracy    20% critical
ancient_power = int(zapdos_damage * 6); ancient_power_range = 200; ancient_power_posibility = 200        # damage(60, 72)     100% acurracy    20% critical
thunder = int(zapdos_damage * 9); thunder_range = 288; thunder_posibility = 200                          # damage(90, 108)     70% acurracy    14% critical
zap_cannon = int(zapdos_damage * 10); zap_cannon_range = 400; zap_cannon_posibility = 200                # damage(100, 120)    50% acurracy    10% critical

hitmonchan_damage = random.randint(10, 12)
hitmonchan_critical =(random.randint(11, 13))/10
hitmonchan_lvl = random.randint(33, 36)
hitmonchan_base_hp = 74
hitmonchan_hp = hitmonchan_base_hp + hitmonchan_lvl*3
HITMONCHAN_LVL_BASED_HP = hitmonchan_hp
drain_punch = int(hitmonchan_damage * 7.5); drain_punch_range = 200; drain_punch_posibility = 200        # damage(75, 90)     100% acurracy    20% critical
power_up_punch = int(hitmonchan_damage * 4); power_up_punch_range = 200; power_up_punch_posibility = 200 # damage(40, 48)     100% acurracy    20% critical
fire_punch = int(hitmonchan_damage * 7.5); fire_punch_range = 200; fire_punch_posibility = 200           # damage(75, 90)     100% acurracy    20% critical
mega_punch = int(hitmonchan_damage * 8); mega_punch_range = 235; mega_punch_posibility = 200             # damage(80, 96)      85% acurracy    17% critical
focus_punch = int(hitmonchan_damage * 12); focus_punch_range = 500; focus_punch_posibility = 200         # damage(120, 144)    40% acurracy     8% critical

# < VARIABLES
def intro(loc):
    while loc not in ["1", "2", "3", "4"]:
        print(f"(i) Hospitals [H] restores HP\n\n(i) WASD to move\n\nPikachu {pikachu_hp} HP            LVL "
            f"{pikachu_lvl}\n{life_indicator(pikachu_hp, PIKACHU_LVL_BASED_HP)}\n\n"
            "Pikachu know 4 movements\n  Nuzlle\n  Thunder Shock\n  Quick Attack\n  Feint\n")
        loc = input("Where you are coming from:\n  North (1)\n  South (2)\n  East  (3)\n  West  (4)\n\n"); system(CLS)
        return loc

def start_position():
    loc = intro("")
    if loc == "1":
        my_position = [random.randint(0, MAP_WIDTH -1), random.randint(0, round(MAP_HEIGHT -((MAP_HEIGHT - 1)/1.5)) )]
    elif loc == "2":
        my_position = [random.randint(0, MAP_WIDTH -1), random.randint(round((MAP_HEIGHT + 1)/1.5), MAP_HEIGHT -1)]
    elif loc == "3":
        my_position = [random.randint(round((MAP_WIDTH + 1)/1.5), MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
    elif loc == "4":
        my_position = [random.randint(0, round(MAP_WIDTH -((MAP_WIDTH - 1)/1.5)) ), random.randint(0, MAP_HEIGHT -1)]
    return my_position

def time_battle_end(): # time
    sleep(2)

def obstacles_creation(): # Obstacle Colocation
    obstacles = ""; obstacle = 0; limiter_h = 0; limiter_w = 0
    while limiter_h < MAP_HEIGHT: # random map generator
        while limiter_w < MAP_WIDTH:
            obstacle = random.choice(odds)
            if obstacle == " ":
                limiter_w += 1
            elif obstacle == ",,":
                limiter_w += 2
            elif obstacle == ",,,":
                limiter_w += 3
            obstacles += obstacle
        obstacles += "."
        limiter_h += 1; limiter_w = 0
    obstacles = [list(row) for row in obstacles.split(".")]
    return obstacles

def battle_starts(enemy_pokemon, enemy_pokemon_hp, enemy_LVL_BASED_HP):
    print(f"{enemy_pokemon} {enemy_pokemon_hp} HP\n{life_indicator(enemy_pokemon_hp, enemy_LVL_BASED_HP)}\n\n"
          f"Pikachu {pikachu_hp} HP\n{life_indicator(pikachu_hp, PIKACHU_LVL_BASED_HP)}\n\n"
          f"Pikachu's LVL {pikachu_lvl}\n\n"
          f"Pikachu's Critical: [ {pikachu_critical} ]\n\n"
          f"Pikachu's Damage: [ {pikachu_damage} ]\n\n")

def life_indicator(pokemon_hp, pokemon_LVL_BASED_HP): # Health Bar
    if pokemon_hp >= 0:
        health_bar = int(pokemon_hp * 30 / pokemon_LVL_BASED_HP)
        health_bar_print = "[{}{}]".format("#" * health_bar, " " *(30 - health_bar))
        return health_bar_print
    elif pokemon_hp < 0:
        health_bar = int(-1 *(pokemon_hp * 30 / pokemon_LVL_BASED_HP))
        health_bar_print = "[{}{}]".format(" " *(30 - health_bar), "/" * health_bar)
        return health_bar_print

def damages(pokemon_txt, pokemon_attack_txt, pokemon_attack, attack_range, attack_posibility, pokemon_critical, enemy_pokemon, enemy_pokemon_hp, enemy_LVL_BASED_HP):
    print(f"{pokemon_txt} uses {pokemon_attack_txt}\n") # 'Pokemon uses attack'
    attack = random.randint(0, attack_range); sleep(1)
    if attack <= 160:
        enemy_pokemon_hp -= pokemon_attack # normal damage
        print(f"-{pokemon_attack}\n")
    elif 160 < attack <= attack_posibility:
        enemy_pokemon_hp -= int(pokemon_attack * pokemon_critical) # special damage
        print(f"critical___ -{int(pokemon_attack * pokemon_critical)}\n")
    elif attack_posibility < attack:
        enemy_pokemon_hp -= 0 # miss
        print("miss___\n")
    print(f"{enemy_pokemon} {enemy_pokemon_hp} HP\n{life_indicator(enemy_pokemon_hp, enemy_LVL_BASED_HP)}\n")
    return enemy_pokemon_hp

obstacles = obstacles_creation()
my_position = start_position()

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

                            if pikachu_hp > 0:
                                my_turn = None
                                while my_turn not in ["1", "2", "3", "4", "exit"]:
                                    battle_starts("Squirtle", squirtle_hp, SQUIRTLE_LVL_BASED_HP)
                                    my_turn = input("Select your attack:\n\n"
                                                    f"1.Nuzzle\n    {nuzzle} damage\n    95 acurracy\n    33 critical chance\n\n"
                                                    f"2.Thunder Shock\n    {thunder_shock} damage\n    65 acurracy\n    18 critical chance\n\n"
                                                    f"3.Quick Attack\n    {quick_attack} damage\n    75 acurracy\n    20 critical chance\n\n"
                                                    f"4.Feint\n    {feint} damage\n    85 acurracy \n    26 critical chance\n\n"); system(CLS)

                                if my_turn == "1":
                                    squirtle_hp = damages("Pikachu", "Nuzlle", nuzzle, nuzzle_range, nuzzle_posibility, pikachu_critical, 
                                                            "Squirtle", squirtle_hp, SQUIRTLE_LVL_BASED_HP)
                                elif my_turn == "2":
                                    squirtle_hp = damages("Pikachu", "Thunder Shock", thunder_shock, thunder_shock_range, thunder_shock_posibility, pikachu_critical, 
                                                            "Squirtle", squirtle_hp, SQUIRTLE_LVL_BASED_HP)
                                elif my_turn == "3":
                                    squirtle_hp = damages("Pikachu", "Quick Attack", quick_attack, quick_attack_range, quick_attack_posibility, pikachu_critical, 
                                                            "Squirtle", squirtle_hp, SQUIRTLE_LVL_BASED_HP)
                                elif my_turn == "4":
                                    squirtle_hp = damages("Pikachu", "Feint", feint, feint_range, feint_posibility, pikachu_critical, 
                                                            "Squirtle", squirtle_hp, SQUIRTLE_LVL_BASED_HP)
                                elif my_turn == "exit":
                                    game_true = True; water_done = True; playing = False
                                time_battle_end(); system(CLS)

                            if playing:
                                if squirtle_hp > 0:
                                    turn = random.randint(1, 5)

                                    if turn == 1:
                                        pikachu_hp = damages("Squirtle", "Tackle", tackle, tackle_range, tackle_posibility, squirtle_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 2:
                                        pikachu_hp = damages("Squirtle", "Water Gun", water_gun, water_gun_range, water_gun_posibility, squirtle_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 3:
                                        pikachu_hp = damages("Squirtle", "Rapid Spin", rapid_spin, rapid_spin_range, rapid_spin_posibility, squirtle_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 4:
                                        pikachu_hp = damages("Squirtle", "Bite", bite, bite_range, bite_posibility, squirtle_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 5:
                                        pikachu_hp = damages("Squirtle", "Water Pulse", water_pulse, water_pulse_range, water_pulse_posibility, squirtle_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    time_battle_end(); system(CLS)

                            if squirtle_hp < 1:
                                true_2 = True
                                water_done = True
                                PIKACHU_LVL_BASED_HP += random.randint(6, 12)
                                pikachu_critical = ((pikachu_critical * 10) + 1)/10
                                pikachu_damage += 1
                                nuzzle = int((pikachu_damage) * 2.5)
                                thunder_shock = int((pikachu_damage) * 4.5)
                                quick_attack = int((pikachu_damage) * 4)
                                feint = int((pikachu_damage) * 3)
                                pikachu_lvl += 3
                            elif pikachu_hp < 1:
                                true_3 = True
                                water_done = True

                if not rock_done: # Rock Gym

                    if rock_gym[POS_X] == coordinate_x and rock_gym[POS_Y] == coordinate_y:
                        print(); system(CLS); input("You entered -Pewter Rock Gym-\n\n"); system(CLS)

                        while not rock_done: # rock gym fight

                            if pikachu_hp > 0:
                                my_turn = None
                                while my_turn not in ["1", "2", "3", "4", "exit"]:
                                    battle_starts("Lairon", lairon_hp, LAIRON_LVL_BASED_HP)
                                    my_turn = input("Select your attack:\n\n"
                                                    f"1.Nuzzle\n    {nuzzle} damage\n    95 acurracy\n    33 critical chance\n\n"
                                                    f"2.Thunder Shock\n    {thunder_shock} damage\n    65 acurracy\n    18 critical chance\n\n"
                                                    f"3.Quick Attack\n    {quick_attack} damage\n    75 acurracy\n    20 critical chance\n\n"
                                                    f"4.Feint\n    {feint} damage\n    85 acurracy \n    26 critical chance\n\n"); system(CLS)

                                if my_turn == "1":
                                    lairon_hp = damages("Pikachu", "Nuzlle", nuzzle, nuzzle_range, nuzzle_posibility, pikachu_critical, 
                                                        "Lairon", lairon_hp, LAIRON_LVL_BASED_HP)
                                elif my_turn == "2":
                                    lairon_hp = damages("Pikachu", "Thunder Shock", thunder_shock, thunder_shock_range, thunder_shock_posibility, pikachu_critical, 
                                                        "Lairon", lairon_hp, LAIRON_LVL_BASED_HP)
                                elif my_turn == "3":
                                    lairon_hp = damages("Pikachu", "Quick Attack", quick_attack, quick_attack_range, quick_attack_posibility, pikachu_critical, 
                                                        "Lairon", lairon_hp, LAIRON_LVL_BASED_HP)
                                elif my_turn == "4":
                                    lairon_hp = damages("Pikachu", "Feint", feint, feint_range, feint_posibility, pikachu_critical, 
                                                        "Lairon", lairon_hp, LAIRON_LVL_BASED_HP)
                                elif my_turn == "exit":
                                    game_true = True; rock_done = True; playing = False
                                time_battle_end(); system(CLS)

                            if playing:
                                if lairon_hp > 0:
                                    turn = random.randint(1, 5)

                                    if turn == 1:
                                        pikachu_hp = damages("Lairon", "Metal Claw", metal_claw, metal_claw_range, metal_claw_posibility, lairon_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 2:
                                        pikachu_hp = damages("Lairon", "Rock Tomb", rock_tomb, rock_tomb_range, rock_tomb_posibility, lairon_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 3:
                                        pikachu_hp = damages("Lairon", "Headbutt", headbutt, headbutt_range, headbutt_posibility, lairon_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 4:
                                        pikachu_hp = damages("Lairon", "Rock Slide", rock_slide, rock_slide_range, rock_slide_posibility, lairon_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 5:
                                        pikachu_hp = damages("Lairon", "Iron Tail", iron_tail, iron_tail_range, iron_tail_posibility, lairon_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    time_battle_end(); system(CLS)

                            if lairon_hp < 1:
                                true_2 = True
                                rock_done = True
                                PIKACHU_LVL_BASED_HP += random.randint(7, 13)
                                pikachu_critical = ((pikachu_critical * 10) + 1)/10
                                pikachu_damage += 1
                                nuzzle = int((pikachu_damage) * 2.5)
                                thunder_shock = int((pikachu_damage) * 4.5)
                                quick_attack = int((pikachu_damage) * 4)
                                feint = int((pikachu_damage) * 3)
                                pikachu_lvl += 3
                            elif pikachu_hp < 1:
                                true_3 = True
                                rock_done = True

                if not electric_done: # Electric Gym

                    if electric_gym[POS_X] == coordinate_x and electric_gym[POS_Y] == coordinate_y:
                        print(); system(CLS); input("You entered -Vermilion Electric Gym-\n\n"); system(CLS)

                        while not electric_done: # electric gym fight

                            if pikachu_hp > 0:
                                my_turn = None
                                while my_turn not in ["1", "2", "3", "4", "exit"]:
                                    battle_starts("Zapdos", zapdos_hp, ZAPDOS_LVL_BASED_HP)
                                    my_turn = input("Select your attack:\n\n"
                                                    f"1.Nuzzle\n    {nuzzle} damage\n    95 acurracy\n    33 critical chance\n\n"
                                                    f"2.Thunder Shock\n    {thunder_shock} damage\n    65 acurracy\n    18 critical chance\n\n"
                                                    f"3.Quick Attack\n    {quick_attack} damage\n    75 acurracy\n    20 critical chance\n\n"
                                                    f"4.Feint\n    {feint} damage\n    85 acurracy \n    26 critical chance\n\n"); system(CLS)

                                if my_turn == "1":
                                    zapdos_hp = damages("Pikachu", "Nuzlle", nuzzle, nuzzle_range, nuzzle_posibility, pikachu_critical, 
                                                        "Zapdos", zapdos_hp, ZAPDOS_LVL_BASED_HP)
                                elif my_turn == "2":
                                    zapdos_hp = damages("Pikachu", "Thunder Shock", thunder_shock, thunder_shock_range, thunder_shock_posibility, pikachu_critical, 
                                                        "Zapdos", zapdos_hp, ZAPDOS_LVL_BASED_HP)
                                elif my_turn == "3":
                                    zapdos_hp = damages("Pikachu", "Quick Attack", quick_attack, quick_attack_range, quick_attack_posibility, pikachu_critical, 
                                                        "Zapdos", zapdos_hp, ZAPDOS_LVL_BASED_HP)
                                elif my_turn == "4":
                                    zapdos_hp = damages("Pikachu", "Feint", feint, feint_range, feint_posibility, pikachu_critical, 
                                                        "Zapdos", zapdos_hp, ZAPDOS_LVL_BASED_HP)
                                elif my_turn == "exit":
                                    game_true = True; electric_done = True; playing = False
                                time_battle_end(); system(CLS)

                            if playing:
                                if zapdos_hp > 0:
                                    turn = random.randint(1, 5)

                                    if turn == 1:
                                        pikachu_hp = damages("Zapdos", "Peck", peck, peck_range, peck_posibility, zapdos_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 2:
                                        pikachu_hp = damages("Zapdos", "Pluck", pluck, pluck_range, pluck_posibility, zapdos_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 3:
                                        pikachu_hp = damages("Zapdos", "Ancient Power", ancient_power, ancient_power_range, ancient_power_posibility, zapdos_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 4:
                                        pikachu_hp = damages("Zapdos", "Thunder", thunder, thunder_range, thunder_posibility, zapdos_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 5:
                                        pikachu_hp = damages("Zapdos", "Zap Cannon", zap_cannon, zap_cannon_range, zap_cannon_posibility, zapdos_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    time_battle_end(); system(CLS)

                            if zapdos_hp < 1:
                                true_2 = True
                                electric_done = True
                                PIKACHU_LVL_BASED_HP += random.randint(8, 14)
                                pikachu_critical = ((pikachu_critical * 10) + 2)/10
                                pikachu_damage += 2
                                nuzzle = int((pikachu_damage) * 2.5)
                                thunder_shock = int((pikachu_damage) * 4.5)
                                quick_attack = int((pikachu_damage) * 4)
                                feint = int((pikachu_damage) * 3)
                                pikachu_lvl += 3
                            elif pikachu_hp < 1:
                                true_3 = True
                                electric_done = True

                if not fighting_done: # Fighting Gym

                    if fighting_gym[POS_X] == coordinate_x and fighting_gym[POS_Y] == coordinate_y:
                        print(); system(CLS); input("You entered -Cianwood Fighting Gym\n\n"); system(CLS)

                        while not fighting_done: # fighting gym fight

                            if pikachu_hp > 0:
                                my_turn = None
                                while my_turn not in ["1", "2", "3", "4", "exit"]:
                                    battle_starts("Hitmonchan", hitmonchan_hp, HITMONCHAN_LVL_BASED_HP)
                                    my_turn = input("Select your attack:\n\n"
                                                    f"1.Nuzzle\n    {nuzzle} damage\n    95 acurracy\n    33 critical chance\n\n"
                                                    f"2.Thunder Shock\n    {thunder_shock} damage\n    65 acurracy\n    18 critical chance\n\n"
                                                    f"3.Quick Attack\n    {quick_attack} damage\n    75 acurracy\n    20 critical chance\n\n"
                                                    f"4.Feint\n    {feint} damage\n    85 acurracy \n    26 critical chance\n\n"); system(CLS)

                                if my_turn == "1":
                                    hitmonchan_hp = damages("Pikachu", "Nuzlle", nuzzle, nuzzle_range, nuzzle_posibility, pikachu_critical, 
                                                            "Hitmonchan", hitmonchan_hp, HITMONCHAN_LVL_BASED_HP)
                                elif my_turn == "2":
                                    hitmonchan_hp = damages("Pikachu", "Thunder Shock", thunder_shock, thunder_shock_range, thunder_shock_posibility, pikachu_critical, 
                                                            "Hitmonchan", hitmonchan_hp, HITMONCHAN_LVL_BASED_HP)
                                elif my_turn == "3":
                                    hitmonchan_hp = damages("Pikachu", "Quick Attack", quick_attack, quick_attack_range, quick_attack_posibility, pikachu_critical, 
                                                            "Hitmonchan", hitmonchan_hp, HITMONCHAN_LVL_BASED_HP)
                                elif my_turn == "4":
                                    hitmonchan_hp = damages("Pikachu", "Feint", feint, feint_range, feint_posibility, pikachu_critical, 
                                                            "Hitmonchan", hitmonchan_hp, HITMONCHAN_LVL_BASED_HP)
                                elif my_turn == "exit":
                                    game_true = True; fighting_done = True; playing = False
                                time_battle_end(); system(CLS)

                            if playing:
                                if hitmonchan_hp > 0:
                                    turn = random.randint(1, 5)

                                    if turn == 1:
                                        pikachu_hp = damages("Hitmonchan", "Drain Punch", drain_punch, drain_punch_range, drain_punch_posibility, hitmonchan_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 2:
                                        pikachu_hp = damages("Hitmonchan", "Power-Up Punch", power_up_punch, power_up_punch_range, power_up_punch_posibility, hitmonchan_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 3:
                                        pikachu_hp = damages("Hitmonchan", "Fire Punch", fire_punch, fire_punch_range, fire_punch_posibility, hitmonchan_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 4:
                                        pikachu_hp = damages("Hitmonchan", "Mega Punch", mega_punch, mega_punch_range, mega_punch_posibility, hitmonchan_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    elif turn == 5:
                                        pikachu_hp = damages("Hitmonchan", "Focus_Punch", focus_punch, focus_punch_range, focus_punch_posibility, hitmonchan_critical, 
                                                                "Pikachu", pikachu_hp, PIKACHU_LVL_BASED_HP)
                                    time_battle_end(); system(CLS)

                            if hitmonchan_hp < 1:
                                true_2 = True
                                fighting_done = True
                                PIKACHU_LVL_BASED_HP += random.randint(10, 16)
                                pikachu_critical = ((pikachu_critical * 10) + 2)/10
                                pikachu_damage += 2
                                nuzzle = int((pikachu_damage) * 2.5)
                                thunder_shock = int((pikachu_damage) * 4.5)
                                quick_attack = int((pikachu_damage) * 4)
                                feint = int((pikachu_damage) * 3)
                                pikachu_lvl += 3
                            elif pikachu_hp < 1:
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
        pikachu_hp = PIKACHU_LVL_BASED_HP
        print(); system(CLS)
        print("Pikachu's HP Restored\n\nMove to Continue\n")
        true_1 = False
    if true_2: # Gym win
        system(CLS); print(f"Pikachu grew to LVL {pikachu_lvl - 2}!\n"
                               f"Pikachu grew to LVL {pikachu_lvl - 1}!\n"
                               f"Pikachu grew to LVL {pikachu_lvl}!\n\n"
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