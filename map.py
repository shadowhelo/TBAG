from items import *

room_death = {
    "name":"",

    "description":
    """
    You Die, You Die, You Die!
    """
}

room_credits = {
    "name":""

    "description":
    """
    Credits
    """
}

room_main_menu = {
    "name": "",

    "description":
    """
    You emerge from a dense forest into a large clearing, upon the rise infront of you stands a
    forboding castle made of a dark stone. The castles 

    you walk towards the castle when a wizened old man calls you from behind.

    Kirill apprears (magic poof?)
    Gives you task to go to the castle and do something(decide end quest goal)

    Do you accept the quest ? (yes or no, no closes the game)
    
    Kirill gives clue/reference to how to solve the bridge ?        
    """,

    "exits": {"north": "Courtyard"}

    "items": []
}

room_courtyard = {

    "name": "Courtyard",

    "description":
    """
    You arrive at the edge of the castle grounds, three paths lie before you;
    
    There is a path to that leads to the castle from the west of you made of yellow bricks.
    There is a path to the north of you that has a small white dog bounding down infront of you.
    There is a path to the east that curves towards the castle which has a pair of red shoes part way down it.  
    """,

    "exits": {"west": "Castle_Gates", "north": "Death", "east": "Death"}

    "items": []
}

room_castle_gates = {

    "name": "Castle Gates",

    "description":
    """
    Here lies a gate ....
    """,

    "exits": {"north": "Great_Hall"}

    "items": []
}

room_great_hall = {

    "name": "The Great Hall",

    "description":
    """
    Here is the great hall....
    """,

    "exits": {"south": "Great_Hall", "north": "Final_Room", "east": "Dungeon", "west": "Throne_Room", "south" }

    "items": []

}

rooms = {
    "Death": room_death,
    "Courtyard": room_courtyard,
    "Castle_Gates": room_castle_gates,
    "Great_Hall": room_great_hall,
}
