#if statements
#logical operators
#for loop
#while loop
#lists
#solve a logic problem
#import external library

import random
import time

print("You disembark from a ferry onto Marrowbone Island.")
name = input("What is your name, adventurer? > ")
print(f"Welcome, {name}. Your quest begins now...")

weather = ["foggy", "rainy", "sunny"]

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
        for step in range(1, 4):
            print(f"Step {step}...")
            time.sleep(0.5)  # pause for half a second
        print(f"You are on a {random.choice(weather)} trail. You can return south to the dock.")
        move = input("Where do you go? > ").lower()
        if move == "go south" or move == "south":
            current_location = 'dock'
        else:
            print("Try typing 'go south' or just 'south'.")
