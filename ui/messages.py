import core.utils as cu

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
    message = (
        f"{enemy.name} {enemy.hp} HP\n{cu.message_life_indicator(enemy)}\n\n"
        f"{attacker.name} {attacker.hp} HP\n{cu.message_life_indicator(attacker)}\n\n"
        f"{attacker.name}'s LVL {attacker.level}\n\n"
        f"{attacker.name}'s Damage: {attacker.damage}\n\n"
    )
    return message
