import random

import gyms.base as gyms
import trainers.base as trainers
from data import game_state, create_pokemons

def load_gyms():
    # Crear gimnasios y agregarlos al estado global
    rock_gym = gyms.Gym(name="Gimnasio Roca", type_="Roca", icon="R")
    water_gym = gyms.Gym(name="Gimnasio Agua", type_="Agua", icon="W")
    electric_gym = gyms.Gym(name="Gimnasio Eléctrico", type_="Eléctrico", icon="E")
    fighting_gym = gyms.Gym(name="Gimnasio Lucha", type_="Lucha", icon="F")
    
    new_gyms = [rock_gym, water_gym, electric_gym, fighting_gym]

    # Agregar todos los gimnacios al estado global
    game_state.gyms.extend(new_gyms)

def load_trainers():
    # Crear entrenadores y asignarlos a sus respectivos gimnasios
    trainer_user = trainers.Trainer("User")
    trainer_brock = trainers.Trainer("Brock")
    trainer_misty = trainers.Trainer("Misty")
    trainer_ltsurge = trainers.Trainer("Lt. Surge")
    trainer_sabrina = trainers.Trainer("Sabrina")
    
    new_trainers = [trainer_brock, trainer_misty, trainer_ltsurge, trainer_sabrina]
    
    # Asignar entrenadores a los gimnasios correspondientes (usando referencias del estado global)
    for gym in game_state.gyms:
        if gym.type == "Roca":
            gym.add_trainer(trainer_brock)
        elif gym.type == "Agua":
            gym.add_trainer(trainer_misty)
        elif gym.type == "Eléctrico":
            gym.add_trainer(trainer_ltsurge)
        elif gym.type == "Lucha":
            gym.add_trainer(trainer_sabrina)
    
    # Agregar todos los entrenadores al estado global
    game_state.trainers.extend(new_trainers)
    game_state.user = trainer_user

def load_trainers_pokemons():
    """
    Asigna a cada entrenador (excepto "User") entre 1 y 6 Pokémon,
    donde la probabilidad de tener más Pokémon disminuye en potencias de 2.
    Si el entrenador pertenece a un gimnasio, se usará el tipo del gimnasio
    para generar Pokémon con ese tipo preferido.
    """
    # Pesos para 1 a 6 Pokémon (1 Pokémon es el más común)
    weights = [1, 1/2, 1/4, 1/8, 1/16, 1/32]
    options = list(range(1, 7))

    for trainer in game_state.trainers:
        if trainer.name == "User":
            continue  # No asignamos Pokémon al "User"
        
        # Determinar el tipo preferido en función del gimnasio del entrenador (si tiene)
        preferred_type = trainer.gym.type if trainer.gym is not None else None
        
        num_pokemons = random.choices(options, weights=weights, k=1)[0]
        for _ in range(num_pokemons):
            # Se pasa el preferred_type si está disponible, de lo contrario se genera sin sesgo
            pokemon = create_pokemons.create_random_pokemon(preferred_type=preferred_type)
            trainer.add_pokemon(pokemon)

def load_user_pokemon(species):
    """
    Genera un Pokémon de la especie especificada y lo asigna al entrenador "User".

    Parámetros:
      - species (str): la especie del Pokémon a generar.
    """
    # Genera el Pokémon usando la función especializada
    pokemon = create_pokemons.create_pokemon_by_species(species)
    # Asigna el Pokémon al usuario (suponiendo que game_state.user ya fue inicializado)
    game_state.user.add_pokemon(pokemon)

def load_data():
    # Función central para precargar todos los datos del juego.
    load_gyms()
    load_trainers()
    load_trainers_pokemons()
    load_user_pokemon("Pikachu")
