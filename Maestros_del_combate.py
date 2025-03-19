import random
import time
import os
import readchar

all_done = False
rock_limiter = True
rock_done = False
rock_win = False
rock_lose = False
water_limiter = True
water_done = False
water_win = False
water_lose = False
electric_limiter = True
electric_done = False
electric_win = False
electric_lose = False
fighting_limiter = True
fighting_done = False
fighting_win = False
fighting_lose = False
gym1 = False
gym2 = False
gym3 = False
gym4 = False
map = False
rock_gym = None
water_gym = None
electric_gym = None
fighting_gym = None
gyms = []
## pokemon
p = "Pikachu"; pu = "Pikachu uses"
pikachu_damage = random.randint(10, 12)
pikachu_base_hp = 50
pikachu_critical = (random.randint(14, 20))/10
pikachu_lvl = random.randint(30, 32)
PIKACHU_LVL_BASED_HP = pikachu_base_hp + pikachu_lvl*3 # for each lvl 3+ hp
pikachu_hp = PIKACHU_LVL_BASED_HP
pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
pikachu_health_bar_print = "[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar))
s = "Squirtle"; su = "Squirtle uses"
squirtle_damage = random.randint(10, 12)
squirtle_base_hp = 68
squirtle_critical = (random.randint(11, 15))/10
squirtle_lvl = random.randint(26, 30)
SQUIRTLE_LVL_BASED_HP = squirtle_base_hp + squirtle_lvl*3 # for each lvl 3+ hp
squirtle_hp = SQUIRTLE_LVL_BASED_HP
squirtle_health_bar = int(squirtle_hp * 30 / SQUIRTLE_LVL_BASED_HP)
squirtle_health_bar_print = "[{}{}]".format("#" * squirtle_health_bar, " " * (30 - squirtle_health_bar))
l = "Lairon"; lu = "Lairon uses"
lairon_damage = random.randint(10, 12)
lairon_base_hp = 78
lairon_critical = (random.randint(11, 14))/10
lairon_lvl = random.randint(29, 32)
LAIRON_LVL_BASED_HP = lairon_base_hp + lairon_lvl*3 # for each lvl 3+ hp
lairon_hp = LAIRON_LVL_BASED_HP
lairon_health_bar = int(lairon_hp * 30 / LAIRON_LVL_BASED_HP)
lairon_health_bar_print = "[{}{}]".format("#" * lairon_health_bar, " " * (30 - lairon_health_bar))
z = "Zapdos"; zu = "Zapdos uses"
zapdos_damage = random.randint(10, 12)
zapdos_base_hp = 60
zapdos_critical = (random.randint(11, 12))/10
zapdos_lvl = random.randint(32, 34)
ZAPDOS_LVL_BASED_HP = zapdos_base_hp + zapdos_lvl*3 # for each lvl 3+ hp
zapdos_hp = ZAPDOS_LVL_BASED_HP
zapdos_health_bar = int(zapdos_hp * 30 / ZAPDOS_LVL_BASED_HP)
zapdos_health_bar_print = "[{}{}]".format("#" * zapdos_health_bar, " " * (30 - zapdos_health_bar))
h = "Hitmonchan"; hu = "Hitmonchan uses"
hitmonchan_damage = random.randint(10, 12)
hitmonchan_base_hp = 48
hitmonchan_critical = (random.randint(11, 13))/10
hitmonchan_lvl = 36
HITMOCHAN_LVL_BASED_HP = hitmonchan_base_hp + hitmonchan_lvl*3 # for each lvl 3+ hp
hitmonchan_hp = HITMOCHAN_LVL_BASED_HP
hitmonchan_health_bar = int(hitmonchan_hp * 30 / HITMOCHAN_LVL_BASED_HP)
hitmonchan_health_bar_print = "[{}{}]".format("#" * hitmonchan_health_bar, " " * (30 - hitmonchan_health_bar))
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
obstacle_column_limiter = 0
obstacle_row_limiter = 0
obstacle_colocation = ""
k = " "; odds = [",,,", ",,", k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k, k]

while obstacle_column_limiter < MAP_HEIGHT: # random map generator
    while obstacle_row_limiter < MAP_WIDTH:
        odds_limiter = random.choice(odds)
        if odds_limiter == " ":
            obstacle_row_limiter += 1
        elif odds_limiter == ",,":
            obstacle_row_limiter += 2
        elif odds_limiter == ",,,":
            obstacle_row_limiter += 3
        obstacle_colocation += odds_limiter
    obstacle_colocation += "."
    obstacle_column_limiter += 1
    obstacle_row_limiter = 0
