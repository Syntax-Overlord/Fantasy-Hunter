import random

#data
skills = {
    # Warrior Skills
    101: ("Power Strike", "A powerful blow dealing massive physical damage."),
    102: ("Shield Block", "Reduces incoming damage with a well-timed block."),
    103: ("War Cry", "Boosts allies' attack power with a fierce shout."),
    104: ("Berserk", "Increases attack power but lowers defense temporarily."),
    105: ("Charge", "Rushes to the enemy, dealing impact damage."),
    106: ("Iron Will", "Temporarily reduces damage taken by sheer determination."),
    107: ("Whirlwind", "Spins with weapon, hitting multiple enemies around."),
    108: ("Earth Shatter", "Smashes the ground, dealing area damage."),
    109: ("Defensive Stance", "Increases defense but reduces movement speed."),
    110: ("Raging Slash", "Unleashes a flurry of rapid, powerful strikes."),
    111: ("Slash","Basic Slashing"),
    112: ("Dodge","Escaping an attack"),
    113: ("Stab","Basic stabbing"),
    114: ("Block","Basic Blocking"),
    115: ("Parry","Redirecting an attack"),
    # Mage Skills
    201: ("Fireball", "Launches a flaming projectile dealing burn damage."),
    202: ("Ice Spike", "Summons icicles that pierce enemies, slowing them."),
    203: ("Magic Shield", "Creates a barrier that absorbs magical damage."),
    204: ("Arcane Blast", "Unleashes concentrated magical energy, dealing massive damage"),
    205: ("Teleport", "Instantly moves to a nearby location."),
    206: ("Mana Drain", "Absorbs enemy mana to replenish your own."),
    207: ("Lightning Bolt", "Strikes with electricity, possibly stunning targets."),
    208: ("Meteor Shower", "Summons meteors to rain down on enemies."),
    209: ("Time Warp", "Slows down enemies within a specific area."),
    210: ("Mana Burst", "Expends mana to release a powerful area attack."),
    # Rogue Skills
    301: ("Backstab", "Deals increased damage when attacking from behind."),
    302: ("Shadow Step", "Quickly dashes to avoid enemy attacks."),
    303: ("Poison Blade", "Applies poison, dealing damage over time."),
    304: ("Smoke Bomb", "Conceals area, increasing evasion temporarily."),
    305: ("Sneak Attack", "High-damage attack when undetected by enemies."),
    306: ("Evasion", "Increases dodge rate for a short duration."),
    307: ("Critical Strike", "Guaranteed critical hit on the next attack."),
    308: ("Shadow Clone", "Creates a decoy to distract enemies."),
    309: ("Swift Strike", "Rapid attack with increased critical hit chance."),
    310: ("Assassinate", "Instantly kills weaker enemies from stealth."),
    # Cleric Skills
    401: ("Heal", "Restores health to an ally or self."),
    402: ("Holy Light", "Damages undead and heals allies in the area."),
    403: ("Divine Shield", "Grants temporary invincibility from all damage."),
    404: ("Blessing", "Boosts ally attack or defense for a short time."),
    405: ("Revive", "Brings a fallen ally back to life."),
    406: ("Purify", "Removes negative status effects from allies."),
    407: ("Mana Infusion", "Restores an ally's or own mana."),
    408: ("Smite", "Holy attack dealing damage to dark creatures."),
    409: ("Protection Aura", "Reduces damage taken by allies within range."),
    410: ("Holy Nova", "Deals area damage and heals allies nearby."),
    # Archer Skills
    501: ("Piercing Arrow", "Shoots an arrow that penetrates multiple enemies."),
    502: ("Multi-Shot", "Fires several arrows at once in a spread."),
    503: ("Sniper Shot", "High accuracy, long-range attack with increased critical chance."),
    504: ("Explosive Arrow", "Arrow explodes on impact, dealing area damage."),
    505: ("Rapid Fire", "Unleashes a rapid barrage of arrows."),
    506: ("Poison Arrow", "Applies poison, damaging target over time."),
    507: ("Hawk Eye", "Increases accuracy and critical hit rate."),
    508: ("Wind Step", "Increases movement speed and evasion temporarily."),
    509: ("Trap Mastery", "Deploys traps that immobilize or damage enemies."),
    510: ("Rain of Arrows", "Rains arrows over a wide area, damaging all."),
}
jobs = ["warrior","mage","rogue","cleric","archer"]
default_skills_ = {"warrior" : [skills[111][0],
                                skills[112][0],
                                skills[113][0],
                                skills[114][0],
                                skills[115][0]],
                   "mage"     : [skills[201][0],
                                skills[202][0],
                                skills[203][0],
                                skills[204][0]],
                   "rogue"    : [skills[111][0],
                                skills[112][0],
                                skills[113][0],
                                skills[301][0],
                                skills[307][0]],
                   "cleric"   : [skills[401][0],
                                skills[406][0],
                                skills[409][0]],
                   "archer"   : [skills[501][0],
                                skills[502][0],
                                skills[307][0]]
                   }
genders = ["male","female","other"]
stats = {"might" : 0,           #Strength
         "agility" : 0,         #Dexterity
         "constitution" : 0,    #Constitution
         "intellect" : 0,       #Intelligence
         "insight" : 0,         #Wisdom
         "presence" : 0}        #Charisma
gold = 1000
level = 1
exp = {"current" : 10,
       "need" : 100}
title = []

