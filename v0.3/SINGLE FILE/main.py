import random as rd
import datetime as dt
import math


logo = r"""  ______      _   _ _______        _______     __  _    _ _    _ _   _ _______ ______ _____  
 |  ____/\   | \ | |__   __|/\    / ____\ \   / / | |  | | |  | | \ | |__   __|  ____|  __ \ 
 | |__ /  \  |  \| |  | |  /  \  | (___  \ \_/ /  | |__| | |  | |  \| |  | |  | |__  | |__) |
 |  __/ /\ \ | . ` |  | | / /\ \  \___ \  \   /   |  __  | |  | | . ` |  | |  |  __| |  _  / 
 | | / ____ \| |\  |  | |/ ____ \ ____) |  | |    | |  | | |__| | |\  |  | |  | |____| | \ \ 
 |_|/_/    \_\_| \_|  |_/_/    \_\_____/   |_|    |_|  |_|\____/|_| \_|  |_|  |______|_|  \_\
                                                                                             
                                                                                             """

# BASIC STARTING CLASSES
classes = {
    "C1": {
        "name": "warrior",
        "stats": {
            "str": 10,
            "int": 2,
            "dex": 5,
            "end": 8,
            "char": 4
        }
    },
    "C2": {
        "name": "mage",
        "stats": {
            "str": 2,
            "int": 10,
            "dex": 4,
            "end": 3,
            "char": 5
        }
    },
    "C3": {
        "name": "rogue",
        "stats": {
            "str": 4,
            "int": 3,
            "dex": 10,
            "end": 5,
            "char": 6
        }
    },
    "C4": {
        "name": "archer",
        "stats": {
            "str": 5,
            "int": 4,
            "dex": 9,
            "end": 6,
            "char": 4
        }
    },
    "C5": {
        "name": "priest",
        "stats": {
            "str": 3,
            "int": 8,
            "dex": 4,
            "end": 5,
            "char": 8
        }
    }
}

# BASIC STARTING GEAR
gear = {
    1001: {
        "name": "rusty sword",
        "attack": 5,
        "spaceTake": 1,
        "durability": 100,   
    },
    1002: {
        "name": "rusty staff",
        "attack": 0,
        "spaceTake": 1,
        "durability": 100  
    },
    1003: {
        "name": "rusty dagger",
        "attack": 8,
        "spaceTake": 1,
        "durability": 100
    },
    1004: {
        "name": "rusty bow",
        "attack": 0,
        "spaceTake": 1,
        "durability":100  
    }
}

skills = {
    101: {
        "name": "martial arts",
        "levels" : 0,
    },
    102: {
        "name": "swordsmanship",
        "level": 0
    },
    103: {
        "name": "magi control",
        "level": 0
    },
    104: {
        "name": "stealth",
        "level": 0
    },
    105: {
        "name": "aim",
        "level": 0
    },
    106: {
        "name": "heal",
        "level": 0
    }
}



playerData = {}
progress = 0
evil = 0
good = 0


# CREATE PLAYER STATUS -------------------------------------------------------------------------------------------------------------------------------------------------
def create_player(details):
    """CREATES THE PLAYER DATA USING THE DATABASES AND THE USER GIVEN DATA"""
    global playerData
    # Class, Name, equipments, gender
    stats = classes[details["class"]]["stats"]

    playerData = {
        "name": details["name"],
        "gender": details["gender"],
        "class": classes[details["class"]]["name"],
        "stats": stats,
        "equipment": [gear[details["equipments"]]["name"]],
        "hp": int(stats["str"] * 5) + int(stats["end"] * 10),
        "mana": int(stats["int"] * 10) + int(stats["char"] * 2),
        "level": 1,
    }


