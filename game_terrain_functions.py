import random

# get size of map
# randomize obstacles
#   make sure that obstacles don't overlap each other
# randomize spawn point
#   make sure spawn point isn't on top of obstacle

x_coords = []
y_coords = []


spawn_point = ""
obstacle_coords_list = []
def map_size():
    #separate user inputs with calculations later on
    x_length = int(input("How large do you want the map to be horizontally?"))
    y_length = int(input("How large do you want the map to be vertically?"))

    for counter in range(0, x_length + 1):
        x_coords.append(counter)
    for counter in range(0, y_length + 1):
        y_coords.append(counter)

    print(x_coords)
    print(y_coords)


def new_map_size():
    x_length = 15
    y_length = 15 

    for counter in range(0, x_length + 1):
        x_coords.append(counter)
    for counter in range(0, y_length + 1):
        y_coords.append(counter)
    
    return x_coords, y_coords

def get_obstacles():
    map_size()
    obstacles_number = int(input("How many obstacles would you like?"))

    for counter in range(0, obstacles_number):
        obstacle_x = random.randint(x_coords[0], x_coords[-1])
        obstacle_y = random.randint(y_coords[1], y_coords[-1])
        obstacle_coord = obstacle_x, obstacle_y
        obstacle_coords_list.append(obstacle_coord)
    
    print(obstacle_coords_list)

    

def potential_spawn():
    get_obstacles()

    spawn_x = random.randint(x_coords[0], x_coords[-1])
    spawn_y = random.randint(y_coords[1], y_coords[-1])

    spawn_point = spawn_x, spawn_y
    print(spawn_point)
    return spawn_point


# remove this part and make new loop
def spawn_check():
    potential_spawn()

    for coord in obstacle_coords_list:
        if coord == spawn_point:
            potential_spawn()
        else:
            break
    for coord in obstacle_coords_list:
        if coord == spawn_point:
            potential_spawn()
        else:
            break
    
    
    
spawn_check()
