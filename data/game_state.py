import random

# Estado de los gimnasios (si la batalla en cada uno ya se realizó)
gym_flags = {
    "rock_completed": False,
    "water_completed": False,
    "electric_completed": False,
    "fighting_completed": False
}

# Indicadores para mostrar mensajes o acciones especiales:
message_flags = {
    "hospital_used": False,   # Si se ha activado la acción del hospital (restauración de HP)
    "victory_shown": False,   # Si se ha mostrado el mensaje de victoria en el gimnasio
    "defeat_shown": False     # Si se ha mostrado el mensaje de derrota en el gimnasio
}

# Otros estados globales
game_over = False

locations = []
gyms = []
hospitals = []
trainers = []
pokemons = []

obstacles = []

user = None
user_position = []

MAP_WIDTH = 20
MAP_HEIGHT = random.randint(MAP_WIDTH -5, MAP_WIDTH +10)
