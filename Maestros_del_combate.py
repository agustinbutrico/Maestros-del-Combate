import random
from time import sleep
from os import system
from readchar import readchar

system ("cls")

rock_done = False
water_done = False
electric_done = False
fighting_done = False
gym_battle_done = False
true_0 = False
true_1 = False
true_2 = False
true_3 = False
true_4 = False
true_6 = False
true_5 = False
limiter = 0
limiter_1 = 0
limiter_2 = 0
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
my_position = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
k = " "; odds = [",,,", ",,", k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k]

# Pikachu
pikachu_damage = random.randint(10, 12)
pikachu_critical = (random.randint(14, 20))/10
pikachu_base_hp = 50
pikachu_lvl = random.randint(30, 32)
pikachu_hp = pikachu_base_hp + pikachu_lvl*3 # for each lvl 3+ hp
PIKACHU_LVL_BASED_HP = pikachu_hp
pikachu = "Pikachu"; pikachu_uses = "Pikachu uses"

pikachu_nuzlle = "Nuzlle"; nuzzle = int(pikachu_damage * 2.5) # damage (25, 30)
nuzzle_range = 260 ; nuzzle_posibility = 245 # 95% acurracy    33% critical
pikachu_thunder_shock = "Thunder Shock"; thunder_shock = int(pikachu_damage * 4.5) # damage (45, 54)
thunder_shock_range = 340; thunder_shock_posibility = 220 # 65% acurracy    18% critical
pikachu_quick_attack = "Quick Attack"; quick_attack = int(pikachu_damage * 4) # damage (40, 48)
quick_attack_range = 294; quick_attack_posibility = 220 # 75% acurracy    20 critical
pikachu_feint = "Feint"; feint = int(pikachu_damage * 3) # damage (30, 34)
feint_range = 270; feint_posibility = 230 # 85% acurracy    26% critical

# Lairon
lairon_damage = random.randint(10, 12)
lairon_critical = (random.randint(11, 14))/10
lairon_base_hp = 78
lairon_lvl = random.randint(29, 32)
lairon_hp = lairon_base_hp + lairon_lvl*3 # for each lvl 3+ hp
LAIRON_LVL_BASED_HP = lairon_hp
lairon = "Lairon"; lairon_uses = "Lairon uses"

lairon_metal_claw = "Metal Claw"; metal_claw = int(lairon_damage * 5) # damage (50, 60)
metal_claw_range = 210; metal_claw_posibility = 200 # 95% acurracy    20% critical
lairon_rock_tomb = "Rock Tomb"; rock_tomb = int(lairon_damage * 6) # damage (60, 72)
rock_tomb_range = 210; rock_tomb_posibility = 200 # 95% acurracy    20% critical
lairon_headbutt = "Headbutt"; headbutt = int(lairon_damage * 7) # damage (70, 84)
headbutt_range = 200; headbutt_posibility = 200 # 100% acurracy    20% critical
lairon_rock_slide = "Rock Slide"; rock_slide = int(lairon_damage * 7.5) # damage (75, 90) 
rock_slide_range = 222; rock_slide_posibility = 200 # 90% acurracy    18% critical
lairon_iron_tail = "Iron Tail"; iron_tail = int(lairon_damage * 10) # damage (100, 120)
iron_tail_range = 268; iron_tail_posibility = 200 # 75% acurracy    15% critical

# Squirtle
squirtle_damage = random.randint(10, 12)
squirtle_critical = (random.randint(11, 15))/10
squirtle_base_hp = 68
squirtle_lvl = random.randint(26, 30)
squirtle_hp = squirtle_base_hp + squirtle_lvl*3 # for each lvl 3+ hp
SQUIRTLE_LVL_BASED_HP = squirtle_hp
squirtle = "Squirtle"; squirtle_uses = "Squirtle uses"

squirtle_tackle = "Tackle"; tackle = int(squirtle_damage * 4) # damage (40, 48)
tackle_range = 268; tackle_posibility = 200 # 75% acurracy    15% critical
squirtle_water_gun = "Water Gun"; water_gun = int(squirtle_damage * 4) # damage (40, 48)
water_gun_range = 268; water_gun_posibility = 200 # 75% acurracy    15% critical
squirtle_rapid_spin = "Rapid Spin"; rapid_spin = int(squirtle_damage * 5) # damage (50, 60)
rapid_spin_range = 310; rapid_spin_posibility = 200 # 65% acurracy    13% critical
squirtle_bite = "Bite"; bite = int(squirtle_damage * 6) # damage (60, 72)
bite_range = 365; bite_posibility = 200 # 55% acurracy    11% critical
squirtle_water_pulse = "Water Pulse"; water_pulse = int(squirtle_damage * 6) # damage (60, 72)
water_pulse_range = 336; water_pulse_posibility = 200 # 60% acurracy    12% critical

