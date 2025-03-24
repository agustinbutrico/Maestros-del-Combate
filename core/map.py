import random
import data.game_state as gs
import ui.messages as uim

def obstacles_creation():
    obstacles = []
    for _ in range(gs.MAP_HEIGHT):
        current_row = ""
        current_width = 0
        while current_width < gs.MAP_WIDTH:
            possible_obstacles = [",,,", ",,", " "]
            weights = [2, 3, 95]
            obstacle = random.choices(possible_obstacles, weights=weights, k=1)[0]
            
            # Check if the obstacle fits in the remaining width
            if current_width + len(obstacle) > gs.MAP_WIDTH:
                # If the obstacle doesn't fit, fill with a space
                current_row += " "
                current_width += 1
            else:
                current_row += obstacle
                current_width += len(obstacle)
        # Appends the current row to the grid
        obstacles.append(list(current_row))
    # Saves the map with same dimentions with obstacles
    gs.obstacles = obstacles

def locations_creation(location_types):
    """
    Genera ubicaciones usando gs.user_position, gs.obstacles, gs.MAP_WIDTH y gs.MAP_HEIGHT.
    Para los gimnasios, se espera que la tupla tenga 4 elementos: (name, icon, type_, Gym).
    Para hospitales, se esperan 3 elementos: (name, icon, Hospital).
      
    Cada vez que se crea una instancia (Gym u Hospital), sus constructores
    se encargan de validarla e incorporarla a las listas globales correspondientes.
    """
    generated_coords = []  # Para llevar el control de las coordenadas ya generadas
    limiter = 0
    
    while limiter < len(location_types):
        new_location = [random.randint(0, gs.MAP_WIDTH - 1), random.randint(0, gs.MAP_HEIGHT - 1)]
        pos_x, pos_y = new_location[0], new_location[1]
        
        # Verificar que la ubicación sea válida:
        # - No se haya generado antes.
        # - No coincida con la posición del usuario.
        # - No haya un obstáculo (el caracter en gs.obstacles no es ",")
        if (new_location not in generated_coords and
            new_location != gs.user_position and
            gs.obstacles[pos_y][pos_x] != ","):
            
            generated_coords.append(new_location)
            data = location_types[limiter]
            
            if len(data) == 5:  # Caso para Gym: (name, icon, type_, Gym)
                name, icon, alias, gym_type, location_class = data
                try:
                    location_class(name, icon, pos_x, pos_y, alias, gym_type)
                except ValueError as e:
                    continue
            else:  # Caso para Hospital: (name, icon, Hospital)
                name, icon, location_class = data
                try:
                    location_class(name, icon, pos_x, pos_y)
                except ValueError as e:
                    continue
            
            limiter += 1

def start_location_selection(trainer):
    user_input = ""
    while user_input not in ["1", "2", "3", "4"]:
        user_start_position = ""
        user_input = input(uim.message_start_location_selection())

        match user_input:
            case "1": # Norte
                user_start_position = [
                    random.randint(0, gs.MAP_WIDTH - 1), random.randint(0, round(gs.MAP_HEIGHT - ((gs.MAP_HEIGHT - 1) / 1.5))),
                ]
            case "2": # Sur
                user_start_position = [
                    random.randint(0, gs.MAP_WIDTH - 1), random.randint(round((gs.MAP_HEIGHT + 1) / 1.5), gs.MAP_HEIGHT - 1),
                ]
            case "3": # Este
                user_start_position = [
                    random.randint(round((gs.MAP_WIDTH + 1) / 1.5), gs.MAP_WIDTH - 1), random.randint(0, gs.MAP_HEIGHT - 1),
                ]
            case "4": # Oeste
                user_start_position = [
                    random.randint(0, round(gs.MAP_WIDTH - ((gs.MAP_WIDTH - 1) / 1.5))), random.randint(0, gs.MAP_HEIGHT - 1),
                ]
        if user_start_position is not None:
            gs.user_position = user_start_position