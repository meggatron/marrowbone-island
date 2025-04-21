#algorithims
#debugging

import random
import time

print("You disembark from a ferry onto Marrowbone Island.")
name = input("What is your name, adventurer? > ")
print(f"Welcome, {name}. Your quest begins now...")

weather = ["foggy", "rainy", "sunny"]
inventory = []
current_location = 'dock'

while True:
    if current_location == 'dock':
        print(f"\nYou are on a {random.choice(weather)} dock. Paths lead north to a trail.")
        move = input("Where do you go? > ").lower()
        if move == "go north" or move == "north":
            current_location = 'trail'
        else:
            print("Try typing 'go north' or just 'north'.")

    elif current_location == 'trail':
        print("\nYou begin walking up the trail.")
        for step in range(1, 6):
            print(f"Step {step}...")
            time.sleep(0.5)
        print(f"You are on a {random.choice(weather)} trail. Paths lead west into a forest or south back to the dock.")
        move = input("Where do you go? > ").lower()
        if move == "go west" or move == "west":
            current_location = 'forest'
        elif move == "go south" or move == "south":
            current_location = 'dock'
        else:
            print("Try 'west' or 'south'.")

    elif current_location == 'forest':
        print(f"\nYou step into a {random.choice(weather)} forest. The trees are thick and quiet.")
        if "map" not in inventory:
            take = input("You find a crumpled old map. Take it? (yes/no) > ").lower()
            if take == "yes":
                inventory.append("map")
                print("You take the map and tuck it into your coat.")
            else:
                print("You leave the map in the tree hollow.")
        else:
            print("You've already taken the map. There's nothing else here.")

        print("\nYour inventory contains:")
        for item in inventory:
            print("-", item)

        move = input("You can go east to return to the trail. Where do you go? > ").lower()
        if move == "go east" or move == "east":
            current_location = 'trail'
        else:
            print("Try typing 'east'.")
