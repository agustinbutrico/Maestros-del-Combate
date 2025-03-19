import random
from time import sleep
from os import system
from readchar import readchar

rock_done = False
water_done = False
electric_done = False
fighting_done = False
true_start = False
limiter = 0
limiter_1 = 0
limiter_2 = 0
true_0 = False
true_1 = False
true_2 = False
true_3 = False
true_4 = False
true_5 = False
true_6 = False
rock_gym = None
water_gym = None
electric_gym = None
fighting_gym = None
hospital_1 = None
hospital_2 = None
locations = []

def pikachu_life_indicator (pikachu_hp_life_indicator, PIKACHU_LVL_BASED_HP_life_indicator):
    pikachu_health_bar = int(pikachu_hp_life_indicator * 30 / PIKACHU_LVL_BASED_HP_life_indicator)
    pikachu_health_bar_print = "[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar))
    return pikachu_health_bar_print
def squirtle_life_indicator (squirtle_hp_life_indicator):
    squirtle_health_bar = int(squirtle_hp_life_indicator * 30 / SQUIRTLE_LVL_BASED_HP)
    squirtle_health_bar_print = "[{}{}]".format("#" * squirtle_health_bar, " " * (30 - squirtle_health_bar))
    return squirtle_health_bar_print
def lairon_life_indicator (lairon_hp_life_indicator):
    lairon_health_bar = int(lairon_hp_life_indicator * 30 / LAIRON_LVL_BASED_HP)
    lairon_health_bar_print = "[{}{}]".format("#" * lairon_health_bar, " " * (30 - lairon_health_bar))
    return lairon_health_bar_print
def zapdos_life_indicator (zapdos_hp_life_indicator):
    zapdos_health_bar = int(zapdos_hp_life_indicator * 30 / ZAPDOS_LVL_BASED_HP)
    zapdos_health_bar_print = "[{}{}]".format("#" * zapdos_health_bar, " " * (30 - zapdos_health_bar))
    return zapdos_health_bar_print
def hitmonchan_life_indicator (hitmonchan_hp_life_indicator):
    hitmonchan_health_bar = int(hitmonchan_hp_life_indicator * 30 / HITMOCHAN_LVL_BASED_HP)
    hitmonchan_health_bar_print = "[{}{}]".format("#" * hitmonchan_health_bar, " " * (30 - hitmonchan_health_bar))
    return hitmonchan_health_bar_print

