from game_logic import intro, dock, trail, forest, tidepools, cave, cliff, boathouse

inventory = []
name = intro()  # <--- this is the line that should trigger the name prompt
current_location = 'dock'

locations = {
    'dock': dock,
    'trail': trail,
    'forest': forest,
    'tidepools': tidepools,
    'cave': cave,
    'cliff': cliff,
    'boathouse': boathouse
}

while current_location != 'end':
    current_location = locations[current_location]()