obstacle_colocation = [list(row) for row in obstacle_colocation.split(".")]
while not gym1: # rock gym position
    new_gym = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
    if new_gym not in gyms and new_gym != my_position and obstacle_colocation[new_gym[POS_Y]][new_gym[POS_X]] != ",":
        gyms.append(new_gym)
        rock_gym = new_gym
        gym1 = True
while not gym2: # water gym position
    new_gym = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
    if new_gym not in gyms and new_gym != my_position and obstacle_colocation[new_gym[POS_Y]][new_gym[POS_X]] != ",":
        gyms.append(new_gym)
        water_gym = new_gym
        gym2 = True
while not gym3: # electric gym position
    new_gym = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
    if new_gym not in gyms and new_gym != my_position and obstacle_colocation[new_gym[POS_Y]][new_gym[POS_X]] != ",":
        gyms.append(new_gym)
        electric_gym = new_gym
        gym3 = True
while not gym4: # fighting gym position
    new_gym = [random.randint(0, MAP_WIDTH -1), random.randint(0, MAP_HEIGHT -1)]
    if new_gym not in gyms and new_gym != my_position and obstacle_colocation[new_gym[POS_Y]][new_gym[POS_X]] != ",":
        gyms.append(new_gym)
        fighting_gym = new_gym
        gym4 = True

# Intro giving info to the player
os.system("cls"); print("Pikachu's lvl:", pikachu_lvl, "\n"); print(p, pikachu_hp, "HP\n", pikachu_health_bar_print, "\n")
print(p, "know 4 movements\nNuzlle, Thunder Shock, Quick Attack and Feint"); time.sleep(3); os.system("cls")

# game starts
os.system("cls"); print("\nWASD to move"); time.sleep(1)

