from items import *

room_death = {
    "name":"",

    "description":
    """You Die, You Die, You Die!
    """
}

room_credits = {
    "name":"",

    "description":
    """Credits
    """
}      

room_courtyard = {

    "name": "Courtyard",

    "description":
    """Here lies some castle gates....""",

    "exits": {"north": "Great_Hall"},

    "items": []
}

room_castle_grounds = {

    "name": "Castle Grounds",

    "description":
    """You arrive at the edge of the castle grounds, three paths lie before you;

There is a path to that leads to the castle from the west of you made of yellow bricks.

There is a path to the north of you that has a small white dog bounding down infront of you.

There is a path to the east that curves towards the castle which has a pair of red shoes part way down it. 
    """,

    "exits": {"west": "Courtyard", "north": "Courtyard", "east": "Courtyard"},

    "items": []
}

room_great_hall = {

    "name": "The Great Hall",

    "description":
    """Here is the great hall....    """,

    "exits": {"south": "Courtyard", "north": "Final_Room", "east": "Dungeon", "west": "Throne_Room"},

    "items": []

}

room_throne_room = {
    
    "name": "Throne Room",

    "description":
    """Here is the throne room....    """,

    "exits": {"west": "Great_Hall"},

    "items": []
}

room_dungeon = {

    "name": "Dungeon",

    "description":
    """Here is the dungeon....    """,

    "exits": {"east": "Great_Hall", "south": "Credits" },

    "items": []
}

rooms = {
    "Death": room_death,
    "Courtyard": room_courtyard,
    "Castle_Grounds": room_castle_grounds,
    "Great_Hall": room_great_hall,
    "Throne_Room": room_throne_room,
    "Dungeon": room_dungeon,
    "Credits": room_credits
}