## pokemon
p = "Pikachu"; pu = "Pikachu uses"
pikachu_damage = random.randint(10, 12)
pikachu_base_hp = 50
pikachu_critical = (random.randint(14, 20))/10
pikachu_lvl = random.randint(30, 32)
PIKACHU_LVL_BASED_HP = pikachu_base_hp + pikachu_lvl*3 # for each lvl 3+ hp
pikachu_hp = PIKACHU_LVL_BASED_HP
s = "Squirtle"; su = "Squirtle uses"
squirtle_damage = random.randint(10, 12)
squirtle_base_hp = 68
squirtle_critical = (random.randint(11, 15))/10
squirtle_lvl = random.randint(26, 30)
SQUIRTLE_LVL_BASED_HP = squirtle_base_hp + squirtle_lvl*3 # for each lvl 3+ hp
squirtle_hp = SQUIRTLE_LVL_BASED_HP
l = "Lairon"; lu = "Lairon uses"
lairon_damage = random.randint(10, 12)
lairon_base_hp = 78
lairon_critical = (random.randint(11, 14))/10
lairon_lvl = random.randint(29, 32)
LAIRON_LVL_BASED_HP = lairon_base_hp + lairon_lvl*3 # for each lvl 3+ hp
lairon_hp = LAIRON_LVL_BASED_HP
z = "Zapdos"; zu = "Zapdos uses"
zapdos_damage = random.randint(10, 12)
zapdos_base_hp = 60
zapdos_critical = (random.randint(11, 12))/10
zapdos_lvl = random.randint(32, 34)
ZAPDOS_LVL_BASED_HP = zapdos_base_hp + zapdos_lvl*3 # for each lvl 3+ hp
zapdos_hp = ZAPDOS_LVL_BASED_HP
h = "Hitmonchan"; hu = "Hitmonchan uses"
hitmonchan_damage = random.randint(10, 12)
hitmonchan_base_hp = 48
hitmonchan_critical = (random.randint(11, 13))/10
hitmonchan_lvl = 36
HITMOCHAN_LVL_BASED_HP = hitmonchan_base_hp + hitmonchan_lvl*3 # for each lvl 3+ hp
hitmonchan_hp = HITMOCHAN_LVL_BASED_HP
# Pikachu Attacks    # forward you will find a chance, the odds range from 200 to "x", value of 200 for 100% acurracy of the attack.
p_n = "Nuzlle"; nuzzle = int(pikachu_damage * 2); nuzzle_odd = 210 # 95% acurracy
p_ts = "Thunder Shock"; thunder_shock = int(pikachu_damage * 4.5); thunder_shock_odd = 340 # 65% acurracy, this one has extra odds for critical
p_qa = "Quick Attack"; quick_attack = int(pikachu_damage * 4); quick_attack_odd = 270 # 75% acurracy
p_f = "Feint"; feint = int(pikachu_damage * 3); feint_odd = 240 # 85% acurracy
# Squirtle Attacks
s_t = "Tackle"; tackle = int(squirtle_damage * 4); tackle_odd = 270 # 75% acurracy
s_wg = "Water Gun"; water_gun = int(squirtle_damage * 4); water_gun_odd = 270 # 75% acurracy
s_rs = "Rapid Spin"; rapid_spin = int(squirtle_damage * 5); rapid_spin_odd = 312 # 65% acurracy
s_b = "Bite"; bite = int(squirtle_damage * 6); bite_odd = 365 # 55% acurracy
s_wp = "Water Pulse"; water_pulse = int(squirtle_damage * 6); water_pulse_odd = 338 # 60% acurracy
# Lairon Attacks
l_mc = "Metal Claw"; metal_claw = int(lairon_damage * 5); metal_claw_odd = 210 # 95% acurracy
l_rt = "Rock Tomb"; rock_tomb = int(lairon_damage * 6); rock_tomb_odd = 210 # 95% acurracy
l_hb = "Headbutt"; headbutt = int(lairon_damage * 7); headbutt_odd = 200 # 100% acurracy
l_rs = "Rock Slide"; rock_slide = int(lairon_damage * 7.5); rock_slide_odd = 224 # 90% acurracy
l_it = "Iron Tail"; iron_tail = int(lairon_damage * 10); iron_tail_odd = 270 # 75% acurracy
# Zapdos Attacks
z_pe = "Peck"; peck = int(zapdos_damage * 3.5); peck_odd = 200 # 100% acurracy
z_pl = "Pluck"; pluck = int(zapdos_damage * 5); pluck_odd = 200 # 100% acurrac
z_ap = "Ancient Power"; ancient_power = int(zapdos_damage * 6); ancient_power_odd = 200 # 100% acurracy
z_t = "Thunder"; thunder = int(zapdos_damage * 9); thunder_odd = 290 # 70% acurracy
z_zc = "Zap Cannon"; zap_cannon = int(zapdos_damage * 10); zap_cannon_odd = 400 # 50% acurracy
# Hitmonchan Attacks
h_dp = "Drain Punch"; drain_punch = int(hitmonchan_damage * 7.5); drain_punch_odd = 200 # 100% acurracy
h_php = "Power-Up Punch"; power_up_punch = int(hitmonchan_damage * 4); power_up_punch_odd = 200 # 100% acurracy
h_fip = "Fire Punch"; fire_punch = int(hitmonchan_damage * 7.5); fire_punch_odd = 100 # 100% acurracy
h_mp = "Mega Punch"; mega_punch = int(hitmonchan_damage * 8); mega_punch_odd = 235 # 85% acurracy
h_fop = "Focus_Punch"; focus_punch = int(hitmonchan_damage * 12); focus_punch_odd = 500 # 40% acurracy
input1 = ("Select your attack\n1.Nuzzle ({} damage)\n    95 acurracy\n2.Thunder Shock ({} damage)\n  "
         "  65 acurracy\n3.Quick Attack ({} damage)\n    75 acurracy\n4.Feint ({} damage)\n    85 acurracy\n").format(nuzzle, thunder_shock, quick_attack, feint)
## snake
MAP_WIDTH = 20
MAP_HEIGHT = random.randint(MAP_WIDTH -5, MAP_WIDTH +10)
POS_X = 0 # pos 1* of list
POS_Y = 1 # pos 2* of list
my_position = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
obstacle_colocation = ""
k = " "; odds = [",,,", ",,", k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k]

while limiter_1 < MAP_HEIGHT: # random map generator
    while limiter_2 < MAP_WIDTH:
        limiter = random.choice(odds)
        if limiter == " ":
            limiter_2 += 1
        elif limiter == ",,":
            limiter_2 += 2
        elif limiter == ",,,":
            limiter_2 += 3
        obstacle_colocation += limiter
    obstacle_colocation += "."
    limiter_1 += 1
    limiter_2 = 0
