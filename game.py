#!/usr/bin/python3
import time

from map import rooms
from player import *
from items import *
from gameparser import *
from credits import *

dungeon_locked = True
tower_locked = True
aslan_on_table = True
riddle_solved = False


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_sword, item_potion])
    'The Atlantean Sword, Amortentia Love Potion'

    >>> list_of_items([item_rusty_key])
    'Rusty Key'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_book1, item_book2])
    'Pride and Prejudice, Romeo and Juliet'

    """
    items_return = []

    for i in items:
        items_return.append(i["name"])

    return ', '.join(items_return)

def print_features(room, item):
    #prints the list of features in the room

    for f in room["features"]:
        print("Type " + f["id"].upper() + " to use " + item["name"] + " on " + f["name"])
    print()

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Chamber"])
    There is Amortentia Love Potion here.
    <BLANKLINE>

    >>> print_room_items(rooms["Throne_Room"])
    There is The Atlantean Sword here.
    <BLANKLINE>

    >>> print_room_items(rooms["Death"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """

    if not room["items"]:
        pass
    else:
        print("There is " + list_of_items(room["items"]) + " here.\n")


def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have Kirill's survival kit.
    <BLANKLINE>

    """
    item_list = list_of_items(items)

    if item_list == "":
        pass
    else:
        print("You have " + str(item_list) + ".\n")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Courtyard"])
    <BLANKLINE>
    COURTYARD
    <BLANKLINE>
    You have crossed the moat, into the coutryard. Rising above you to the north is the castle wall.
    Its parapets loom overhead, its murder holes glare out at you as if eyes of a great beast.
    The courtyard you stand in, however is a beautiful garden, with blooming flowers. The
    courtyard has clearly not been maintained in some time, as thegrass brushes up above your
    ankles and the bushes are an unruly mess. Despite this, the beauty of the flowering plants,
    and the deep, dark reflecting pool in front of the great door cannot be denied.
    <BLANKLINE>

    >>> print_room(rooms["Chamber"])
    <BLANKLINE>
    A SMALL CHAMBER
    <BLANKLINE>
    A very small room adjacent to the dungeon.
    <BLANKLINE>
    There is Amortentia Love Potion here.
    <BLANKLINE>

    
    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    global aslan_on_table
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    if current_room == rooms["Throne_Room"] and aslan_on_table == True:
        if inventory.count(item_sword) == 1:
            print("As you step back from pulling the sword from the lion, the table cracks in half and you notice he has disappeared from the table. When you turn to leave the room, he is stood behind you. He cries out “They always said you should never let your heart rule your head, but is it not better to have loved and lost than to have never loved at all… ” before hopping over the table and into the wardrobe.")
            aslan_on_table = False
        else:
            print("""Laying motionless on the table is a beautiful golden coloured Lion,
as you move closer to the table you see a sword protruding from the belly of this magnificent beast.

""")

    # Display room items
    print_room_items(room)

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Tower"]["exits"], "south")
    'The Great Hall'
    >>> exit_leads_to(rooms["Dungeon"]["exits"], "east")
    'The Great Hall'
    >>> exit_leads_to(rooms["Great_Hall"]["exits"], "north")
    'Tower'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to the <where it leads>.

    For example:
    >>> print_exit("east", "Great_Hall")
    GO EAST to the Great_Hall.
    >>> print_exit("south", "Courtyard")
    GO SOUTH to the Courtyard.
    """
    print("GO " + direction.upper() + " to the " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for i in room_items:
        print("TAKE " + str(i["id"]).upper() + " to take " + i["name"] + " from the " + i["location"] + ".")

    for i in inv_items:
        print("DROP, USE or INSPECT " + str(i["id"]).upper() + " to drop, use or inspect your " + i["name"] + ".")

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Tower"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Dungeon"]["exits"], "north")
    False
    >>> is_valid_exit(rooms["Throne_Room"]["exits"], "west")
    True
    >>> is_valid_exit(rooms["Throne_Room"]["exits"], "east")
    False
    >>> is_valid_exit(rooms["Great_Hall"]["exits"], "east")
    True
    >>> is_valid_exit(rooms["Great_Hall"]["exits"], "north")
    True
    """
    return chosen_exit in exits


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """

    global current_room
    if (current_room == rooms["Dungeon"] and dungeon_locked == True ):
        print("You are locked in.")
    elif (current_room == rooms["Great_Hall"] and tower_locked == True and direction == "north"):
        print("That door is locked, for now.")

    elif (current_room == rooms["Castle_Grounds"]) and (direction == "east" or direction == "north"):
        print("The stone beneath your feet feels unsteady, and then...")
        time.sleep(1)
        print("The floor gives out from underneath you, and you tumble into the water, cracking your head against the rocks.")
        time.sleep(2)
        current_room = move(current_room["exits"],direction)
    
    elif (is_valid_exit(current_room["exits"], direction) == True):
        current_room = move(current_room["exits"],direction)
    else:
        print("you cannot go there")


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    global inventory
    for i in current_room["items"]:
        if item_id == i["id"]:
            inventory.append(i)
            current_room["items"].remove(i)
            return
    print("You cannot take that.")


