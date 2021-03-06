from items import *
from features import *

room_death = {
    "name":"Courtyard",

    "description":
    """
____    ____  ______    __    __      _______   __   _______  _______      __
\   \  /   / /  __  \  |  |  |  |    |       \ |  | |   ____||       \    |  |
 \   \/   / |  |  |  | |  |  |  |    |  .--.  ||  | |  |__   |  .--.  |   |  |
  \_    _/  |  |  |  | |  |  |  |    |  |  |  ||  | |   __|  |  |  |  |   |  |
    |  |    |  `--'  | |  `--'  |    |  '--'  ||  | |  |____ |  '--'  |   |__|
    |__|     \______/   \______/     |_______/ |__| |_______||_______/    (__)

    """,

    "exits": {},

    "items": [],

    "features": []
}

room_chamber = {
    "name":"Small Chamber",

    "description":
    """A very small room adjacent to the dungeon.""",

    "exits": {"north": "Dungeon"},

    "items": [item_potion],

    "features": []
}

room_courtyard = {

    "name": "Courtyard",

    "description":
    """You have crossed the moat, into the coutryard. Rising above you to the north is the castle wall.
Its parapets loom overhead, its murder holes glare out at you as if eyes of a great beast.
The courtyard you stand in, however is a beautiful garden, with blooming flowers. The
courtyard has clearly not been maintained in some time, as thegrass brushes up above your
ankles and the bushes are an unruly mess. Despite this, the beauty of the flowering plants,
and the deep, dark reflecting pool in front of the great door cannot be denied.""",

    "exits": {"north": "Great_Hall"},

    "items": [],

    "features": []
}

room_castle_grounds = {

    "name": "Castle Grounds",

    "description": """You arrive at the edge of the castle grounds, three paths lie before you;
There is a path to that leads to the castle from the west of you made of yellow bricks.
There is a path to the north of you that Toto is bounding down.
There is a path to the east that curves towards the castle which has a pair of red shoes
part way down it.

Choose your path wisely, death awaits those unfortunate to stray down the wrong path""",

    "exits": {"west": "Courtyard", "north": "Death", "east": "Death"},

    "items": [],

    "features": []
}

room_great_hall = {

    "name": "Great Hall",

    "description":
    """You are now standing at the entrance of the great hall. As you look around you notice
that it is lit by thousands and thousands of floating candles, as you look upward
you see a velvety black ceiling dotted with stars, it looks as though the great
hall was the gate way to heaven. To your West there is a doorway with a staircase
leading down, to your East there is a door and to the North there is another door,
but it is locked.""",

    "exits": {"south": "Courtyard", "north": "Tower", "west": "Dungeon", "east": "Throne_Room"},

    "items": [],

    "features": []
}


room_throne_room = {

    "name": "Throne Room",

    "description":
    """As you enter the Throne Room in front of you is a large stone table with
numerous symbols etched into the side of it. In the corner of the room there is
a rather large and familiar wardrobe, the wardrobe is ajar and inside
you can see at least 10 big fur coats.""",

    "exits": {"west": "Great_Hall"},

    "items": [item_sword],

    "features": []
}

room_dungeon = {

    "name": "Dungeon",

    "description":
    """You make your way down a dark spiraling staircase, into a dimly lit room. The air
here is dense and much cooler. Its suspiciously quiet; you can hear the rising
and falling of your own breath. You feel the warmth emanating from a single
torch hanging from the ceiling. By the torch, black text is sloppily painted on
the wall "Supreme excellence consists of breaking the enemy's resistance without fighting".
You accidentally kick a pile of books lying on the floor and a cloud of dust forms.
Moving towards the farthest corner, you can hear a distant clock ticking.""",

    "exits": {"east": "Great_Hall", "south": "Chamber" },

    "items": [item_book1, item_book2, item_book3, item_book4, item_book5, item_book6, item_book7],

    "features": [feature_bookcase, feature_rusty_gate]
}

room_tower = {

    "name": "Tower",

    "description":
    """As you enter the highest room of the tallest tower the hot smokey air fills your lungs.
The heat dries the moisture in your eyes, blurring your vision. As you look up from
the burnt stone floor you see a plethora of skeletons; the remains of the people that
have tried before.

The ground shakes and a hot gust of air blows you back. Towering over you is the terrible
fire breathing dragon that has guarded the Arkenstone for many years. Wrapped in its tail
is an annoying donkey.""",

    "exits": {"south": "Great_Hall"},

    "items": [],

    "features": [feature_dragon, feature_donkey]
}


rooms = {
    "Death": room_death,
    "Courtyard": room_courtyard,
    "Castle_Grounds": room_castle_grounds,
    "Great_Hall": room_great_hall,
    "Throne_Room": room_throne_room,
    "Dungeon": room_dungeon,
    "Tower" : room_tower,
    "Chamber": room_chamber
}
