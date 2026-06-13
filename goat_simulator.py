# =======================================================================================
# Textbased Goat-Simulator in Python
# =======================================================================================


# ---------------------------------------------------------------------------------------
# Feature ideas
# ---------------------------------------------------------------------------------------


"""
	Map
	Secrets
	Quests
	Fähigkeiten
	Chaos-Level -> XP
	Achievements
	Collectables
	Freischaltbare Ziegen -> versch. Eigenschaften
	Tragbare Items mit Effekten
"""


# ----------------------------------------------------------------------------------------
# World map
# ----------------------------------------------------------------------------------------


MAP = """
						Weltname
							|
						 Zuhause
							|
	 Einkaufszentrum -- Marktplatz -- Bahnhof   
	 	/		\			|		   /	\
Erdgeschoss -- 1. Stock    Park  --  Farm -- Schwarzmarkt 
	 |			  |		   /	\
 Boutiquen		  |	  Museum   Schwimmbad
	 		   /	\			 	|
			Imbiss  Kino	  Kanalisation						
"""

# ----------------------------------------------------------------------------------------
# World data
# ----------------------------------------------------------------------------------------


places = {
 
    "Zuhause": {
		"name": "Zuhause",
    	"connections": ["Marktplatz"]
	},

	"Marktplatz": {
        "name": "Marktplatz",
        "connections": ["Zuhause", "Einkaufszentrum", "Bahnhof", "Park"]
	},
    
	"Einkaufszentrum": {
        "name": "Einkaufszentrum",
        "connections": ["Marktplatz", "Erdgeschoss", "1. Stock"]
	},
    
	"Bahnhof": {
        "name": "Bahnhof",
        "connections": ["Marktplatz", "Farm", "Schwarzmarkt"]
	},
    
	"Erdgeschoss": {
        "name": "Erdgeschoss",
        "connections": ["Einkaufszentrum", "1. Stock", "Boutiquen"]
	},
    
	"1. Stock": {
        "name": "1. Stock",
        "connections": ["Einkaufszentrum", "Erdgeschoss", "Imbiss", "Kino"]
	},
    
	"Park": {
        "name": "Park",
        "connections": ["Marktplatz", "Museum", "Schwimmbad"]
	},
    
	"Farm": {
        "name": "Farm",
        "connections": ["Bahnhof", "Park", "Schwarzmarkt"]
	},
    
	"Schwarzmarkt": {
        "name": "Schwarzmarkt",
		"connections": ["Bahnhof", "Farm"]
	},
    
	"Boutiquen": {
        "name": "Boutiquen",
        "connections": ["Erdgeschoss"]
	},
    
	"Museum": {
        "name": "Museum",
        "connections": ["Park"]
	},
    
	"Schwimmbad": {
		"name": "Schwimmbad",
        "connections": ["Park", "Kanalisation"]
	},
    
	"Imbiss": {
        "name": "Imbiss",
        "connections": ["1. Stock"]
	},
    
	"Kino": {
        "name": "Kino",
        "connections": ["1. Stock"]
	},
    
	"Kanalisation": {
        "name": "Kanalisation",
        "connections": ["Schwimmbad"]
	}
} 


# ----------------------------------------------------------------------------------------
# Player data
# ----------------------------------------------------------------------------------------

current_place = "Zuhause"
inventory = []
chaos = 0

print("Standort:", current_place)
print("Chaos-Level:", chaos)
print("Inventar:", inventory)

