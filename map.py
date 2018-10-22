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
    """You have crossed the moat, into the coutryard. Rising above you to the north is the castle wall. Its parapets 
    
    loom overhead, its murder holes glare out at you as if eyes of a great beast. The courtyard you stand in, however 
    
    is a beautiful garden, with blooming flowers. The courtyard has clearly not been maintained in some time, as the
    
    grass brushes up above your ankles and the bushes are an unruly mess. Despite this, the beauty of the flowering
    
    plants, and the deep, dark reflecting pool in front of the great door cannot be denied.

    At first the door seems dark, like a great mouth of some form of massive stony beast, but shortly it begins to 
    
    glow. Slowly you can make out letters appearing, as if etched in moonlight upon the oaken door:

    This thing all things devours:
    
    Birds, beasts, trees, flowers;
    
    Gnaws iron, bites steel;
    
    Grinds hard stones to meal;
    
    Slays king, ruins town,
    
        And beats high mountain down.
    
    Name this thing, and enter.""",

    "exits": {"north": "Great_Hall"},

    "items": []
}

room_castle_grounds = {

    "name": "Castle Grounds",

    "description": """
    You arrive at the edge of the castle grounds, three paths lie before you;

    There is a path to that leads to the castle from the west of you made of yellow bricks.

    There is a path to the north of you that has a small white dog bounding down infront of you.

    There is a path to the east that curves towards the castle which has a pair of red shoes part way down it. 
    """,

    "exits": {"west": "Courtyard", "north": "Courtyard", "east": "Courtyard"},

    "items": []
}

room_great_hall = {

    "name": "The Great Hall",

    "description": """
    You are now standing at the entrance of the great hall. As you look around the notice that it is
    
    lit by thousands and thousands of candles which are floating in mid-air, as you look upward you see a 
    
    velvety black ceiling dotted with stars, it looks as though the great hall was the gate way to heaven. 
    
    To your West there is a doorway with a staircase leading down, to your East there is a door and to the North 
    
    there is another door, but it is locked.""",

    "exits": {"south": "Courtyard", "north": "Tower", "east": "Dungeon", "west": "Throne_Room"},

    "items": []

 

room_throne_room = {
    
    "name": "Throne Room",

    "description":
    """As you enter the Throne Room in front of you is a large stone table with numerous symbols etched 
    
    into the side of it. Laying motionless on the table was a beautiful golden coloured Lion, as you move closer 
    
    to the table you see a sword protruding from the belly of this magnificent beast. In the corner of the room 
    
    there is a rather large and familiar wardrobe, the wardrobe is slightly open and inside you can see at least 
    
    10 big fur coats. """,

    "exits": {"west": "Great_Hall"},

    "items": []
}

room_dungeon = {

    "name": "Dungeon",

    "description":
    """You make your way down a dark spiraling staircase, into a dimly lit room. The air here is dense and much cooler. 

    Its suspiciously quiet; you can hear the rising and falling of your own breath. You feel the warmth emanating from a 

    single torch hanging from the ceiling. By the torch, black text is sloppily painted on the wall. You accidentally kick 

    a pile of books lying on the floor and a cloud of dust forms. Moving towards the farthest corner, you can hear a distant 

    clock ticking. There you vaguely see an anxious rabbit in a waistcoat - gripping onto a golden pocket watch. He mutters “I’m 

    late, I’m late for a very important date”. The long hand on his clock face points at a bearing of 240, and the short hand 030. 

    There is a rusty gate to the south. The door then slams behind you, the clock has started, GO!""",

    "exits": {"east": "Great_Hall", "south": "Credits" },

    "items": []
}

room_tower = {
    
    "name" : "Tower"

    "description" : 
    """As you enter the final room the hot smokey air fills your lungs. The heat dries the moisture in 

    your eyes, blurring your vision. As you look up from the burnt stone floor you see a plethora of skeletons; the 

    remains of the people that have tried before. The ground shakes and a hot gust of air blows you back. Towering over 

    you is the grotesque scaley beast with dagger-like fangs and wings too small for its humongous body. 

    Wrapped in its tail is an annoying donkey.""",

    "exits": {"east": "Great_Hall", "south": "Credits" },

    "items": []
}


rooms = {
    "Death": room_death,
    "Moat": room_moat,
    "Courtyard": room_courtyard,
    "Castle_Grounds": room_castle_grounds,
    "Great_Hall": room_great_hall,
    "Throne_Room": room_throne_room,
    "Dungeon": room_dungeon,
    "Tower" : room_tower,
    "Credits": room_credits
}
