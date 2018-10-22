#!/usr/bin/python3
import time

from map import rooms
from player import *
from items import *
from gameparser import *

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """
    items_return = []

    for i in items:
        items_return.append(i["name"])

    return ', '.join(items_return)


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

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
    You have id card, laptop, money.
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

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()

    # Display room items
    print_room_items(room)

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


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
        print("TAKE " + str(i["id"]).upper() + " to take " + i["name"])

    for i in inv_items:
        print("DROP " + str(i["id"]).upper() + " to drop your " + i["name"])

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
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
    if (is_valid_exit(current_room["exits"], direction) == True):
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

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

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

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    True

    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]

def castle_grounds():

    return

def courtyard():
    print("At first the door seems dark, like a great mouth of some form of massive stony beast, but shortly it begins to glow. Slowly you can make out letters appearing, as if etched in moonlight upon the oaken door:")

    print("This thing all things devours:")
    time.sleep(1)
    print("Birds, beasts, trees, flowers;")
    time.sleep(1)
    print("Gnaws iron, bites steel;")
    time.sleep(1)
    print("Grinds hard stones to meal;")
    time.sleep(1)
    print("Slays king, ruins town,")
    time.sleep(1)
    print("And beats high mountain down.")
    time.sleep(1)
    print("Name this thing, and enter.")

    riddle_solved = False

    while riddle_solved == False:
        user_input = input("> ")
        normalise_input(user_input)
        user_input = ''.join(user_input).lower()

        if user_input == "time":
            riddle_solved = True
        
    return



# This is the entry point of our program
def main():

    global player_name
    
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
    
    print()
    print("You emerge from a dense forest into a large clearing, upon the rise in front of you stands a of you is a forboding castle made of a dark stone. The castles..." + "\n")
    print("You start walk towards the castle when a wizened man in flowing blue robes calls you from behind. You walk over to the man and he asks of your name.")
    print("You reply by saying your name is")

    player_name=""
    while player_name == "":    
        player_name = input("")
        player_name = normalise_input(player_name)
        player_name = ''.join(player_name)

    print("Ahh, so it is you after all " + player_name + """. You have come finally, as it was fortold many years ago that you would be the one to....""")

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
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        #interupts here to ensure loop works correctly
        if current_room["name"] == "Courtyard":
            courtyard()

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
   main()