obstacle_colocation = [list(row) for row in obstacle_colocation.split(".")]
limiter = 0; limiter_1 = 0; limiter_2 = 0

while not true_0: # rock gym position
    while 0 <= limiter < 4: 
        new_gym = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
        if new_gym not in locations and new_gym != my_position and obstacle_colocation[new_gym[POS_Y]][new_gym[POS_X]] != ",":
            locations.append(new_gym)
            if   limiter == 0:
                rock_gym = new_gym
                true_1 = True
            elif limiter == 1:
                water_gym = new_gym
                true_2 = True
            elif limiter == 2:
                electric_gym = new_gym
                true_3 = True
            elif limiter == 3:
                fighting_gym = new_gym
                true_4 = True
            limiter += 1
        if true_1 and true_2 and true_3 and true_4:
            true_0 = True
limiter = 0; true_0 = False; true_1 = False; true_2 = False; true_3 = False; true_4 = False

while limiter != 2: # hospital position
    new_hospital = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
    if new_hospital not in  locations and new_hospital != my_position and obstacle_colocation[new_hospital[POS_Y]][new_hospital[POS_X]] != ",":
        locations.append(new_hospital)
        if limiter == 0:
            hospital_1 = new_hospital
        if limiter == 1:
            hospital_2 = new_hospital
        limiter += 1
limiter = 0

# Intro giving info to the player
system("cls"); print("Pikachu's lvl:", pikachu_lvl, "\n"); sleep(1); print(p, pikachu_hp, "HP\n", pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP), "\n"); sleep(1)
print(p, "know 4 movements\nNuzlle, Thunder Shock, Quick Attack and Feint\n");sleep(3); print("Hospitals [H] restores HP"); sleep(2); system("cls")

# game starts
system("cls"); print("\nWASD to move"); sleep(1)

