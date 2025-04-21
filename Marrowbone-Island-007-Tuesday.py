#read
#write

import random
import time

weather = ["foggy", "rainy", "sunny"]
inventory = []

# Read intro text from file
def intro():
    with open("intro.txt", "r") as f:
        for line in f:
            print(line.strip())
    name = input("What is your name, adventurer? > ")
    print(f"Welcome, {name}. Your quest begins now...")
    return name

# Append each room visit to a log file
def log_room(location):
    with open("log.txt", "a") as log:
        log.write(f"Entered {location}\n")

def dock():
    log_room("dock")
    print(f"\nYou are on a {random.choice(weather)} dock. Paths lead north to a trail.")
    move = input("Where do you go? > ").lower()
    if move == "go north" or move == "north":
        return 'trail'
    else:
        print("Try typing 'go north' or just 'north'.")
        return 'dock'

def trail():
    log_room("trail")
    print("\nYou begin walking up the trail.")
    for step in range(1, 4):
        print(f"Step {step}...")
        time.sleep(0.5)
    print(f"You are on a {random.choice(weather)} trail. Paths lead west into a forest or south back to the dock.")
    move = input("Where do you go? > ").lower()
    if move == "go west" or move == "west":
        return 'forest'
    elif move == "go south" or move == "south":
        return 'dock'
    else:
        print("Try 'west' or 'south'.")
        return 'trail'

def forest():
    log_room("forest")
    print(f"\nYou step into a {random.choice(weather)} forest. The trees are thick and mossy.")
    if "map" not in inventory:
        take = input("You find a crumpled old map. Take it? (yes/no) > ").lower()
        if take == "yes":
            inventory.append("map")
            print("You take the map and tuck it into your coat.")
        else:
            print("You leave the map in the tree hollow.")
    else:
        print("The forest is quiet. You've already taken the map.")

    print("You can go east to return to the trail.")
    move = input("Where do you go? > ").lower()
    if move == "go east" or move == "east":
        return 'trail'
    else:
        print("Try typing 'east'.")
        return 'forest'

# Dictionary of location names mapped to functions
locations = {
    'dock': dock,
    'trail': trail,
    'forest': forest
}

# Start the game
player_name = intro()
current_location = 'dock'

while True:
    current_location = locations[current_location]()
