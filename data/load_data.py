import random

import data.game_state as gs
import core.pokemons as cp
import locations.base as loc
from core import map
from trainers.base import Trainer

def load_obstacles():
    map.obstacles_creation()

def load_locations():
    location_types = [
        ("Rock Gym", " R", "Pewter Rock", "Roca", loc.Gym),
        ("Water Gym", " W", "Cerulean Water", "Agua", loc.Gym),
        ("Electric Gym", " E", "Vermilion Electric", "Electrico",loc.Gym),
        ("Fighting Gym", " F", "Cianwood Fighting", "Lucha", loc.Gym),
        ("Hospital 1", " H", loc.Hospital),
        ("Hospital 2", " H", loc.Hospital),
    ]
    map.locations_creation(location_types)
    # Los constructores de Gym y Hospital agregan las instancias a game_state.gyms, game_state.hospitals y game_state.locations

def load_trainers():
    # Crear entrenadores y asignarlos a sus respectivos gimnasios
    trainer_user = Trainer("User")
    trainer_brock = Trainer("Brock")
    trainer_misty = Trainer("Misty")
    trainer_ltsurge = Trainer("Lt. Surge")
    trainer_sabrina = Trainer("Sabrina")
    
    new_trainers = [trainer_brock, trainer_misty, trainer_ltsurge, trainer_sabrina]
    
    # Asignar entrenadores a los gimnasios correspondientes (usando referencias del estado global)
    for gym in gs.gyms:
        if gym.type_ == "Roca":
            gym.add_trainer(trainer_brock)
        elif gym.type_ == "Agua":
            gym.add_trainer(trainer_misty)
        elif gym.type_ == "Eléctrico":
            gym.add_trainer(trainer_ltsurge)
        elif gym.type_ == "Lucha":
            gym.add_trainer(trainer_sabrina)
    
    # Agregar todos los entrenadores al estado global
    gs.trainers.extend(new_trainers)
    gs.user = trainer_user

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

    for trainer in gs.trainers:
        if trainer.name == "User":
            continue  # No asignamos Pokémon al "User"
        
        # Determinar el tipo preferido en función del gimnasio del entrenador (si tiene)
        preferred_type = trainer.gym.type_ if trainer.gym is not None else None
        
        num_pokemons = random.choices(options, weights=weights, k=1)[0]
        for _ in range(num_pokemons):
            # Se pasa el preferred_type si está disponible, de lo contrario se genera sin sesgo
            pokemon = cp.create_random_pokemon(preferred_type=preferred_type)
            trainer.add_pokemon(pokemon)

def load_user_pokemon(species):
    """
    Genera un Pokémon de la especie especificada y lo asigna al entrenador "User".

    Parámetros:
      - species (str): la especie del Pokémon a generar.
    """
    # Genera el Pokémon usando la función especializada
    pokemon = cp.create_pokemon_by_species(species)
    # Asigna el Pokémon al usuario (suponiendo que game_state.user ya fue inicializado)
    gs.user.add_pokemon(pokemon)

def load_data():
    # Función central para precargar todos los datos del juego.
    load_obstacles()
    load_locations()
    load_trainers()
    load_trainers_pokemons()
    load_user_pokemon("Pikachu")