# Zapdos
zapdos_damage = random.randint(10, 12)
zapdos_critical = (random.randint(11, 12))/10
zapdos_base_hp = 60
zapdos_lvl = random.randint(32, 34)
zapdos_hp = zapdos_base_hp + zapdos_lvl*3 # for each lvl 3+ hp
ZAPDOS_LVL_BASED_HP = zapdos_hp
zapdos = "Zapdos"; zapdos_uses = "Zapdos uses"

zapdos_peck = "Peck"; peck = int(zapdos_damage * 3.5) # damage (35, 42)
peck_range = 200; peck_posibility = 200 # 100% acurracy    20% critical
zapdos_pluck = "Pluck"; pluck = int(zapdos_damage * 5) # damage (50, 60)
pluck_range = 200; pluck_posibility = 200 # 100% acurrac    20% critical
zapdos_ancient_power = "Ancient Power"; ancient_power = int(zapdos_damage * 6) # damage (60, 72)
ancient_power_range = 200; ancient_power_posibility = 200 # 100% acurracy    20% critical
zapdos_thunder = "Thunder"; thunder = int(zapdos_damage * 9) # damage (90, 108)
thunder_range = 288; thunder_posibility = 200 # 70% acurracy    14% critical
zapdos_zap_cannon = "Zap Cannon"; zap_cannon = int(zapdos_damage * 10) # damage (100, 120)
zap_cannon_range = 400; zap_cannon_posibility = 200 # 50% acurracy    10% critical

# Hitmonchan
hitmonchan_damage = random.randint(10, 12)
hitmonchan_critical = (random.randint(11, 13))/10
hitmonchan_base_hp = 48
hitmonchan_lvl = 36
hitmonchan_hp = hitmonchan_base_hp + hitmonchan_lvl*3 # for each lvl 3+ hp
HITMONCHAN_LVL_BASED_HP = hitmonchan_hp
hitmonchan = "Hitmonchan"; hitmonchan_uses = "Hitmonchan uses"

hitmonchan_drain_punch = "Drain Punch"; drain_punch = int(hitmonchan_damage * 7.5) # damage (75, 90)
drain_punch_range = 200; drain_punch_posibility = 200 # 100% acurracy    20% critical
hitmonchan_power_up_punch = "Power-Up Punch"; power_up_punch = int(hitmonchan_damage * 4) # damage (40, 48)
power_up_punch_range = 200; power_up_punch_posibility = 200 # 100% acurracy    20% critical
hitmonchan_fire_punch = "Fire Punch"; fire_punch = int(hitmonchan_damage * 7.5) # damage (75, 90)
fire_punch_range = 200; fire_punch_posibility = 200 # 100% acurracy    20% critical
hitmonchan_mega_punch = "Mega Punch"; mega_punch = int(hitmonchan_damage * 8) # damage (80, 96)
mega_punch_range = 235; mega_punch_posibility = 200 # 85% acurracy    17% critical
hitmonchan_focus_punch = "Focus_Punch"; focus_punch = int(hitmonchan_damage * 12) # damage (120, 144)
focus_punch_range = 500; focus_punch_posibility = 200 # 40% acurracy    8% critical

input1 = ("Select your attack\n"
          "1.Nuzzle\n    {} damage\n    95 acurracy\n    33 critical chance\n\n2.Thunder Shock\n    {} damage\n    65 acurracy\n    18 critical chance\n\n"
          "3.Quick Attack\n    {} damage\n    75 acurracy\n    20 critical chance\n\n4.Feint\n    {} damage\n    85 acurracy \n    26 critical chance\n\n"
          "").format(nuzzle, thunder_shock, quick_attack, feint)

def life_indicator (pokemon_hp, pokemon_LVL_BASED_HP): # Health Bar
    health_bar = int(pokemon_hp * 30 / pokemon_LVL_BASED_HP)
    health_bar_print = "[{}{}]".format("#" * health_bar, " " * (30 - health_bar))
    return health_bar_print