while not all_done:
    os.system("cls")
    # draw map start
    print("-"* (MAP_WIDTH* 2 + 3)) # top

    for coordinate_y in range(MAP_HEIGHT): # Y
        print("|", end="") # left side

        for coordinate_x in range(MAP_WIDTH): # X
            char_to_draw = "  "

            if rock_gym[POS_X] == coordinate_x and rock_gym[POS_Y] == coordinate_y: # rock gym print
                char_to_draw = " R"
            if water_gym[POS_X] == coordinate_x and water_gym[POS_Y] == coordinate_y: # water gym print
                char_to_draw = " W"
            if electric_gym[POS_X] == coordinate_x and electric_gym[POS_Y] == coordinate_y: # electric gym print
                char_to_draw = " E"
            if fighting_gym[POS_X] == coordinate_x and fighting_gym[POS_Y] == coordinate_y: # fighting gym print
                char_to_draw = " F"

            if obstacle_colocation[coordinate_y][coordinate_x] == ",": # walls
                if obstacle_colocation[my_position[POS_Y]][my_position[POS_X]] != ",": # walls print
                    char_to_draw = " #"

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y: # your position
                char_to_draw = " @" # you

                if rock_limiter:# enter the rock gym
                    if rock_gym[POS_X] == coordinate_x and rock_gym[POS_Y] == coordinate_y:
                        print(); os.system("cls"); print("You entered -Pewter Rock Gym-\n")

                        while not rock_done: # rock gym fight
                            if pikachu_hp > 0 :
                                print(l, lairon_hp, "HP")
                                lairon_health_bar = int(lairon_hp * 30 / LAIRON_LVL_BASED_HP)
                                print("[{}{}]".format("#" * lairon_health_bar, " " * (30 - lairon_health_bar)))
                                print("\nPikachu's Critical: [", pikachu_critical, "]\n")
                                pikachus_turn = None
                                while pikachus_turn != "1" and pikachus_turn != "2" and pikachus_turn != "3" and pikachus_turn != "4" :
                                    pikachus_turn = input(input1)
                                os.system("cls")

                                if pikachus_turn == "1" :
                                    print(pu, p_n)
                                    critical_odds = random.randint(1, nuzzle_odd)
                                    time.sleep(1)
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
                                    lairon_health_bar = int(lairon_hp * 30 / LAIRON_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * lairon_health_bar, " " * (30 - lairon_health_bar)))

                                elif pikachus_turn == "2" :
                                    print(pu, p_ts)
                                    critical_odds = random.randint(1, thunder_shock_odd)
                                    time.sleep(1)
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
                                    lairon_health_bar = int(lairon_hp * 30 / LAIRON_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * lairon_health_bar, " " * (30 - lairon_health_bar)))

                                elif pikachus_turn == "3" :
                                    print(pu, p_qa)
                                    critical_odds = random.randint(1, quick_attack_odd)
                                    time.sleep(1)
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
                                    lairon_health_bar = int(lairon_hp * 30 / LAIRON_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * lairon_health_bar, " " * (30 - lairon_health_bar)))
                                
                                elif pikachus_turn == "4" :
                                    print(pu, p_f)
                                    critical_odds = random.randint(1, feint_odd)
                                    time.sleep(1)
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
                                    lairon_health_bar = int(lairon_hp * 30 / LAIRON_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * lairon_health_bar, " " * (30 - lairon_health_bar)))
                            time.sleep(3)
                            os.system("cls")

                            if lairon_hp > 0 :
                                lairon_turn = random.randint(1, 5)

                                if lairon_turn == 1 :
                                    print(lu, l_mc)
                                    critical_odds = random.randint(1, metal_claw_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif lairon_turn == 2 :
                                    print(lu, l_rt)
                                    critical_odds = random.randint(1, rock_tomb_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif lairon_turn == 3 :
                                    print(lu, l_hb)
                                    critical_odds = random.randint(1, headbutt_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif lairon_turn == 4 :
                                    print(lu, l_rs)
                                    critical_odds = random.randint(1, rock_slide_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif lairon_turn == 5 :
                                    print(lu, l_it)
                                    critical_odds = random.randint(1, iron_tail_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))
                            time.sleep(3); os.system("cls")

                            if lairon_hp < 1:
                                rock_done = True
                                rock_win = True
                            elif pikachu_hp < 1:
                                rock_done = True
                                rock_lose = True

                        lairon_hp = LAIRON_LVL_BASED_HP
                        pikachu_hp = PIKACHU_LVL_BASED_HP
                        pikachu_lvl += random.randint(1, 2)
                        pikachu_critical += 0.1
                        rock_limiter = False
                if water_limiter: # enter the water gym
                    if water_gym[POS_X] == coordinate_x and water_gym[POS_Y] == coordinate_y:
                        print(); os.system("cls"); print("You entered -Cerulean Water Gym-\n")

                        while not water_done: # water gym fight
                            if pikachu_hp > 0 :
                                print(s, squirtle_hp, "HP")
                                squirtle_health_bar = int(squirtle_hp * 30 / SQUIRTLE_LVL_BASED_HP)
                                print("[{}{}]".format("#" * squirtle_health_bar, " " * (30 - squirtle_health_bar)))
                                print("\nPikachu's Critical: [", pikachu_critical, "]\n")
                                pikachus_turn = None
                                while pikachus_turn != "1" and pikachus_turn != "2" and pikachus_turn != "3" and pikachus_turn != "4" :
                                    pikachus_turn = input(input1)
                                os.system("cls")

                                if pikachus_turn == "1" :
                                    print(pu, p_n)
                                    critical_odds = random.randint(1, nuzzle_odd)
                                    time.sleep(1)
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
                                    squirtle_health_bar = int(squirtle_hp * 30 / SQUIRTLE_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * squirtle_health_bar, " " * (30 - squirtle_health_bar)))

                                elif pikachus_turn == "2" :
                                    print(pu, p_ts)
                                    critical_odds = random.randint(1, thunder_shock_odd)
                                    time.sleep(1)
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
                                    squirtle_health_bar = int(squirtle_hp * 30 / SQUIRTLE_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * squirtle_health_bar, " " * (30 - squirtle_health_bar)))

                                elif pikachus_turn == "3" :
                                    print(pu, p_qa)
                                    critical_odds = random.randint(1, quick_attack_odd)
                                    time.sleep(1)
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
                                    squirtle_health_bar = int(squirtle_hp * 30 / SQUIRTLE_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * squirtle_health_bar, " " * (30 - squirtle_health_bar)))
                                
                                elif pikachus_turn == "4" :
                                    print(pu, p_f)
                                    critical_odds = random.randint(1, feint_odd)
                                    time.sleep(1)
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
                                    squirtle_health_bar = int(squirtle_hp * 30 / SQUIRTLE_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * squirtle_health_bar, " " * (30 - squirtle_health_bar)))
                            time.sleep(3)
                            os.system("cls")

                            if squirtle_hp > 0 :
                                squirtle_turn = random.randint(1, 5)

                                if squirtle_turn == 1 :
                                    print(su, s_t)
                                    critical_odds = random.randint(1, tackle_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif squirtle_turn == 2 :
                                    print(su, s_wg)
                                    critical_odds = random.randint(1, water_gun_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif squirtle_turn == 3 :
                                    print(su, s_rs)
                                    critical_odds = random.randint(1, rapid_spin_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif squirtle_turn == 4 :
                                    print(su, s_b)
                                    critical_odds = random.randint(1, bite_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif squirtle_turn == 5 :
                                    print(su, s_wp)
                                    critical_odds = random.randint(1, water_pulse_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))
                            time.sleep(3); os.system("cls")

                            if squirtle_hp < 1:
                                water_done = True
                                water_win = True
                            elif pikachu_hp < 1:
                                water_done = True
                                water_lose = True

                        squirtle_hp = SQUIRTLE_LVL_BASED_HP
                        pikachu_hp = PIKACHU_LVL_BASED_HP
                        pikachu_lvl += random.randint(1, 2)
                        pikachu_critical += 0.1
                        water_limiter = False
                if electric_limiter: # enter the electric gym
                    if electric_gym[POS_X] == coordinate_x and electric_gym[POS_Y] == coordinate_y:
                        print(); os.system("cls"); print("You entered -Vermilion Electric Gym-\n")

                        while not electric_done: # electric gym fight
                            if pikachu_hp > 0 :
                                print(z, zapdos_hp, "HP")
                                zapdos_health_bar = int(zapdos_hp * 30 / ZAPDOS_LVL_BASED_HP)
                                print("[{}{}]".format("#" * zapdos_health_bar, " " * (30 - zapdos_health_bar)))
                                print("\nPikachu's Critical: [", pikachu_critical, "]\n")
                                pikachus_turn = None
                                while pikachus_turn != "1" and pikachus_turn != "2" and pikachus_turn != "3" and pikachus_turn != "4" :
                                    pikachus_turn = input(input1)
                                os.system("cls")

                                if pikachus_turn == "1" :
                                    print(pu, p_n)
                                    critical_odds = random.randint(1, nuzzle_odd)
                                    time.sleep(1)
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
                                    zapdos_health_bar = int(zapdos_hp * 30 / ZAPDOS_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * zapdos_health_bar, " " * (30 - zapdos_health_bar)))

                                elif pikachus_turn == "2" :
                                    print(pu, p_ts)
                                    critical_odds = random.randint(1, thunder_shock_odd)
                                    time.sleep(1)
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
                                    zapdos_health_bar = int(zapdos_hp * 30 / ZAPDOS_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * zapdos_health_bar, " " * (30 - zapdos_health_bar)))

                                elif pikachus_turn == "3" :
                                    print(pu, p_qa)
                                    critical_odds = random.randint(1, quick_attack_odd)
                                    time.sleep(1)
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
                                    zapdos_health_bar = int(zapdos_hp * 30 / ZAPDOS_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * zapdos_health_bar, " " * (30 - zapdos_health_bar)))
                                
                                elif pikachus_turn == "4" :
                                    print(pu, p_f)
                                    critical_odds = random.randint(1, feint_odd)
                                    time.sleep(1)
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
                                    zapdos_health_bar = int(zapdos_hp * 30 / ZAPDOS_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * zapdos_health_bar, " " * (30 - zapdos_health_bar)))
                            time.sleep(3)
                            os.system("cls")

                            if zapdos_hp > 0 :
                                zapdos_turn = random.randint(1, 5)

                                if zapdos_turn == 1 :
                                    print(zu, z_pe)
                                    critical_odds = random.randint(1, peck_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif zapdos_turn == 2 :
                                    print(zu, z_pl)
                                    critical_odds = random.randint(1, pluck_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif zapdos_turn == 3 :
                                    print(zu, z_ap)
                                    critical_odds = random.randint(1, ancient_power_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif zapdos_turn == 4 :
                                    print(zu, z_t)
                                    critical_odds = random.randint(1, thunder_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif zapdos_turn == 5 :
                                    print(zu, z_zc)
                                    critical_odds = random.randint(1, zap_cannon_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))
                            time.sleep(3); os.system("cls")

                            if zapdos_hp < 1:
                                electric_done = True
                                electric_win = True
                            elif pikachu_hp < 1:
                                electric_done = True
                                electric_lose = True

                        zapdos_hp = ZAPDOS_LVL_BASED_HP
                        pikachu_hp = PIKACHU_LVL_BASED_HP
                        pikachu_lvl += random.randint(1, 3)
                        pikachu_critical += 0.1
                        electric_limiter = False
                if fighting_limiter: # enter the fighting
                    if fighting_gym[POS_X] == coordinate_x and fighting_gym[POS_Y] == coordinate_y:
                        print(); os.system("cls"); print("You entered -Cianwood Fighting Gym\n")

                        while not fighting_done: # fighting gym fight
                            if pikachu_hp > 0 :
                                print(h, hitmonchan_hp, "HP")
                                hitmonchan_health_bar = int(hitmonchan_hp * 30 / HITMOCHAN_LVL_BASED_HP)
                                print("[{}{}]".format("#" * hitmonchan_health_bar, " " * (30 - hitmonchan_health_bar)))
                                print("\nPikachu's Critical: [", pikachu_critical, "]\n")
                                pikachus_turn = None
                                while pikachus_turn != "1" and pikachus_turn != "2" and pikachus_turn != "3" and pikachus_turn != "4" :
                                    pikachus_turn = input(input1)
                                os.system("cls")

                                if pikachus_turn == "1" :
                                    print(pu, p_n)
                                    critical_odds = random.randint(1, nuzzle_odd)
                                    time.sleep(1)
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
                                    hitmonchan_health_bar = int(hitmonchan_hp * 30 / HITMOCHAN_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * hitmonchan_health_bar, " " * (30 - hitmonchan_health_bar)))

                                elif pikachus_turn == "2" :
                                    print(pu, p_ts)
                                    critical_odds = random.randint(1, thunder_shock_odd)
                                    time.sleep(1)
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
                                    hitmonchan_health_bar = int(hitmonchan_hp * 30 / HITMOCHAN_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * hitmonchan_health_bar, " " * (30 - hitmonchan_health_bar)))

                                elif pikachus_turn == "3" :
                                    print(pu, p_qa)
                                    critical_odds = random.randint(1, quick_attack_odd)
                                    time.sleep(1)
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
                                    hitmonchan_health_bar = int(hitmonchan_hp * 30 / HITMOCHAN_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * hitmonchan_health_bar, " " * (30 - hitmonchan_health_bar)))
                                
                                elif pikachus_turn == "4" :
                                    print(pu, p_f)
                                    critical_odds = random.randint(1, feint_odd)
                                    time.sleep(1)
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
                                    hitmonchan_health_bar = int(hitmonchan_hp * 30 / HITMOCHAN_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * hitmonchan_health_bar, " " * (30 - hitmonchan_health_bar)))
                            time.sleep(3)
                            os.system("cls")

                            if hitmonchan_hp > 0 :
                                hitmonchan_turn = random.randint(1, 5)

                                if hitmonchan_turn == 1 :
                                    print(hu, h_dp)
                                    critical_odds = random.randint(1, drain_punch_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif hitmonchan_turn == 2 :
                                    print(hu, h_php)
                                    critical_odds = random.randint(1, power_up_punch_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif hitmonchan_turn == 3 :
                                    print(hu, h_fip)
                                    critical_odds = random.randint(1, fire_punch_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif hitmonchan_turn == 4 :
                                    print(hu, h_mp)
                                    critical_odds = random.randint(1, mega_punch_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))

                                elif hitmonchan_turn == 5 :
                                    print(hu, h_fop)
                                    critical_odds = random.randint(1, focus_punch_odd)
                                    time.sleep(1)
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
                                    pikachu_health_bar = int(pikachu_hp * 30 / PIKACHU_LVL_BASED_HP)
                                    print("[{}{}]".format("#" * pikachu_health_bar, " " * (30 - pikachu_health_bar)))
                            time.sleep(3); os.system("cls")

                            if hitmonchan_hp < 1:
                                fighting_done = True
                                fighting_win = True
                            elif pikachu_hp < 1:
                                fighting_done = True
                                fighting_lose = True

                        hitmonchan_hp = HITMOCHAN_LVL_BASED_HP
                        pikachu_hp = PIKACHU_LVL_BASED_HP
                        pikachu_lvl += random.randint(2, 3)
                        pikachu_critical += 0.1
                        fighting_limiter = False

            print("{}".format(char_to_draw), end="") # printer
        print(" |") # right side

    print("-"* (MAP_WIDTH* 2 + 3)) # bottom
    # draw map finish

    if rock_win or water_win or electric_win or fighting_win:# Gym win
        os.system("cls"); print("\nGym Cleared\nMove to Continue")
        rock_win = False
        water_win = False
        electric_win = False
        fighting_win = False
    if rock_lose or water_lose or electric_lose or fighting_lose: # Gym lost
        os.system("cls"); print("\nGym Fight Losed\n\nYou Lose")
        all_done = True
    if rock_done and water_done and electric_done and fighting_done: # win conditions
        os.system("cls"); print("You win all battles, congratulations!")
        all_done = True

    direction = readchar.readchar() # where he/she want to move
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