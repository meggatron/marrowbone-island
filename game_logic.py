import random  # used for chance-based events like orca appearance

# global inventory to track items the player collects
inventory = []

# intro screen and name input
def intro():
    print("you disembark from a ferry onto marrowbone island, just north of seattle. rumor has it that a lost pirate treasure is buried here.")
    name = input("what is your name, adventurer? > ")
    print(f"welcome, {name}. your quest begins now...")
    return name

# dock location — starting point of the game
def dock():
    print("you stand on the old ferry dock. paths lead north to the trail, east to the tidepools, and west to a crumbling boathouse.")
    while True:
        move = input("where do you go? > ").lower()
        if move == "go north":
            return 'trail'
        elif move == "go east":
            return 'tidepools'
        elif move == "go west":
            return 'boathouse'
        else:
            print("try 'go north', 'go east', or 'go west'.")

# trail — the central path connecting multiple locations
def trail():
    print("a gravel trail winds through mossy trees. paths lead west to a forest grove, north toward a cliff, and south back to the dock.")
    while True:
        move = input("where do you go? > ").lower()
        if move == "go west":
            return 'forest'
        elif move == "go north":
            return 'cliff'
        elif move == "go south":
            return 'dock'
        else:
            print("try 'go west', 'go north', or 'go south'.")

# forest — contains a map item
def forest():
    print("you enter a silent grove. huge footprints are pressed into the mud. sasquatch? you spot a map tucked in a tree hollow.")
    if "map" not in inventory:
        take = input("take the map? (yes/no) > ").lower()
        if take == "yes":
            print("you take the map.")
            inventory.append("map")
        else:
            print("you leave it behind.")
    return 'trail'

# tidepools — randomized chance of finding a cave
def tidepools():
    print("you approach slippery tidepools. barnacles crunch underfoot.")
    if random.choice([True, False]):
        print("an orca surfaces nearby, startling you! it disappears with a splash.")
        print("among the rocks, you glimpse a cave entrance...")
        return 'cave'
    else:
        print("you find tidepools filled with sea stars and hermit crabs. nothing else here.")
        return 'dock'

# cave — contains a key item
def cave():
    print("you duck into a sea cave. a skeleton slumps in the corner beside a rusty key. the exit leads east to the cliff or south to the tidepools.")
    if "key" not in inventory:
        take = input("take the key? (yes/no) > ").lower()
        if take == "yes":
            print("you take the key.")
            inventory.append("key")
        else:
            print("you leave the key.")
    while True:
        move = input("where do you go? > ").lower()
        if move == "go east":
            return 'cliff'
        elif move == "go south":
            return 'tidepools'
        else:
            print("try 'go east' or 'go south'.")

# cliff — win condition is checked here
def cliff():
    print("you reach a wind-swept bluff. an ancient chest is buried in a hollow. you can go south back to the trail or west to the cave.")
    if "key" in inventory:
        print("you unlock the chest and discover the treasure of marrowbone island! you win!")
        return 'end'
    else:
        print("the chest is locked. maybe there's a key somewhere?")
    while True:
        move = input("where do you go? > ").lower()
        if move == "go south":
            return 'trail'
        elif move == "go west":
            return 'cave'
        else:
            print("try 'go south' or 'go west'.")

# boathouse — optional flavor area
def boathouse():
    print("you enter the crumbling boathouse. the floorboards creak underfoot. a broken canoe leans against the wall.")
    return 'dock'
