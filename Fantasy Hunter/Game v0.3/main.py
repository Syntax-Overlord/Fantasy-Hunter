import skills as sk
import items as itm
import classes as c
import random as rd
import datetime as dt
import math

playerData = {}

def creation_Of_Player(details):
    global playerData
    stats = c.classes[details["class"]]["stats"]
    
    playerData = {
        "name": details["name"],
        "class": c.classes[details["class"]]["name"],
        "stats": stats,
        "equipment": details["equipments"],
        "hp": int(stats["str"] * 5) + int(stats["end"] * 10),
        "mana": int(stats["int"] * 10) + int(stats["char"] * 2)
    }
