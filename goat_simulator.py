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

"""
	3 verschiedene Starter-Ziegen:
		Steve: Penner-Look, schielt, kaugummikauend, mehr Glück im Casino
		Elvira: feine Dame, top gestyled, Dauerrabatt in der Boutique, Charm hat Effekt auf NPCs
		Patchy: Flicken-Fell, Propeller-Mütze, Profi-Dreck-Wühler und besonders gut im collectables finden
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
	 |			  |		   /	\				   |
 Boutiquen		  |	  Museum   Schwimmbad		Casino
	 		   /	\			 	|
			Imbiss  Kino	  Kanalisation						
"""

# ----------------------------------------------------------------------------------------
# World data
# ----------------------------------------------------------------------------------------


places = {
 
	"Zuhause": {					# quasi home base. pennen, ziege anpassen, achievements checken,...
		"name": "Zuhause",
		"connections": ["Marktplatz"],
		"actions": {

			"schlafen": {			# resettet vllt negative statuseffekte etc
				"text": "foo",
			},

			"Kleiderschrank": {
				"text": "miau",		# braucht multiple choices
			},

			"Sammlungen": {
				"text": "arff",		# braucht multiple choices, zb achievements, collectables,...
			}

		}
	},

	"Marktplatz": {
		"name": "Marktplatz",
		"connections": ["Zuhause", "Einkaufszentrum", "Bahnhof", "Park"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"Einkaufszentrum": {
		"name": "Einkaufszentrum",
		"connections": ["Marktplatz", "Erdgeschoss", "1. Stock"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"Bahnhof": {
		"name": "Bahnhof",
		"connections": ["Marktplatz", "Farm", "Schwarzmarkt"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"Erdgeschoss": {
		"name": "Erdgeschoss",
		"connections": ["Einkaufszentrum", "1. Stock", "Boutiquen"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"1. Stock": {
		"name": "1. Stock",
		"connections": ["Einkaufszentrum", "Erdgeschoss", "Imbiss", "Kino"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"Park": {
		"name": "Park",
		"connections": ["Marktplatz", "Museum", "Schwimmbad"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"Farm": {
		"name": "Farm",
		"connections": ["Bahnhof", "Park", "Schwarzmarkt"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"Schwarzmarkt": {				# hier gibts nen dealer, obviously. also iwie shop integ
		"name": "Schwarzmarkt",
		"connections": ["Bahnhof", "Farm", "Casino"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"Boutiquen": {					# hier gibts shops. items, custemization,...
		"name": "Boutiquen",
		"connections": ["Erdgeschoss"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"Museum": {						# hier werden die collectables ausgestellt
		"name": "Museum",
		"connections": ["Park"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	
	},

	"Schwimmbad": {
		"name": "Schwimmbad",
		"connections": ["Park", "Kanalisation"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},

	"Casino": {
		"name": "Casino",
		"connections": ["Schwarzmarkt"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	
	"Imbiss": {						# hier gibts food 
		"name": "Imbiss",
		"connections": ["1. Stock"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"Kino": {
		"name": "Kino",
		"connections": ["1. Stock"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	},
	
	"Kanalisation": {
		"name": "Kanalisation",
		"connections": ["Schwimmbad"],
		"actions": {

			"rammen": {
				"text": "foo",
				"chaos_gain": 5		# muss irgendwie je nach ziel variieren
			},

			"lecken": {
				"text": "miau",
				"chaos_gain": 3		# muss irgendwie je nach ziel variieren
			},

			"meckern": {
				"text": "arff",
				"chaos_gain": 1 	# muss irgendwie je nach ziel variieren
			}

		}
	}
} 


# ----------------------------------------------------------------------------------------
# Player data
# ----------------------------------------------------------------------------------------


current_place = "Zuhause"
inventory = []
chaos = 0

while True:
	
	print("Standort:", current_place)
	print("Chaos-Level:", chaos)
	print("Inventar:", inventory)


	print("\nMögliche Ziele:")

	for destination in places[current_place]["connections"]:
		print("-", destination)
	
	choice = input("\nWohin möchtest du gehen?")

	if choice in places[current_place]["connections"]:
		current_place = choice
		print("Du gehst zu", choice)
		print("Neuer Standort:", current_place)
	else:
		print(f"[!]'{choice}' ist kein gültiges Ziel, bääh!")