def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    global inventory
    for i in inventory:
        if item_id == i["id"]:
            current_room["items"].append(i)
            inventory.remove(i)
            return
    print("You cannot drop that.")

def execute_use(item_id):
    global current_room
    
    for i in inventory:
        if item_id == i["id"]:
            if i["id"] == "kit":
                print("You are overcome with a warm fuzzy feeling.\n")
                inventory.remove(i)
                return
            else:
                print("\nObjects in room that can be acted upon:")
                print_features(current_room, i)
                print("Use " + i["name"] + " on what?")
                feat = input("")
                feat = normalise_input(feat)
                for f in current_room["features"]:
                    if feat[0] == f["id"]:
                        print("You attempt to use " + i["name"] + " on " + f["name"] + ".\n")
                        return list([f,i])
            return
    print("You cannot use that.")

def execute_inspect(item_id):
    for i in inventory:
        if item_id == i["id"]:
            print(i["description"])
    return

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
        return

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
        return

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
        return

    elif command[0] == "use":
        if len(command) > 1:
            return execute_use(command[1])
        else:
            print("Use what?")

    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")
        return

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)
    
    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Chamber"]["exits"], "north") == rooms["Dungeon"]
    True
    >>> move(rooms["Dungeon"]["exits"], "south") == rooms["Chamber"]
    True

    >>> move(rooms["Great_Hall"]["exits"], "east") == rooms["Courtyard"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]

def dungeon():
    global dungeon_locked
    global inventory
    global current_room
    if dungeon_locked == True:
        print("There you vaguely see an anxious rabbit in a waistcoat - gripping onto a golden pocket watch. He mutters “I’m late, I’m late for a very important date, I'll miss my afternoon tea!”. The long hand on his clock face points at 9, and the short hand at 1. There is a rusty gate to the south. The door slams behind you!\n")
    while dungeon_locked == True:
        # Show the menu with possible actions and ask the player
        command = menu([], current_room["items"], inventory)

        # Execute the player's command
        use_list = execute_command(command)
        correct_book = "book3"
        try:
            if use_list[1]["id"] == correct_book and use_list[0]["id"] == "bookcase":
                    print("You place The Art of War upon the shelf of the bookcase. You hear the clink of metal on wood.\n")
                    inventory.remove(use_list[1])
                    current_room["items"].append(item_rusty_key)
                    print('"Oh no!" the rabbit shouts. "Time has nearly run out!" Curiously, the long hand on his clock face still points at 9, and the short hand at 1.\n')

            elif use_list[0]["id"] == "bookcase":
                    if use_list[1]["id"] == "key":
                        print("You place " + use_list[1]["name"] + " on the shelf of the bookcase. It begins to shake violently and " + use_list[1]["name"] + " flies into the air and burst into flame, and is quickly turned into a pile of dust.\n")
                        inventory.remove(use_list[1])
                        time.sleep(1)
                        print("You destoyed your only key out. You are doomed to waste away in this dark dungeon.")
                        time.sleep(2.5)
                        current_room = rooms["Death"]
                        break
                    elif use_list[1]["id"] == "sword" or use_list[1]["id"] == "potion":
                        print("You place " + use_list[1]["name"] + " on the shelf of the bookcase. It begins to shake violently and " + use_list[1]["name"] + " flies into the air and lands back in your hands.")
                    else:
                        print("You place " + use_list[1]["name"] + " on the shelf of the bookcase. It begins to shake violently and " + use_list[1]["name"] + " flies into the air and burst into flame, and is quickly turned into a pile of dust.\n")
                        inventory.remove(use_list[1])

            elif use_list[1]["id"] == "key" and use_list[0]["id"] == "gate":
                    print("You turn the key in the lock, but notice it does not rotate all the way. There are four numbers of some form of combination lock above the keyhole.")
                    print("What number do you input?")
                    combo = normalise_input(input("> "))
                    if combo[0] == "1345":
                        dungeon_locked = False
                        print("The key rotates completely, and you hear the latch on the gate open, revealing a small chamber. The room begins to shake and you hear the clicking of a latch behind. The door is open again!\n")
                        time.sleep(1.5)
                        break
                    else:
                        print("Nothing happens.")
        except:
            pass

    return

