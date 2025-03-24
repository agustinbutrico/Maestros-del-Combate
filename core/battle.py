import random
import core.utils
import data.game_state as gs
import ui.messages as uim

def movement_damage(attack, enemy):
    """
    Verifica el tipo de daño realizado en el movimiento.
      - "move_normal" si el daño del movimiento fue normal,
      - "move_critic" si el daño del movimiento fue critico,
      - "move_miss" si el daño del movimiento fue nulo,
    Aplica el daño y lo devuelve para ser usado en mensajes
    """
    gs.battle_flags["move_normal"] = False
    gs.battle_flags["move_critic"] = False
    gs.battle_flags["move_miss"] = False

    if random.random() < attack.accuracy:
        if random.random() < attack.critical_chance:
            gs.battle_flags["move_critic"] = True
            damage_dealt = int(attack.damage * attack.critical_multiplier)
        else:
            gs.battle_flags["move_normal"] = True
            damage_dealt = attack.damage
    else:
        gs.battle_flags["move_miss"] = True
        damage_dealt = 0

    enemy.hp -= damage_dealt # Se le quita la vida al enemigo
    return damage_dealt

def player_turn(trainer):
    """
    Gestiona el turno del jugador: muestra los mensajes, solicita la elección y ejecuta el ataque.
    Retorna "exit" si el jugador decide salir o None para continuar la batalla.
    """
    my_turn = None
    while my_turn not in ["1", "2", "3", "4"]:
        core.utils.limpiar_pantalla()
        print(uim.message_battle_starts(trainer))
        my_turn = input(uim.message_pokemon_attacks(gs.user))

    pokemon_attack_index = int(my_turn) - 1
    pokemon_attack = gs.user.pokemons[0].attacks[pokemon_attack_index]
    damage_dealt = movement_damage(pokemon_attack, trainer.pokemons[0])
    uim.message_movement_damage(gs.user.pokemons[0], pokemon_attack, trainer.pokemons[0], damage_dealt)
    core.utils.time_battle_end()

def enemy_turn(trainer):
    """
    Ejecuta el turno del enemigo de forma aleatoria y aplica el daño.
    """
    enemy_pokemon_attack = random.randint(1, 4)
    enemy_pokemon_attack = trainer.pokemons[0].attacks[enemy_pokemon_attack - 1]
    damage_dealt = movement_damage(enemy_pokemon_attack, gs.user.pokemons[0])
    uim.message_movement_damage(trainer.pokemons[0], enemy_pokemon_attack, gs.user.pokemons[0], damage_dealt)
    core.utils.time_battle_end()

def verify_battle_outcome(trainer):
    """
    Verifica el estado de la batalla.
      - "won" si el enemigo fue derrotado,
      - "lost" si el jugador fue derrotado,
      - "ongoing" si la batalla continúa.
    """
    if trainer.pokemons[0].hp < 1:
        gs.battle_flags["battle_won"] = True
        gs.battle_flags["battle_ongoing"] = False
    if gs.user.pokemons[0].hp < 1:
        gs.battle_flags["battle_lost"] = True
        gs.battle_flags["battle_ongoing"] = False

def battle(gym, trainer, entry_message=None):
    """
    Función general de batalla entre dos pokémons.
    Parámetros:
      - trainer: Enemigo.
      - gym: Gimnasio.
      - entry_message: Mensaje opcional para la entrada al gimnasio.
    """
    # Mostrar mensaje de entrada (ahora parametrizable)
    uim.message_fight_entry(gym, entry_message)
    gs.battle_flags["battle_won"] = False
    gs.battle_flags["battle_lost"] = False
    gs.battle_flags["battle_ongoing"] = True

    while gs.battle_flags["battle_ongoing"]:
        # Turno del jugador (si tiene suficiente HP)
        if gs.user.pokemons[0].hp > 0:
            player_turn(trainer)

        # Comprobar si el enemigo fue derrotado
        verify_battle_outcome(trainer)

        # Turno del enemigo (si tiene suficiente HP)
        if trainer.pokemons[0].hp > 0:
            enemy_turn(trainer)

        # Comprobar nuevamente si el jugador fue derrotado
        verify_battle_outcome(trainer)

def handle_gym_battle(gym, trainer, flag_key, hp_range, damage_incr, level_incr, entry_message=None):
    """
    Maneja la batalla de un gimnasio.
    
    Parámetros:
      - gym: objeto del gimnasio con atributos x e y.
      - trainer: entrenador que contiene su lista de pokémons.
      - flag_key: clave para actualizar gs.gym_flags.
      - hp_range: tupla para aumentar max_hp al ganar.
      - damage_incr: incremento de daño al ganar.
      - level_incr: incremento de nivel al ganar.
      - entry_message: mensaje opcional para la entrada al gimnasio.
      
    Retorna:
      - "win", "lose", "exit" o None si no se ejecuta la batalla.
    """
    # Verificar posición y flag
    pos_x, pos_y = 0, 1
    if gym.x == gs.user_position[pos_x] and gym.y == gs.user_position[pos_y] and not gs.gym_flags[flag_key]:
        battle(gym, trainer, entry_message)

        if gs.battle_flags["battle_won"]:
            gs.user.pokemons[0].max_hp += random.randint(hp_range[0], hp_range[1])
            gs.user.pokemons[0].damage += damage_incr
            gs.user.pokemons[0].level += level_incr

            gs.gym_flags[flag_key] = True
            gs.message_flags["victory_shown"] = True

        elif gs.battle_flags["battle_lost"]:
            gs.message_flags["defeat_shown"] = True