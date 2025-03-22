import random
from data.game_state import MAP_HEIGHT, MAP_WIDTH

def obstacles_creation():
    obstacles = []
    for _ in range(MAP_HEIGHT):
        current_row = ""
        current_width = 0
        while current_width < MAP_WIDTH:
            possible_obstacles = [",,,", ",,", " "]
            weights = [2, 3, 95]
            obstacle = random.choices(possible_obstacles, weights=weights, k=1)[0]
            
            # Check if the obstacle fits in the remaining width
            if current_width + len(obstacle) > MAP_WIDTH:
                # If the obstacle doesn't fit, fill with a space
                current_row += " "
                current_width += 1
            else:
                current_row += obstacle
                current_width += len(obstacle)
        # Appends the current row to the grid
        obstacles.append(list(current_row))
    # returns the map with same dimentions with obstacles
    return obstacles
