#functions

import random
import time

weather = ["foggy", "rainy", "sunny"]
inventory = []

def intro():
    print("You disembark from a ferry onto Marrowbone Island.")
    name = input("What is your name, adventurer? > ")
    print(f"Welcome, {name}. Your quest begins now...")
    return name

def dock():
    print(f"\nYou are on a {random.choice(weather)} dock. Paths lead north to a trail.")
    move = input("Type 'north' to move. > ").lower()
    if move == "north":
        return 'trail'
    else:
        print("You can only type 'north' for now.")
        return 'dock'

def trail():
    print("\nYou begin walking up the trail.")
    print("Step 1...")
    time.sleep(0.5)
    print("Step 2...")
    time.sleep(0.5)
    print("Step 3...")
    time.sleep(0.5)
    print(f"You are on a {random.choice(weather)} trail. Paths lead west into a forest or south back to the dock.")
    move = input("Type 'west' or 'south'. > ").lower()
    if move == "west":
        return 'forest'
    elif move == "south":
        return 'dock'
    else:
        print("Type exactly 'west' or 'south'.")
        return 'trail'

def forest():
    print(f"\nYou step into a {random.choice(weather)} forest. The trees are thick and mossy.")
    if "map" not in inventory:
        take = input("You find a crumpled old map. Type 'yes' to take it. > ").lower()
        if take == "yes":
            inventory.append("map")
            print("You take the map and tuck it into your coat.")
        else:
            print("You leave the map in the tree hollow.")
    else:
        print("The forest is quiet. You've already taken the map.")

    print("You can go 'east' to return to the trail.")
    move = input("Type 'east' to return. > ").lower()
    if move == "east":
        return 'trail'
    else:
        print("You can only type 'east' for now.")
        return 'forest'

#start game
player_name = intro()
current_location = 'dock'

# main game loop (no dictionaries yet)
while True:
    if current_location == 'dock':
        current_location = dock()
    elif current_location == 'trail':
        current_location = trail()
    elif current_location == 'forest':
        current_location = forest()
    else:
        print("You seem to be lost... Ending game.")
        break
