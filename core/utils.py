def message_pokemon_attacks(pokemon):
    """
    Devuelve un mensaje con la lista de ataques del Pokémon,
    mostrando el número, nombre, daño, precisión y probabilidad crítica.
    """
    message = "Select your attack:\n\n"
    for index, attack in enumerate(pokemon.attacks, start=1):
        message += (
            f"{index}. {attack.name}\n"
            f"    {attack.damage} damage\n"
            f"    {round(attack.accuracy * 100)}% accuracy\n"
            f"    {round(attack.critical_chance * 100)}% critical chance\n\n"
        )
    return message


def message_battle_starts(attacker, enemy):
    print(
        f"{enemy.name} {enemy.hp} HP\n{message_life_indicator(enemy)}\n\n"
        f"{attacker.name} {attacker.hp} HP\n{message_life_indicator(attacker)}\n\n"
        f"{attacker.name}'s LVL {attacker.level}\n\n"
        f"{attacker.name}'s Damage: {attacker.damage}\n\n"
    )

def message_life_indicator(pokemon): # Health Bar
    """Retorna una barra de vida en formato texto basada en hp y max_hp."""
    if pokemon.hp >= 0:
        health_bar = int(pokemon.hp * 30 / pokemon.max_hp)
        health_bar_print = "[{}{}]".format("#" * health_bar, " " *(30 - health_bar))
    elif pokemon.hp < 0:
        health_bar = int(-1 *(pokemon.hp * 30 / pokemon.max_hp))
        health_bar_print = "[{}{}]".format(" " *(30 - health_bar), "/" * health_bar)
    return health_bar_print
