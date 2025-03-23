import random
import core.utils
import data.game_state as gs
import ui.messages as uim

def damages(attacker, attack, enemy):
    """
    Realiza un ataque de 'attacker' usando el objeto 'attack' contra 'enemy',
    calculando y aplicando el daño de forma crítica o normal.
    """
    print(f"{attacker.name} uses {attack.name}\n")
    
    if random.random() < attack.accuracy:
        if random.random() < attack.critical_chance:
            damage_dealt = int(attack.damage * attack.critical_multiplier)
            print(f"Critical hit! -{damage_dealt}\n")
        else:
            damage_dealt = attack.damage
            print(f"-{damage_dealt}\n")
        enemy.hp -= damage_dealt
    else:
        print("Miss___\n")
        
    print(f"{enemy.name} {enemy.hp} HP\n{core.utils.message_life_indicator(enemy)}\n")

def battle(player_pokemon, enemy_pokemon, gym_name):
    """
    Función de batalla general para enfrentar dos pokémons.
    Retorna:
      - "win" si el jugador gana,
      - "lose" si el jugador pierde,
      - "exit" si el jugador decide salir.
    """
    print()
    core.utils.limpiar_pantalla()
    input(f"You entered -{gym_name} Gym-\n\n")
    core.utils.limpiar_pantalla()

    while True:
        # Turno del jugador
        if player_pokemon.hp > 0:
            my_turn = None
            while my_turn not in ["1", "2", "3", "4", "exit"]:
                print(uim.message_battle_starts(player_pokemon, enemy_pokemon))
                my_turn = input(uim.message_pokemon_attacks(player_pokemon))
                core.utils.limpiar_pantalla()

            if my_turn == "exit":
                return "exit"

            attack_index = int(my_turn) - 1
            core.battle.damages(player_pokemon, player_pokemon.attacks[attack_index], enemy_pokemon)
            core.utils.time_battle_end()
            core.utils.limpiar_pantalla()
        else:
            return "lose"

        # Verificar si el enemigo ha sido derrotado
        if enemy_pokemon.hp < 1:
            return "win"

        # Turno del enemigo
        if enemy_pokemon.hp > 0:
            enemy_attack = random.randint(1, 4)
            core.battle.damages(enemy_pokemon, enemy_pokemon.attacks[enemy_attack - 1], player_pokemon)
            core.utils.time_battle_end()
            core.utils.limpiar_pantalla()

        # Verificar si el jugador ha sido derrotado
        if player_pokemon.hp < 1:
            return "lose"
        
def handle_gym_battle(player, gym, trainer, flag_key, gym_name, hp_range, damage_incr, level_incr):
    """
    Maneja la batalla de un gimnasio.

    Parámetros:
      - player: el jugador (o su Pokémon) que participa.
      - gym: objeto del gimnasio con atributos x e y.
      - trainer: el entrenador enemigo asociado a este gimnasio.
      - flag_key: clave del diccionario gs.gym_flags para identificar si ya se realizó la batalla.
      - gym_name: nombre del gimnasio (para mostrar en la batalla).
      - hp_range: tupla con el rango para aumentar max_hp en caso de victoria.
      - damage_incr: cantidad a incrementar en el daño del Pokémon al ganar.
      - level_incr: cantidad a incrementar en el nivel del Pokémon al ganar.

    Retorna:
      - "win", "lose", "exit" o None (si no se ejecuta la batalla).
    """
    pos_x = 0
    pos_y = 1

    if gym.x == gs.user_position[pos_x] and gym.y == gs.user_position[pos_y] and not gs.gym_flags[flag_key]:
        resultado = battle(player.pokemons[0], trainer.pokemons[0], gym_name)
        if resultado == "win":
            player.pokemons[0].max_hp += random.randint(hp_range[0], hp_range[1])
            player.pokemons[0].damage += damage_incr
            player.pokemons[0].level += level_incr
            gs.gym_flags[flag_key] = True
            return "win"
        elif resultado == "lose":
            gs.gym_flags[flag_key] = True
            return "lose"
        elif resultado == "exit":
            gs.gym_flags[flag_key] = True
            return "exit"
    return None
