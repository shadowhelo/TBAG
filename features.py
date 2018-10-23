"""This is where "features" are stored. Features are objects and structures
in the game world that the player interacts with, but do not fit the 
defintion of "item" as they would never enter the player's inventory.
id and name both aid in identification of the feature, description briefly
describes it, and use will do something, once the feature is acted upon 
appropriately.
"""

feature_bookcase = { 
	"id": "bookcase",
	
	"name": "The bookcase",

	"description":  "An old oaken bookcase, it was once very fine indeed, but now it is wearing away."
}

feature_dragon = {
        "id": "dragon",

        "name": "The dragon",

        "description": "A giant fucking dragon."
}

feature_donkey = {
        "id": "donkey",

        "name": "The donkey",

        "description": "Looks like a bit of an ass"
}

feature_wall_text = {
	"id": "wall_text",

	"name": "text on wall",

	"description": "\nInscribed on the wall is a block of text saying, \n" + """"I HINT AT WHICH BOOK TO PICKUP." """

}