while not true_0:
    system("cls")
    # draw map start
    print("-"* (MAP_WIDTH* 2 + 3)) # top

    for coordinate_y in range(MAP_HEIGHT): # Map and fights
        print("|", end="") # left side

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

            if obstacle_colocation[coordinate_y][coordinate_x] == ",": # walls
                if obstacle_colocation[my_position[POS_Y]][my_position[POS_X]] != ",": # walls print
                    char_to_draw = " #"

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y: # your position
                char_to_draw = " @" # you

                if hospital_1[POS_X] == coordinate_x and hospital_1[POS_Y] == coordinate_y: # enter hospital 1
                    true_6 = True
                if hospital_2[POS_X] == coordinate_x and hospital_2[POS_Y] == coordinate_y: # enter hospital 2
                    true_6 = True

                if not true_start:# enter the rock gym
                    if rock_gym[POS_X] == coordinate_x and rock_gym[POS_Y] == coordinate_y:
                        print(); system("cls"); print("You entered -Pewter Rock Gym-\n")

                        while not rock_done: # rock gym fight
                            if pikachu_hp > 0 :
                                print(l, lairon_hp, "HP")
                                lairon_life_indicator (lairon_hp)
                                print("\nPikachu's Critical: [", pikachu_critical, "]\n")
                                pikachus_turn = None
                                while pikachus_turn != "1" and pikachus_turn != "2" and pikachus_turn != "3" and pikachus_turn != "4" :
                                    pikachus_turn = input(input1)
                                system("cls")

                                if pikachus_turn == "1" :
                                    print(pu, p_n)
                                    critical_odds = random.randint(1, nuzzle_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        lairon_hp -= nuzzle
                                        print("\n-{}".format(nuzzle))
                                    elif 160 <= critical_odds <= 200:
                                        lairon_hp -= int(nuzzle * pikachu_critical)
                                        print("\ncritical___-", int(nuzzle * pikachu_critical))
                                    elif 200 < critical_odds <= nuzzle_odd:
                                        lairon_hp -= 0
                                        print("\nmiss___")
                                    print("\n", l, lairon_hp, "HP")
                                    lairon_life_indicator (lairon_hp)

                                elif pikachus_turn == "2" :
                                    print(pu, p_ts)
                                    critical_odds = random.randint(1, thunder_shock_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        lairon_hp -= thunder_shock
                                        print("\n-{}".format(thunder_shock))
                                    elif 160 <= critical_odds <= 220:
                                        lairon_hp -= int(thunder_shock * pikachu_critical)
                                        print("\ncritical___-", int(thunder_shock * pikachu_critical))
                                    elif 220 < critical_odds <= thunder_shock_odd:
                                        lairon_hp -= 0
                                        print("\nmiss___")
                                    print("\n", l, lairon_hp, "HP")
                                    lairon_life_indicator (lairon_hp)

                                elif pikachus_turn == "3" :
                                    print(pu, p_qa)
                                    critical_odds = random.randint(1, quick_attack_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        lairon_hp -= quick_attack
                                        print("\n-{}".format(quick_attack))
                                    elif 160 <= critical_odds <= 200:
                                        lairon_hp -= int(quick_attack * pikachu_critical)
                                        print("\ncritical___-", int(quick_attack * pikachu_critical))
                                    elif 200 < critical_odds <= quick_attack_odd:
                                        lairon_hp -= 0
                                        print("\nmiss___")
                                    print("\n", l, lairon_hp, "HP")
                                    lairon_life_indicator (lairon_hp)
                                
                                elif pikachus_turn == "4" :
                                    print(pu, p_f)
                                    critical_odds = random.randint(1, feint_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        lairon_hp -= feint
                                        print("\n-{}".format(feint))
                                    elif 160 <= critical_odds <= 200:
                                        lairon_hp -= int(feint * pikachu_critical)
                                        print("\ncritical___-", int(feint * pikachu_critical))
                                    elif 200 < critical_odds <= feint_odd:
                                        lairon_hp -= 0
                                        print("\nmiss___")
                                    print("\n", l, lairon_hp, "HP")
                                    lairon_life_indicator (lairon_hp)
                            sleep(3)
                            system("cls")

                            if lairon_hp > 0 :
                                lairon_turn = random.randint(1, 5)

                                if lairon_turn == 1 :
                                    print(lu, l_mc)
                                    critical_odds = random.randint(1, metal_claw_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= metal_claw
                                        print("\n-{}".format(metal_claw))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(metal_claw * lairon_critical)
                                        print("\ncritical___-", int (metal_claw * lairon_critical))
                                    elif 200 < critical_odds <= metal_claw_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif lairon_turn == 2 :
                                    print(lu, l_rt)
                                    critical_odds = random.randint(1, rock_tomb_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= rock_tomb
                                        print("\n-{}".format(rock_tomb))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(rock_tomb * lairon_critical)
                                        print("\ncritical___-", int (rock_tomb * lairon_critical))
                                    elif 200 < critical_odds <= rock_tomb_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif lairon_turn == 3 :
                                    print(lu, l_hb)
                                    critical_odds = random.randint(1, headbutt_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= headbutt
                                        print("\n-{}".format(headbutt))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(headbutt * lairon_critical)
                                        print("\ncritical___-", int (headbutt * lairon_critical))
                                    elif 200 < critical_odds <= headbutt_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif lairon_turn == 4 :
                                    print(lu, l_rs)
                                    critical_odds = random.randint(1, rock_slide_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= rock_slide
                                        print("\n-{}".format(rock_slide))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(rock_slide * lairon_critical)
                                        print("\ncritical___-", int (rock_slide * lairon_critical))
                                    elif 200 < critical_odds <= rock_slide_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif lairon_turn == 5 :
                                    print(lu, l_it)
                                    critical_odds = random.randint(1, iron_tail_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= iron_tail
                                        print("\n-{}".format(iron_tail))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(iron_tail * lairon_critical)
                                        print("\ncritical___-", int (iron_tail * lairon_critical))
                                    elif 200 < critical_odds <= iron_tail_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))
                            sleep(3); system("cls")

                            if lairon_hp < 1:
                                rock_done = True
                                true_1 = True
                            elif pikachu_hp < 1:
                                rock_done = True
                                true_5 = True

                        pikachu_lvl += random.randint(1, 2)
                        pikachu_critical += 0.1
                        true_6 = False

                if not true_start: # enter the water gym
                    if water_gym[POS_X] == coordinate_x and water_gym[POS_Y] == coordinate_y:
                        print(); system("cls"); print("You entered -Cerulean Water Gym-\n")

                        while not water_done: # water gym fight
                            if pikachu_hp > 0 :
                                print(s, squirtle_hp, "HP")
                                squirtle_life_indicator (squirtle_hp)
                                print("\nPikachu's Critical: [", pikachu_critical, "]\n")
                                pikachus_turn = None
                                while pikachus_turn != "1" and pikachus_turn != "2" and pikachus_turn != "3" and pikachus_turn != "4" :
                                    pikachus_turn = input(input1)
                                system("cls")

                                if pikachus_turn == "1" :
                                    print(pu, p_n)
                                    critical_odds = random.randint(1, nuzzle_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        squirtle_hp -= nuzzle
                                        print("\n-{}".format(nuzzle))
                                    elif 160 <= critical_odds <= 200:
                                        squirtle_hp -= int(nuzzle * pikachu_critical)
                                        print("\ncritical___-", int(nuzzle * pikachu_critical))
                                    elif 200 < critical_odds <= nuzzle_odd:
                                        squirtle_hp -= 0
                                        print("\nmiss___")
                                    print("\n", s, squirtle_hp, "HP")
                                    squirtle_life_indicator (squirtle_hp)

                                elif pikachus_turn == "2" :
                                    print(pu, p_ts)
                                    critical_odds = random.randint(1, thunder_shock_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        squirtle_hp -= thunder_shock
                                        print("\n-{}".format(thunder_shock))
                                    elif 160 <= critical_odds <= 220:
                                        squirtle_hp -= int(thunder_shock * pikachu_critical)
                                        print("\ncritical___-", int(thunder_shock * pikachu_critical))
                                    elif 220 < critical_odds <= thunder_shock_odd:
                                        squirtle_hp -= 0
                                        print("\nmiss___")
                                    print("\n", s, squirtle_hp, "HP")
                                    squirtle_life_indicator (squirtle_hp)

                                elif pikachus_turn == "3" :
                                    print(pu, p_qa)
                                    critical_odds = random.randint(1, quick_attack_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        squirtle_hp -= quick_attack
                                        print("\n-{}".format(quick_attack))
                                    elif 160 <= critical_odds <= 200:
                                        squirtle_hp -= int(quick_attack * pikachu_critical)
                                        print("\ncritical___-", int(quick_attack * pikachu_critical))
                                    elif 200 < critical_odds <= quick_attack_odd:
                                        squirtle_hp -= 0
                                        print("\nmiss___")
                                    print("\n", s, squirtle_hp, "HP")
                                    squirtle_life_indicator (squirtle_hp)
                                
                                elif pikachus_turn == "4" :
                                    print(pu, p_f)
                                    critical_odds = random.randint(1, feint_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        squirtle_hp -= feint
                                        print("\n-{}".format(feint))
                                    elif 160 <= critical_odds <= 200:
                                        squirtle_hp -= int(feint * pikachu_critical)
                                        print("\ncritical___-", int(feint * pikachu_critical))
                                    elif 200 < critical_odds <= feint_odd:
                                        squirtle_hp -= 0
                                        print("\nmiss___")
                                    print("\n", s, squirtle_hp, "HP")
                                    squirtle_life_indicator (squirtle_hp)
                            sleep(3)
                            system("cls")

                            if squirtle_hp > 0 :
                                squirtle_turn = random.randint(1, 5)

                                if squirtle_turn == 1 :
                                    print(su, s_t)
                                    critical_odds = random.randint(1, tackle_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= tackle
                                        print("\n-{}".format(tackle))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(tackle * squirtle_critical)
                                        print("\ncritical___-", int (tackle * squirtle_critical))
                                    elif 200 < critical_odds <= tackle_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif squirtle_turn == 2 :
                                    print(su, s_wg)
                                    critical_odds = random.randint(1, water_gun_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= water_gun
                                        print("\n-{}".format(water_gun))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(water_gun * squirtle_critical)
                                        print("\ncritical___-", int (water_gun * squirtle_critical))
                                    elif 200 < critical_odds <= water_gun_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif squirtle_turn == 3 :
                                    print(su, s_rs)
                                    critical_odds = random.randint(1, rapid_spin_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= rapid_spin
                                        print("\n-{}".format(rapid_spin))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(rapid_spin * squirtle_critical)
                                        print("\ncritical___-", int (rapid_spin * squirtle_critical))
                                    elif 200 < critical_odds <= rapid_spin_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif squirtle_turn == 4 :
                                    print(su, s_b)
                                    critical_odds = random.randint(1, bite_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= bite
                                        print("\n-{}".format(bite))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(bite * squirtle_critical)
                                        print("\ncritical___-", int (bite * squirtle_critical))
                                    elif 200 < critical_odds <= bite_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif squirtle_turn == 5 :
                                    print(su, s_wp)
                                    critical_odds = random.randint(1, water_pulse_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= water_pulse
                                        print("\n-{}".format(water_pulse))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(water_pulse * squirtle_critical)
                                        print("\ncritical___-", int (water_pulse * squirtle_critical))
                                    elif 200 < critical_odds <= water_pulse_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))
                            sleep(3); system("cls")

                            if squirtle_hp < 1:
                                water_done = True
                                true_2 = True
                            elif pikachu_hp < 1:
                                water_done = True
                                true_5 = True

                        pikachu_lvl += random.randint(1, 2)
                        pikachu_critical += 0.1
                        true_start = False

                if not true_start: # enter the electric gym
                    if electric_gym[POS_X] == coordinate_x and electric_gym[POS_Y] == coordinate_y:
                        print(); system("cls"); print("You entered -Vermilion Electric Gym-\n")

                        while not electric_done: # electric gym fight
                            if pikachu_hp > 0 :
                                print(z, zapdos_hp, "HP")
                                zapdos_life_indicator (zapdos_hp)
                                print("\nPikachu's Critical: [", pikachu_critical, "]\n")
                                pikachus_turn = None
                                while pikachus_turn != "1" and pikachus_turn != "2" and pikachus_turn != "3" and pikachus_turn != "4" :
                                    pikachus_turn = input(input1)
                                system("cls")

                                if pikachus_turn == "1" :
                                    print(pu, p_n)
                                    critical_odds = random.randint(1, nuzzle_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        zapdos_hp -= nuzzle
                                        print("\n-{}".format(nuzzle))
                                    elif 160 <= critical_odds <= 200:
                                        zapdos_hp -= int(nuzzle * pikachu_critical)
                                        print("\ncritical___-", int(nuzzle * pikachu_critical))
                                    elif 200 < critical_odds <= nuzzle_odd:
                                        zapdos_hp -= 0
                                        print("\nmiss___")
                                    print("\n", z, zapdos_hp, "HP")
                                    zapdos_life_indicator (zapdos_hp)

                                elif pikachus_turn == "2" :
                                    print(pu, p_ts)
                                    critical_odds = random.randint(1, thunder_shock_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        zapdos_hp -= thunder_shock
                                        print("\n-{}".format(thunder_shock))
                                    elif 160 <= critical_odds <= 220:
                                        zapdos_hp -= int(thunder_shock * pikachu_critical)
                                        print("\ncritical___-", int(thunder_shock * pikachu_critical))
                                    elif 220 < critical_odds <= thunder_shock_odd:
                                        zapdos_hp -= 0
                                        print("\nmiss___")
                                    print("\n", z, zapdos_hp, "HP")
                                    zapdos_life_indicator (zapdos_hp)

                                elif pikachus_turn == "3" :
                                    print(pu, p_qa)
                                    critical_odds = random.randint(1, quick_attack_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        zapdos_hp -= quick_attack
                                        print("\n-{}".format(quick_attack))
                                    elif 160 <= critical_odds <= 200:
                                        zapdos_hp -= int(quick_attack * pikachu_critical)
                                        print("\ncritical___-", int(quick_attack * pikachu_critical))
                                    elif 200 < critical_odds <= quick_attack_odd:
                                        zapdos_hp -= 0
                                        print("\nmiss___")
                                    print("\n", z, zapdos_hp, "HP")
                                    zapdos_life_indicator (zapdos_hp)
                                
                                elif pikachus_turn == "4" :
                                    print(pu, p_f)
                                    critical_odds = random.randint(1, feint_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        zapdos_hp -= feint
                                        print("\n-{}".format(feint))
                                    elif 160 <= critical_odds <= 200:
                                        zapdos_hp -= int(feint * pikachu_critical)
                                        print("\ncritical___-", int(feint * pikachu_critical))
                                    elif 200 < critical_odds <= feint_odd:
                                        zapdos_hp -= 0
                                        print("\nmiss___")
                                    print("\n", z, zapdos_hp, "HP")
                                    zapdos_life_indicator (zapdos_hp)
                            sleep(3)
                            system("cls")

                            if zapdos_hp > 0 :
                                zapdos_turn = random.randint(1, 5)

                                if zapdos_turn == 1 :
                                    print(zu, z_pe)
                                    critical_odds = random.randint(1, peck_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= peck
                                        print("\n-{}".format(peck))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(peck * zapdos_critical)
                                        print("\ncritical___-", int (peck * zapdos_critical))
                                    elif 200 < critical_odds <= peck_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif zapdos_turn == 2 :
                                    print(zu, z_pl)
                                    critical_odds = random.randint(1, pluck_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= pluck
                                        print("\n-{}".format(pluck))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(pluck * zapdos_critical)
                                        print("\ncritical___-", int (pluck * zapdos_critical))
                                    elif 200 < critical_odds <= pluck_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif zapdos_turn == 3 :
                                    print(zu, z_ap)
                                    critical_odds = random.randint(1, ancient_power_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= ancient_power
                                        print("\n-{}".format(ancient_power))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(ancient_power * zapdos_critical)
                                        print("\ncritical___-", int (ancient_power * zapdos_critical))
                                    elif 200 < critical_odds <= ancient_power_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif zapdos_turn == 4 :
                                    print(zu, z_t)
                                    critical_odds = random.randint(1, thunder_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= thunder
                                        print("\n-{}".format(thunder))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(thunder * zapdos_critical)
                                        print("\ncritical___-", int (thunder * zapdos_critical))
                                    elif 200 < critical_odds <= thunder_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif zapdos_turn == 5 :
                                    print(zu, z_zc)
                                    critical_odds = random.randint(1, zap_cannon_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= zap_cannon
                                        print("\n-{}".format(zap_cannon))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(zap_cannon * zapdos_critical)
                                        print("\ncritical___-", int (zap_cannon * zapdos_critical))
                                    elif 200 < critical_odds <= zap_cannon_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))
                            sleep(3); system("cls")

                            if zapdos_hp < 1:
                                electric_done = True
                                true_3 = True
                            elif pikachu_hp < 1:
                                electric_done = True
                                true_5 = True

                        pikachu_lvl += random.randint(1, 3)
                        pikachu_critical += 0.1
                        true_start = False

                if not true_start: # enter the fighting
                    if fighting_gym[POS_X] == coordinate_x and fighting_gym[POS_Y] == coordinate_y:
                        print(); system("cls"); print("You entered -Cianwood Fighting Gym\n")

                        while not fighting_done: # fighting gym fight
                            if pikachu_hp > 0 :
                                print(h, hitmonchan_hp, "HP")
                                hitmonchan_life_indicator (hitmonchan_hp)
                                print("\nPikachu's Critical: [", pikachu_critical, "]\n")
                                pikachus_turn = None
                                while pikachus_turn != "1" and pikachus_turn != "2" and pikachus_turn != "3" and pikachus_turn != "4" :
                                    pikachus_turn = input(input1)
                                system("cls")

                                if pikachus_turn == "1" :
                                    print(pu, p_n)
                                    critical_odds = random.randint(1, nuzzle_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        hitmonchan_hp -= nuzzle
                                        print("\n-{}".format(nuzzle))
                                    elif 160 <= critical_odds <= 200:
                                        hitmonchan_hp -= int(nuzzle * pikachu_critical)
                                        print("\ncritical___-", int(nuzzle * pikachu_critical))
                                    elif 200 < critical_odds <= nuzzle_odd:
                                        hitmonchan_hp -= 0
                                        print("\nmiss___")
                                    print("\n", h, hitmonchan_hp, "HP")
                                    hitmonchan_life_indicator (hitmonchan_hp)

                                elif pikachus_turn == "2" :
                                    print(pu, p_ts)
                                    critical_odds = random.randint(1, thunder_shock_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        hitmonchan_hp -= thunder_shock
                                        print("\n-{}".format(thunder_shock))
                                    elif 160 <= critical_odds <= 220:
                                        hitmonchan_hp -= int(thunder_shock * pikachu_critical)
                                        print("\ncritical___-", int(thunder_shock * pikachu_critical))
                                    elif 220 < critical_odds <= thunder_shock_odd:
                                        hitmonchan_hp -= 0
                                        print("\nmiss___")
                                    print("\n", h, hitmonchan_hp, "HP")
                                    hitmonchan_life_indicator (hitmonchan_hp)

                                elif pikachus_turn == "3" :
                                    print(pu, p_qa)
                                    critical_odds = random.randint(1, quick_attack_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        hitmonchan_hp -= quick_attack
                                        print("\n-{}".format(quick_attack))
                                    elif 160 <= critical_odds <= 200:
                                        hitmonchan_hp -= int(quick_attack * pikachu_critical)
                                        print("\ncritical___-", int(quick_attack * pikachu_critical))
                                    elif 200 < critical_odds <= quick_attack_odd:
                                        hitmonchan_hp -= 0
                                        print("\nmiss___")
                                    print("\n", h, hitmonchan_hp, "HP")
                                    hitmonchan_life_indicator (hitmonchan_hp)
                                
                                elif pikachus_turn == "4" :
                                    print(pu, p_f)
                                    critical_odds = random.randint(1, feint_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        hitmonchan_hp -= feint
                                        print("\n-{}".format(feint))
                                    elif 160 <= critical_odds <= 200:
                                        hitmonchan_hp -= int(feint * pikachu_critical)
                                        print("\ncritical___-", int(feint * pikachu_critical))
                                    elif 200 < critical_odds <= feint_odd:
                                        hitmonchan_hp -= 0
                                        print("\nmiss___")
                                    print("\n", h, hitmonchan_hp, "HP")
                                    hitmonchan_life_indicator (hitmonchan_hp)
                            sleep(3)
                            system("cls")

                            if hitmonchan_hp > 0 :
                                hitmonchan_turn = random.randint(1, 5)

                                if hitmonchan_turn == 1 :
                                    print(hu, h_dp)
                                    critical_odds = random.randint(1, drain_punch_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= drain_punch
                                        print("\n-{}".format(drain_punch))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(drain_punch * hitmonchan_critical)
                                        print("\ncritical___-", int (drain_punch * hitmonchan_critical))
                                    elif 200 < critical_odds <= drain_punch_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif hitmonchan_turn == 2 :
                                    print(hu, h_php)
                                    critical_odds = random.randint(1, power_up_punch_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= power_up_punch
                                        print("\n-{}".format(power_up_punch))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(power_up_punch * hitmonchan_critical)
                                        print("\ncritical___-", int (power_up_punch * hitmonchan_critical))
                                    elif 200 < critical_odds <= power_up_punch_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif hitmonchan_turn == 3 :
                                    print(hu, h_fip)
                                    critical_odds = random.randint(1, fire_punch_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= fire_punch
                                        print("\n-{}".format(fire_punch))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(fire_punch * hitmonchan_critical)
                                        print("\ncritical___-", int (fire_punch * hitmonchan_critical))
                                    elif 200 < critical_odds <= fire_punch_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif hitmonchan_turn == 4 :
                                    print(hu, h_mp)
                                    critical_odds = random.randint(1, mega_punch_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= mega_punch
                                        print("\n-{}".format(mega_punch))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(mega_punch * hitmonchan_critical)
                                        print("\ncritical___-", int (mega_punch * hitmonchan_critical))
                                    elif 200 < critical_odds <= mega_punch_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))

                                elif hitmonchan_turn == 5 :
                                    print(hu, h_fop)
                                    critical_odds = random.randint(1, focus_punch_odd)
                                    sleep(1)
                                    if critical_odds < 160:
                                        pikachu_hp -= focus_punch
                                        print("\n-{}".format(focus_punch))
                                    elif 160 <= critical_odds <= 200:
                                        pikachu_hp -= int(focus_punch * hitmonchan_critical)
                                        print("\ncritical___-", int (focus_punch * hitmonchan_critical))
                                    elif 200 < critical_odds <= focus_punch_odd:
                                        pikachu_hp -= 0
                                        print("\nmiss___")
                                    print("\n", p, pikachu_hp, "HP")
                                    print (pikachu_life_indicator (pikachu_hp, PIKACHU_LVL_BASED_HP))
                            sleep(3); system("cls")

                            if hitmonchan_hp < 1:
                                fighting_done = True
                                true_4 = True
                            elif pikachu_hp < 1:
                                fighting_done = True
                                true_5 = True

                        pikachu_lvl += random.randint(2, 3)
                        pikachu_critical += 0.1
                        true_start = False



            print("{}".format(char_to_draw), end="") # printer
        print(" |") # right side

    print("-"* (MAP_WIDTH* 2 + 3)) # bottom
    # draw map finish

    if true_1 or true_2 or true_3 or true_4:# Gym win
        system("cls"); print("\nGym Cleared\nMove to Continue")
        true_1 = False; true_2 = False; true_3 = False; true_4 = False
    if rock_done and water_done and electric_done and fighting_done: # win conditions
        system("cls"); print("You win all battles, congratulations!")
        true_0 = True
    if true_5: # Gym lost
        system("cls"); print("\nGym Fight Losed\n\nYou Lose")
        true_0 = True
    if true_6: # pikachu restoration
        pikachu_hp = PIKACHU_LVL_BASED_HP
        print(); system("cls"); print("Pikachu's HP Restored\nMove to Continue")
        true_6 = False

    direction = readchar() # where he/she want to move
    new_position = None

    if direction == "w": # up movement
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
        if obstacle_colocation[new_position[POS_Y]][new_position[POS_X]] != ",":
            my_position = new_position