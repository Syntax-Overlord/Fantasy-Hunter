import skills as sk
import items as itm
import classes as c
import random as rd
import datetime as dt
import math
import art

playerData = {}
progress = 0


# CREATE PLAYER STATUS -------------------------------------------------------------------------------------------------------------------------------------------------
def create_player(details):
    """CREATES THE PLAYER DATA USING THE DATABASES AND THE USER GIVEN DATA"""
    global playerData
    # Class, Name, equipments, gender
    stats = c.classes[details["class"]]["stats"]

    playerData = {
        "name": details["name"],
        "gender": details["gender"],
        "class": c.classes[details["class"]]["name"],
        "stats": stats,
        "equipment": [itm.gear[details["equipments"]]["name"]],
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
    print(art.logo)
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
    print(
        f"""\n+------------------------------------+
|   NAME: {data["name"].title().ljust(27)}|
|   Gender: {data["gender"].title().ljust(25)}|
|   Level: {str(data["level"]).ljust(26)}|
|   CLASS: {data['class'].title().ljust(26)}|
|   HP: {str(data["hp"]).ljust(29)}|
|   MANA: {str(data["mana"]).ljust(27)}|
|   STATISTICS{"".ljust(23)}|
|     STRENGTH: {str(data["stats"]['str']).ljust(21)}|
|     DEXTERITY: {str(data["stats"]['dex']).ljust(20)}|
|     INTELLIGENCE: {str(data["stats"]['int']).ljust(17)}|
|     ENDURANCE: {str(data["stats"]['end']).ljust(20)}|
|     CHARISMA: {str(data["stats"]['char']).ljust(21)}|
|{"".ljust(36)}|
|   EQUIPPED{"".ljust(25)}|"""
    )
    for _ in data["equipment"]:
        print(f"|  -> {_.title().ljust(31)}|")
    print(f"+------------------------------------+\n")


# STORYLINE START ------------------------------------------------------------------------------------------------------------------------------------------------------
def story():
    """MAIN STORYLINE FUNCTION(I THINK)"""
    global playerData
    print("\n")


def main():
    """MAIN"""
    intro()
    get_status_window(playerData)
    print(playerData)


main()