#functions
def verification(str1,str2):
    """Verify if the entered job/gender is correct or not"""
    while True:
        user = input(": ").lower()
        if user in str2:
            str1 = user
            break
        else:
            if str2 == genders:
                print("\033[3mThe stars whisper many names, but none recognize what you have spoken. Choose again, traveler.\033[0m")
            elif str2 == jobs:
                print("\033[3mLegends tell of mighty warriors, cunning rogues, and mystical mages… but never of what you have spoken. Try again, adventurer!\033[0m")
    return str1

def numeric_verification(str1):
    while True:
        user = int(input("\033[3m-: \033[0m"))
        try:
            str1 = int(user)
            break
        except ValueError:
            print("By the ancient laws, choose your path wisely (1 or 2 only!)")
    return str1

def statistics(int1):
    if int1 == 1:
        for i in stats:
            stats[i] = random.randint(1,9)
    elif int1 == 2:
        for i in stats:
            while True:
                user = int(input("\033[3mChoose Wisely(1-9): \033[0m"))
                try:
                    if 1 <= user < 10:
                        stats[i] = user
                        break
                    else:
                        print("By the ancient laws, choose your path wisely(1-9 only!)")
                except ValueError:
                    print("By the ancient laws, choose your path wisely (1 or 9 only!)")
    return stats

def level_up():
    global level
    global exp
    if exp["current"] >= exp["need"]:
        exp["current"] -= exp["need"]
        exp["need"] += exp["need"]
        level += 1
    return exp,level

#Game
print("____________________________________________________________________________________________________________________________________________________________________________________")
print("Version - Beta 0.2\t                                                          Welcome to Fantasy Hunter!")
print("____________________________________________________________________________________________________________________________________________________________________________________")
print("\n\033[3mIn the realm of legends, where magic reigns and monsters lurk, your story is forged in battle!\n"
      "Embark on an epic text-based adventure, master powerful skills, and carve your destiny in Fantasy Hunter,\n"
      "where every choice shapes the legend you become!\033[0m")

#Credentials
name = input("\n\033[3mA name is the first whisper of a legend…"
             "\nTell me, wanderer, what shall the bards sing of you?: \033[0m")
family = input("\n\033[3mEvery hunter carries a legacy. What surname shall be etched into the annals of history?: \033[0m")
print("-----------------------------------------------------------------------------------------------------------------")
print("\033[3mLegends care not for form, only for strength. How shall the world know you?\n"
               "(Male/Female/Other) \033[0m",end="")
gender = verification("",genders)
print("-----------------------------------------------------------------------------------------------------------------")
print("\033[3mThe path before you forks into destiny.\nWill you be a blade in the shadows, a master of the arcane, or something beyond imagination?\033[0m"
            "\n - Warrior"
            "\n - Mage"
            "\n - Rogue"
            "\n - Cleric"
            "\n - Archer"
            "\n -",end="")
job = verification("",jobs)
print("-----------------------------------------------------------------------------------------------------------------")
choice = ""
print("\033[3mWill you weave your own power from strength and wisdom... "
      "or trust the mystic winds of fate?\n"
      "1. Let fate decide!\n"
      "2. I will write my own destiny!\n"
      "Choice\033[0m",end="")
choice = numeric_verification(choice)
statistics(choice)

#_______________________________________________________________________________________________________________________
a = default_skills_[job]
status = (f"\t    Status"
          f"\nName:   {name} {family}"
          f"\nGender: {gender}"
          f"\nLevel:  {level}"
          f"\nClass:  {job}"
          f"\nTitle:  {", ".join(title)}"
          f"\n\nStats:-"
          f"\n -Might         {stats['might']}"
          f"\n -Agility       {stats['agility']}"
          f"\n -Constitution  {stats['constitution']}"
          f"\n -Intellect     {stats['intellect']}"
          f"\n -Insight       {stats['insight']}"
          f"\n -Presence      {stats['presence']}"
          f"\n\nSkills:-"
          f"\n {" ".join(f'- {i}\n' for i in a)}"
          )
#_______________________________________________________________________________________________________________________

print("-----------------------------------------------------------------------------------------------------------------")
print(f"\033[3mYou are {name} {family}, a spirited youth hailing from New Lake, a secluded, serene village cradled with in the lush\n"
      f"countryside of the 'Valorian Empire' — a realm celebrated far and wide for its unparalleled mastery of the combat arts.\n\n"
      f"Yet, within you burns an insatiable thirst for adventure, a yearning to break free from the tranquil confines of\n"
      f"your homeland. With unwavering resolve, you embark upon a perilous journey across the vast and treacherous Continent,\n"
      f"a land where legends are born and destinies are forged.\n\n"
      f"Before your departure, your parents—bearing the wisdom of those who have seen much—implored you to join the\n"
      f"Adventurer's Guild, a prestigious organization that governs the spoils of those bold enough to challenge the\n"
      f"monstrous creatures lurking beyond civilization's reach. Here, adventurers find not only financial support\n"
      f"but also the arms and knowledge needed to survive the trials that await.\n\n"
      f"After days of relentless travel, you stand before the towering gates of 'Battlecrest', the illustrious capital city\n"
      f"famed for its elite warriors and legendary training grounds, where heroes are tempered in the crucible of battle.\n"
      f"In this grand city, amidst the echoes of valor and glory, you make a choice that will forever shape your destiny,\n"
      f"you register as a job at the Adventurer's Guild.\n\n"
      f"Your path lies before you, shrouded in mystery and danger. Will you rise to become the strongest warrior the\n"
      f"world has ever known? Will you carve your own destiny against the currents of fate? Or perhaps, you will etch\n"
      f"your name into the annals of history, leaving behind a legacy that endures through the ages.\n\n"
      f"The stage is set, the world awaits your mark.\n"
      f"Your adventure begins now!\33[0m")
print("\n-----------------------------------------------------------------------------------------------------------------")
print(status)
