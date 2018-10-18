from items import *

room_castle_grounds = {
    "name": "Castle Grounds",

    "description":
    """
    You are in the grounds of a large castle.

    Kirill apprears (magic poof?)
    Gives you task to go to the castle and do something(decide end quest goal)
    
    Kirill gives clue to how to solve the bridge ?    
    """,

    "exits": {"north": "Bridge"}

    "items": []
}

room_bridge = {

    "name": "Moat Bridge",

    "description":
    """
    Here lies a bridge ....
    """,

    "exits": {"south": "Grounds", "north": "Castle_Gates"}

    "items": []
}

room_castle_gates = {

    "name": "Castle Gates",

    "description":
    """
    Here lies a gate ....
    """,

    "exits": {"south": "bridge", "north": "Main_Hall"}

    "items": []
}

rooms = {
    "Grounds": room_castle_grounds,
    "Bridge": room_bridge,
    "Castle_Gates": room_castle_gates,
    "Main_Hall": room_main_hall,
}