# GET INFORMATION FROM USER TO CREATE PLAYER STATUS ------------------------------------------------------------------------------------------------------------------
def get_info():
    """THIS IS USED TO GET DATA FROM THE USER TO MAKE THE IN GAME PLAYER PROFILE"""
    print()
    while True:
        gender = (
            input(
                "\x1b[3mBefore the threads of destiny are spun, tell me... do you walk the path as a son of steel or a daughter of light — or neither bound by such titles?\x1b[0m\n[Male/Female]: "
            )
            .lower()
            .strip()
        )
        if gender.isalpha() and gender.lower() in ["male", "female"]:
            gender = gender.title()
            break
        else:
            print("\x1b[3mThe stars refuse this command. Choose anew.\x1b[0m")
    print()
    name = (
        input(
            "\x1b[3mAnd what shall the bards call you in song and legend? Speak your name, brave one!\x1b[0m\n--> "
        )
        .strip()
        .lower()
    )
    print()
    while True:
        _class = (
            input(
                "\x1b[3mNow, choose the gift that calls to your spirit…\n"
                " -> To wield strength and steel with unyielding resolve - \x1b[0m\x1b[1mA Warrior\x1b[0m\x1b[3m\n"
                " -> To master the arcane and bend reality with your will - \x1b[0m\x1b[1mA Mage\x1b[0m\x1b[3m\n"
                " -> To strike from shadow, unseen and unstoppable - \x1b[0m\x1b[1mA Rogue\x1b[0m\x1b[3m\n"
                " -> To dance with the wind and strike with piercing grace - \x1b[0m\x1b[1mA Archer\x1b[0m\x1b[3m\n"
                " -> To mend the broken and command divine wrath - \x1b[0m\x1b[1mA Priest\x1b[0m\n"
                "[1,2,3,4,5]: "
            )
            .lower()
            .strip()
        )
        if _class.isdigit() and int(_class) in [1, 2, 3, 4, 5]:
            _class = "C" + _class
            break
        else:
            print("\x1b[3mThe stars refuse this command. Choose anew.\x1b[0m")
    if _class == "C1":
        equipment = 1001
    elif _class == "C2":
        equipment = 1002
    elif _class == "C3":
        equipment = 1003
    elif _class == "C4":
        equipment = 1004
    elif _class == "C5":
        equipment = 1002
    return {"name": name, "class": _class, "equipments": equipment, "gender": gender}


# INTRO TO THE GAME ---------------------------------------------------------------------------------------------------------------------------------------------------
def intro():
    """VERY INTRO OF THE GAME"""
    global playerData
    print(logo)
    print(
        "\x1b[3mIn the age before time, when stars whispered secrets and the winds spoke names long forgotten... a darkness sealed by five heroes begins to stir once more.\x1b[0m"
    )
    print("\x1b[3mA new soul awakens — forged by fate, shaped by choice.\x1b[0m")
    print("\x1b[3mThe world does not remember you yet... but it soon shall.\x1b[0m\n")
    while True:
        play = (
            input(
                "\x1b[3mChoose your path, O Seeker:\n1. Ascend\n2. Recall\n3. Depart\x1b[0m\n[1/2/3]: "
            )
            .lower()
            .strip()
        )
        if play.isdigit() and int(play) in [1, 2, 3]:
            play = int(play)
            break
        else:
            print("\x1b[3mThe stars refuse this command. Choose anew.\x1b[0m")
    if play == 1:
        create_player(get_info())
    else:
        print(
            "\x1b[3mLeaving so soon? Return stronger, and the world will await your legend.\x1b[0m"
        )
        return


# GENERATE STATUS WINDOW -----------------------------------------------------------------------------------------------------------------------------------------------
def get_status_window(data):
    """GENERATES A STATUS WINDOW USING THE GENERATED PLAYER DATA"""
    print(f"\n+------------------------------------+")
    print(f"  NAME: {data["name"].title()}")
    print(f"  Gender: {data["gender"].title()}")
    print(f"  Level: {data["level"]}")
    print(f"  CLASS: {data['class'].title()}")
    print(f"  HP: {data["hp"]}")
    print(f"  MANA: {data["mana"]}")
    print(f" ")
    print(f"  STATISTICS")
    print(f"    STRENGTH: {data["stats"]['str']}     DEXTERITY: {data["stats"]['dex']}")
    print(
        f"    INTELLIGENCE: {data["stats"]['int']}  ENDURANCE: {data["stats"]['end']}"
    )
    print(f"    CHARISMA: {data["stats"]['char']}")
    print(f" ")
    print(f"  EQUIPPED")
    for _ in data["equipment"]:
        print(f"  -> {_.title()}")
    print(f"+------------------------------------+\n")

# STORYLINE START ------------------------------------------------------------------------------------------------------------------------------------------------------
def story():
    """MAIN STORYLINE FUNCTION(I THINK)"""
    global playerData
    print("\n")

def autoQuest():
    """TODO"""

def main():
    """MAIN"""
    intro()
    get_status_window(playerData)
    story()

main()