def courtyard():
    print("At first the door seems dark, like a great mouth of some form of massive stony beast, but shortly it begins to glow. Slowly you can make out letters appearing, as if etched in moonlight upon the oaken door:")

    print("\n\tThis thing all things devours:")
    #time.sleep(1)
    print("\tBirds, beasts, trees, flowers;")
    #time.sleep(1)
    print("\tGnaws iron, bites steel;")
    #time.sleep(1)
    print("\tGrinds hard stones to meal;")
    #time.sleep(1)
    print("\tSlays king, ruins town,")
    #time.sleep(1)
    print("\tAnd beats high mountain down.\n")
    #time.sleep(1)
    print("\tName this thing, and enter.")

    global riddle_solved
    global current_room
    guesses = 3
    while riddle_solved == False:
        print("\nYou have " + str(guesses) + " more attempts to solve this riddle.")
        user_input = input("> ")
        normalise_input(user_input)
        user_input = ''.join(user_input).lower()
        guesses -= 1
        
        if user_input == "time":
            riddle_solved = True
            print("The letters flicker once, twice, three times, and then... the door creaks open, beckoning inwards.")
            time.sleep(1.5)
        elif guesses < 1:
            current_room = rooms["Death"]
            print("The letters flicker once, and then... ")
            time.sleep(1)
            print("The ground opens up beneath you, and swallows you whole.")
            break
        else:
            print("The letters flicker once, and then... nothing.")

    return

def tower():
    global inventory
    global current_room
    while True:
        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        use_list = execute_command(command)

        try:
            if use_list[1]["id"] == "sword":
                if use_list[0]["id"] == "dragon":
                    print("You swing your mighty sword at the dragon's head.")
                    time.sleep(1)
                    print("The beast moves his head out of the way and snaps his teeth at you.")
                    time.sleep(1)
                    print("You sidestep, and thrust your blade into the throat of the creature.")
                    time.sleep(1)
                    print("You struggle under its great weight, but stand strong.")
                    time.sleep(1)
                    print("With roar of pain it finally collapses.")
                    time.sleep(1)
                    print("\nYou've done it.")
                    time.sleep(1)
                    print("You have slain the dragon.")
                    print("You look around, the donkey appears to have run off, and there is no sign of the fabled arkenstone.")
                    time.sleep(2.5)
                    victory()
                    break

                elif use_list[0]["id"] == "donkey":
                    print("With a single swing of your sword you take the head of the donkey clean off.")
                    time.sleep(1)
                    print("On the floor near the donkey's corpse you see it! The Arkenstone!")
                    time.sleep(1)
                    print("It is beautiful")
                    time.sleep(1)
                    print("You feel hot. Very hot. You are burning up.")
                    time.sleep(1)
                    print("To your right, you notice the angry dragon is breathing fire!")
                    time.sleep(1)
                    print("You are melting, it is over.")
                    time.sleep(2.5)
                    current_room = rooms["Death"]
                    break

            elif use_list[1]["id"] == "potion":
                if use_list[0]["id"] == "dragon":
                    print("You splash the potion on the dragon.")
                    time.sleep(1)
                    print("The dragon looks questioningly at the donkey, and then...")
                    time.sleep(1)
                    print("Its eyes soften and gaze lovingly at the donkey.")
                    time.sleep(1)
                    print("The donkey kicks something over to you, and the pair ignore you.")
                    time.sleep(1)
                    print("The object shines brilliantly, what is it?")
                    time.sleep(1)
                    print("It is the Arkenstone! It must be!")
                    time.sleep(2.5)
                    inventory.append(item_arkenstone)
                    victory()
                    break

                elif use_list[0]["id"] == "donkey":
                    print("You splash the potion on the donkey.")
                    time.sleep(1)
                    print("The donkey looks at you questioningly, and then...")
                    time.sleep(1)
                    print("Its eyes soften and seem filled with... love?")
                    time.sleep(1)
                    print("The donkey leaps on you in a fit of emotion.")
                    time.sleep(1)
                    print("The dragon looks displeased...")
                    time.sleep(1)
                    print("Its once red scales seem transformed to green.")
                    time.sleep(1)
                    print("It flashes its great claw at you, tearing you from pelvis to forehead.")
                    time.sleep(1)
                    print("It is over in a second.")
                    time.sleep(2.5)
                    current_room = rooms["Death"]
                    break

            elif use_list[1]["id"] == "key":
                print("It seems mildly irritated.\n")

            else:
                print("Nothing happens.\n")
        except:
            pass