def battle_starts (enemy_pokemon, enemy_pokemon_hp, enemy_LVL_BASED_HP):
    print (enemy_pokemon, enemy_pokemon_hp, "HP\n", life_indicator (enemy_pokemon_hp, enemy_LVL_BASED_HP), "\n")
    print (pikachu, pikachu_hp, "HP\n", life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP), "\n")
    print ("Pikachu's Critical: [", pikachu_critical, "]\n")

def damages (pokemon_attack, attack_range, attack_posibility, pokemon_critical, pokemon_uses, pokemon_text_attack, enemy_pokemon, enemy_pokemon_hp, enemy_LVL_BASED_HP):
    print (pokemon_uses, pokemon_text_attack) # 'Pokemon uses attack'
    attack = random.randint(0, attack_range); sleep (1)
    if   attack <= 160:
        enemy_pokemon_hp -= pokemon_attack # normal damage
        print ("\n-{}".format(pokemon_attack))
    elif 160 < attack <= attack_posibility:
        enemy_pokemon_hp -= int(pokemon_attack * pokemon_critical) # special damage
        print ("\ncritical___-", int(pokemon_attack * pokemon_critical))
    elif attack_posibility < attack :
        enemy_pokemon_hp -= 0 # miss
        print ("\nmiss___")
    print ("\n", enemy_pokemon, enemy_pokemon_hp, "HP\n", life_indicator (enemy_pokemon_hp, enemy_LVL_BASED_HP))
    return enemy_pokemon_hp

def obstacles_creation (): # Obstacle Colocation
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

def time_battle_end ():
    sleep (2)

def start (): # intro
    print ("Pikachu's lvl:", pikachu_lvl, "\n"); sleep (1)
    print (pikachu, pikachu_hp, "HP\n", life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP), "\n"); sleep (1)
    print (pikachu, "know 4 movements\nNuzlle, Thunder Shock, Quick Attack and Feint\n");sleep (2)
    print ("Hospitals [H] restores HP\n"); sleep (2); system ("cls")
    print ("\nWASD to move\n"); sleep (1)

obstacles = obstacles_creation ()

while not true_0: # Locations creation
    while 0 <= limiter <= 5: 
        new_location = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
        if new_location not in locations and new_location != my_position and obstacles[new_location[POS_Y]][new_location[POS_X]] != ",":
            locations.append(new_location)
            if   limiter == 0: # Rock Gym
                rock_gym = new_location
                true_1 = True
            elif limiter == 1: # Water Gym
                water_gym = new_location
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
            true_0 = True
true_0 = False; true_1 = False; true_2 = False; true_3 = False; true_4 = False; true_5 = False; true_6 = False; limiter = 0

# Intro giving info to the player
start()