def victory():
    #This function when executed, allows the player to experience the thrill of victory
    global inventory
    global player_name
    print()
    print("""
A sound like a thunderclap comes from behind you.
""")
    time.sleep(1)
    #Any player achieving victory will see this block of text
    print("""
You see again the wizened man in flowing blue robes. He looks at your handiwork.""")
    print('\t"Well done, ' + player_name + ', you have solved the little problem with the dragon."')
    print("""He smiles to himself, seemingly proud of his choice of champion.
    "But, the Arkenstone, do you have it?"
""")
    #Logic to determine whether or not the player achieved a complete victory, if they did the wizard is very pleased
    if inventory.count(item_arkenstone) == 1:
        print("""You hand the Arkenstone to the wizard.
    "Ha, well done. You truly are a great hero, and all without shedding an ounce of blood!"

            GAME OVER
""")
    else:
        print("""You have nothing to show the wizard.
    "Hmmph, a shame, you were so promising. I suppose I misinterpreted the prophecy."
The wizard walks away, shaking his head.

            GAME OVER
""")

# This is the entry point of our program
def main():

    #brings in global variables
    global player_name
    global inventory
    global tower_locked
    global riddle_solved
    global current_room
    global dungeon_locked

    #Printing intitial game screen
    print("""
  __  ___  __   ______    __   __       __          _______
 |  |/  / |  | |   _  \  |  | |  |     |  |        /       |    
 |  '  /  |  | |  |_)  | |  | |  |     |  |       |   (----`    
 |    <   |  | |      /  |  | |  |     |  |        \   \        
 |  .  \  |  | |  |\  \-.|  | |  `----.|  `----.----)   |       
 |__|\__\ |__| | _| `.__||__| |_______||_______|_______/        
 
  __  ___      ___          _______ __________  __       _______
 |  |/  /     /   \        /       |          ||  |     |   ____|
 |  '  /     /  ^  \      |   (----`---|  |---`|  |     |  |__
 |    <     /  /_\  \      \   \       |  |    |  |     |   __|
 |  .  \   /  _____  \ .----)   |      |  |    |  `----.|  |____
 |__|\__\ /__/     \__\|_______/       |__|    |_______||_______|
                    
""")

    try:
        input("Press enter to continue...")
    except SyntaxError:
        pass
    
    #Setting a player name
    print()
    print("You emerge from a dense forest into a large clearing, upon the rise in front of you stands a of you is a foreboding castle made of a dark stone that has crumbled from the icy winters. The castle walls stood tall but as the tower that protruded into the clouds it looked as though it never ended. As you scan over the imposing structure you notice some windows are shattered and all that remains are fragments of glass stuck in the frame. The colours in the stained glass glowed in the dim sunlight peeking through the clouds, making it obvious it once was beautiful." + "\n")
    print("You start walk towards the castle when a wizened man in flowing blue robes calls you from behind. You walk over to the man and he asks of your name.")
    print("You reply by saying your name is")

    player_name=""
    while player_name == "":
        player_name = input("")

    print("Ahh, so it is you after all " + player_name + """. You have come finally, as it was fortold many years ago that you would be the one to confront the dragon, and free us of his tyranny, and retrieve the Arkenstone.""")
    print()
    time.sleep(1)

    print("Do you accept this mighty quest?")

    user_input = ""
    exit_loop = False
    while exit_loop == False:
        print("Yes or No?")
        user_input = input()
        user_input = normalise_input(user_input)
        user_input = ''.join(user_input)
        if user_input == "yes":
            exit_loop = True
        elif user_input == "no":
                exit_loop = True

    if (user_input != "yes"):
        print("Alas, perhaps you are not the " + player_name + " I was looking for.")
        print("The wizened man in flowing blue robes walks back into the forest")
        return

    time.sleep(1)

    # Main game loop
    while True:

        #Check if the tower door should open
        if inventory.count(item_potion) + inventory.count(item_sword) == 2 and tower_locked == True:
            print("The entire castle shakes as if a great earthquake has come to tear it down. You hear a crash, echoing from the Great Hall\n")
            tower_locked = False
            time.sleep(3)

        #Check if player is dead
        if current_room == rooms["Death"]:
            print(rooms["Death"]["description"])
            time.sleep(4)
            print_credits()
            break

        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        #Checks special cases
        if current_room["name"] == "Courtyard" and riddle_solved == False:
            courtyard()
            continue
        elif current_room["name"] == "Dungeon" and dungeon_locked == True:
            dungeon()
            continue
        elif current_room["name"] == "Tower":
            tower()
            continue
            #if current_room == rooms["Death"]:
            #    print(rooms["Death"]["description"])
            #time.sleep(4)
            #print_credits()
            break

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
   main()