while not true_0:
    system ("cls")

    # draw map start
    print ("-"* (MAP_WIDTH* 2 + 3)) # top

    for coordinate_y in range(MAP_HEIGHT): # Map and fights
        print ("|", end="") # left side

        for coordinate_x in range(MAP_WIDTH):
            char_to_draw = "  "

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

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y: # your position
                char_to_draw = " @" # you

                if hospital_1[POS_X] == coordinate_x and hospital_1[POS_Y] == coordinate_y: # enter hospital 1
                    true_2 = True
                if hospital_2[POS_X] == coordinate_x and hospital_2[POS_Y] == coordinate_y: # enter hospital 2
                    true_2 = True

                if not rock_done:# enter the rock gym

                    if rock_gym[POS_X] == coordinate_x and rock_gym[POS_Y] == coordinate_y:
                        print (); system ("cls"); print ("You entered -Pewter Rock Gym-\n")

                        while not rock_done: # rock gym fight

                            if pikachu_hp > 0 :
                                battle_starts (lairon, lairon_hp, LAIRON_LVL_BASED_HP); my_turn = None
                                while my_turn != "1" and my_turn != "2" and my_turn != "3" and my_turn != "4" :
                                    my_turn = input(input1); system ("cls")

                                if   my_turn == "1" :
                                    lairon_hp = damages (nuzzle, nuzzle_range, nuzzle_posibility, pikachu_critical, pikachu_uses, pikachu_nuzlle, lairon, lairon_hp, LAIRON_LVL_BASED_HP)
                                elif my_turn == "2" :
                                    lairon_hp = damages (thunder_shock, thunder_shock_range, thunder_shock_posibility, pikachu_critical, pikachu_uses, pikachu_thunder_shock, lairon, lairon_hp, LAIRON_LVL_BASED_HP)
                                elif my_turn == "3" :
                                    lairon_hp = damages (quick_attack, quick_attack_range, quick_attack_posibility, pikachu_critical, pikachu_uses, pikachu_quick_attack, lairon, lairon_hp, LAIRON_LVL_BASED_HP)
                                elif my_turn == "4" :
                                    lairon_hp = damages (feint, feint_range, feint_posibility, pikachu_critical, pikachu_uses, pikachu_feint, lairon, lairon_hp, LAIRON_LVL_BASED_HP)
                                time_battle_end (); system ("cls")

                            if lairon_hp > 0 :
                                turn = random.randint(1, 5)

                                if   turn == 1 :
                                    pikachu_hp = damages (metal_claw, metal_claw_range, metal_claw_posibility, lairon_critical, lairon_uses, lairon_metal_claw, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 2 :
                                    pikachu_hp = damages (rock_tomb, rock_tomb_range, rock_tomb_posibility, lairon_critical, lairon_uses, lairon_rock_tomb, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 3 :
                                    pikachu_hp = damages (headbutt, headbutt_range, headbutt_posibility, lairon_critical, lairon_uses, lairon_headbutt, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 4 :
                                    pikachu_hp = damages (rock_slide, rock_slide_range, rock_slide_posibility, lairon_critical, lairon_uses, lairon_rock_slide, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 5 :
                                    pikachu_hp = damages (iron_tail, iron_tail_range, iron_tail_posibility, lairon_critical, lairon_uses, lairon_iron_tail, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                time_battle_end (); system ("cls")

                            if   lairon_hp < 1:
                                true_1 = True
                                rock_done = True
                            elif pikachu_hp < 1:
                                true_3 = True
                                rock_done = True

                        pikachu_lvl += random.randint(1, 2)
                        pikachu_critical += 0.1

                if not water_done: # enter the water gym

                    if water_gym[POS_X] == coordinate_x and water_gym[POS_Y] == coordinate_y:
                        print (); system ("cls"); print ("You entered -Cerulean Water Gym-\n")

                        while not water_done: # water gym fight

                            if pikachu_hp > 0 :
                                battle_starts (squirtle, squirtle_hp, SQUIRTLE_LVL_BASED_HP); my_turn = None
                                while my_turn != "1" and my_turn != "2" and my_turn != "3" and my_turn != "4" :
                                    my_turn = input(input1); system ("cls")

                                if   my_turn == "1" :
                                    squirtle_hp = damages (nuzzle, nuzzle_range, nuzzle_posibility, pikachu_critical, pikachu_uses, pikachu_nuzlle, squirtle, squirtle_hp, SQUIRTLE_LVL_BASED_HP)
                                elif my_turn == "2" :
                                    squirtle_hp = damages (thunder_shock, thunder_shock_range, thunder_shock_posibility, pikachu_critical, pikachu_uses, pikachu_thunder_shock, squirtle, squirtle_hp, SQUIRTLE_LVL_BASED_HP)
                                elif my_turn == "3" :
                                    squirtle_hp = damages (quick_attack, quick_attack_range, quick_attack_posibility, pikachu_critical, pikachu_uses, pikachu_quick_attack, squirtle, squirtle_hp, SQUIRTLE_LVL_BASED_HP)
                                elif my_turn == "4" :
                                    squirtle_hp = damages (feint, feint_range, feint_posibility, pikachu_critical, pikachu_uses, pikachu_feint, squirtle, squirtle_hp, SQUIRTLE_LVL_BASED_HP)
                                time_battle_end (); system ("cls")

                            if squirtle_hp > 0 :
                                turn = random.randint(1, 5)

                                if   turn == 1 :
                                    pikachu_hp = damages (tackle, tackle_range, tackle_posibility, squirtle_critical, squirtle_uses, squirtle_tackle, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 2 :
                                    pikachu_hp = damages (water_gun, water_gun_range, water_gun_posibility, squirtle_critical, squirtle_uses, squirtle_water_gun, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 3 :
                                    pikachu_hp = damages (rapid_spin, rapid_spin_range, rapid_spin_posibility, squirtle_critical, squirtle_uses, squirtle_rapid_spin, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 4 :
                                    pikachu_hp = damages (bite, bite_range, bite_posibility, squirtle_critical, squirtle_uses, squirtle_bite, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 5 :
                                    pikachu_hp = damages (water_pulse, water_pulse_range, water_pulse_posibility, squirtle_critical, squirtle_uses, squirtle_water_pulse, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                time_battle_end (); system ("cls")

                            if   squirtle_hp < 1:
                                true_1 = True
                                water_done = True
                            elif pikachu_hp < 1:
                                true_3 = True
                                water_done = True

                        pikachu_lvl += random.randint(1, 2)
                        pikachu_critical += 0.1

                if not electric_done: # enter the electric gym

                    if electric_gym[POS_X] == coordinate_x and electric_gym[POS_Y] == coordinate_y:
                        print (); system ("cls"); print ("You entered -Vermilion Electric Gym-\n")

                        while not electric_done: # electric gym fight

                            if pikachu_hp > 0 :
                                battle_starts (zapdos, zapdos_hp, ZAPDOS_LVL_BASED_HP); my_turn = None
                                while my_turn != "1" and my_turn != "2" and my_turn != "3" and my_turn != "4" :
                                    my_turn = input(input1); system ("cls")

                                if   my_turn == "1" :
                                    zapdos_hp = damages (nuzzle, nuzzle_range, nuzzle_posibility, pikachu_critical, pikachu_uses, pikachu_nuzlle, zapdos, zapdos_hp, ZAPDOS_LVL_BASED_HP)
                                elif my_turn == "2" :
                                    zapdos_hp = damages (thunder_shock, thunder_shock_range, thunder_shock_posibility, pikachu_critical, pikachu_uses, pikachu_thunder_shock, zapdos, zapdos_hp, ZAPDOS_LVL_BASED_HP)
                                elif my_turn == "3" :
                                    zapdos_hp = damages (quick_attack, quick_attack_range, quick_attack_posibility, pikachu_critical, pikachu_uses, pikachu_quick_attack, zapdos, zapdos_hp, ZAPDOS_LVL_BASED_HP)
                                elif my_turn == "4" :
                                    zapdos_hp = damages (feint, feint_range, feint_posibility, pikachu_critical, pikachu_uses, pikachu_feint, zapdos, zapdos_hp, ZAPDOS_LVL_BASED_HP)
                                time_battle_end (); system ("cls")

                            if zapdos_hp > 0 :
                                turn = random.randint(1, 5)

                                if   turn == 1 :
                                    pikachu_hp = damages (peck, peck_range, peck_posibility, zapdos_critical, zapdos_uses, zapdos_peck, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 2 :
                                    pikachu_hp = damages (pluck, pluck_range, pluck_posibility, zapdos_critical, zapdos_uses, zapdos_pluck, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 3 :
                                    pikachu_hp = damages (ancient_power, ancient_power_range, ancient_power_posibility, zapdos_critical, zapdos_uses, zapdos_ancient_power, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 4 :
                                    pikachu_hp = damages (thunder, thunder_range, thunder_posibility, zapdos_critical, zapdos_uses, zapdos_thunder, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 5 :
                                    pikachu_hp = damages (zap_cannon, zap_cannon_range, zap_cannon_posibility, zapdos_critical, zapdos_uses, zapdos_zap_cannon, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                time_battle_end (); system ("cls")

                            if   zapdos_hp < 1:
                                true_1 = True
                                electric_done = True
                            elif pikachu_hp < 1:
                                true_3 = True
                                electric_done = True

                        pikachu_lvl += random.randint(1, 3)
                        pikachu_critical += 0.1

                if not fighting_done: # enter the fighting

                    if fighting_gym[POS_X] == coordinate_x and fighting_gym[POS_Y] == coordinate_y:
                        print (); system ("cls"); print ("You entered -Cianwood Fighting Gym\n")

                        while not fighting_done: # fighting gym fight

                            if pikachu_hp > 0 :
                                battle_starts (hitmonchan, hitmonchan_hp, HITMONCHAN_LVL_BASED_HP); my_turn = None
                                while my_turn != "1" and my_turn != "2" and my_turn != "3" and my_turn != "4" :
                                    my_turn = input(input1); system ("cls")

                                if   my_turn == "1" :
                                    hitmonchan_hp = damages (nuzzle, nuzzle_range, nuzzle_posibility, pikachu_critical, pikachu_uses, pikachu_nuzlle, hitmonchan, hitmonchan_hp, HITMONCHAN_LVL_BASED_HP)
                                elif my_turn == "2" :
                                    hitmonchan_hp = damages (thunder_shock, thunder_shock_range, thunder_shock_posibility, pikachu_critical, pikachu_uses, pikachu_thunder_shock, hitmonchan, hitmonchan_hp, HITMONCHAN_LVL_BASED_HP)
                                elif my_turn == "3" :
                                    hitmonchan_hp = damages (quick_attack, quick_attack_range, quick_attack_posibility, pikachu_critical, pikachu_uses, pikachu_quick_attack, hitmonchan, hitmonchan_hp, HITMONCHAN_LVL_BASED_HP)
                                elif my_turn == "4" :
                                    hitmonchan_hp = damages (feint, feint_range, feint_posibility, pikachu_critical, pikachu_uses, pikachu_feint, hitmonchan, hitmonchan_hp, HITMONCHAN_LVL_BASED_HP)
                                time_battle_end (); system ("cls")

                            if hitmonchan_hp > 0 :
                                turn = random.randint(1, 5)

                                if   turn == 1 :
                                    pikachu_hp = damages (drain_punch, drain_punch_range, drain_punch_posibility, hitmonchan_critical, hitmonchan_uses, hitmonchan_drain_punch, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 2 :
                                    pikachu_hp = damages (power_up_punch, power_up_punch_range, power_up_punch_posibility, hitmonchan_critical, hitmonchan_uses, hitmonchan_power_up_punch, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 3 :
                                    pikachu_hp = damages (fire_punch, fire_punch_range, fire_punch_posibility, hitmonchan_critical, hitmonchan_uses, hitmonchan_fire_punch, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 4 :
                                    pikachu_hp = damages (mega_punch, mega_punch_range, mega_punch_posibility, hitmonchan_critical, hitmonchan_uses, hitmonchan_mega_punch, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                elif turn == 5 :
                                    pikachu_hp = damages (focus_punch, focus_punch_range, focus_punch_posibility, hitmonchan_critical, hitmonchan_uses, hitmonchan_focus_punch, pikachu, pikachu_hp, PIKACHU_LVL_BASED_HP)
                                time_battle_end (); system ("cls")

                            if   hitmonchan_hp < 1:
                                true_1 = True
                                fighting_done = True
                            elif pikachu_hp < 1:
                                true_3 = True
                                fighting_done = True

                        pikachu_lvl += random.randint(2, 3)
                        pikachu_critical += 0.1

            if obstacles[coordinate_y][coordinate_x] == ",": # walls
                if obstacles[my_position[POS_Y]][my_position[POS_X]] == ",": # don't draw walls on you
                    obstacles[my_position[POS_Y]][my_position[POS_X]] = " "
                if obstacles[my_position[POS_Y]][my_position[POS_X]] != ",": # walls print
                    char_to_draw = " #"

            print ("{}".format(char_to_draw), end="") # printer
        print (" |") # right side

    print ("-"* (MAP_WIDTH* 2 + 3)) # bottom
    # draw map finish

    if true_1: # Gym win
        system ("cls"); print ("\nGym Cleared\nMove to Continue")
        true_1 = False
    if true_2: # pikachu restoration
        pikachu_hp = PIKACHU_LVL_BASED_HP
        print (); system ("cls"); print ("Pikachu's HP Restored\nMove to Continue")
        true_2 = False
    if true_3: # Gym lost
        system ("cls"); print ("\nGym Fight Losed\n\nYou Lose\n")
        true_0 = True
    if rock_done and water_done and electric_done and fighting_done: # win conditions
        system ("cls"); print ("You win all battles, congratulations!")
        true_0 = True

    direction = readchar() # where he/she want to move
    new_position = None

    if   direction == "w": # up movement
        new_position = [my_position[POS_X], my_position[POS_Y] - 1]
        if new_position[POS_Y] < 0:
            new_position[POS_Y] = MAP_HEIGHT - 1
    elif direction == "s": # down movement
        new_position = [my_position[POS_X], my_position[POS_Y] + 1]
        if new_position[POS_Y] > MAP_HEIGHT - 1:
            new_position[POS_Y] = 0
    elif direction == "a": # left movement
        new_position = [my_position[POS_X] - 1, my_position[POS_Y]]
        if new_position[POS_X] < 0:
            new_position[POS_X] = MAP_WIDTH - 1
    elif direction == "d": # right movement
        new_position = [my_position[POS_X] + 1, my_position[POS_Y]]
        if new_position[POS_X] > MAP_WIDTH - 1:
            new_position[POS_X] = 0

    if new_position: # in-game movement
        if obstacles[new_position[POS_Y]][new_position[POS_X]] != ",":
            my_position = new_position