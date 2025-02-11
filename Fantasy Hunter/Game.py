import random
print("Welcome to Fantasy Hunter")
print("This game is still in development, but plan to release soon!")
print("This game is a text-based adventure game that mimics Fantasy adventure stories,\nyou will face monsters, have turn-based fights, you can explore the vast world of magic,\nlearn new skills, and more!")
print("Made by Laksh Chawla")
name = str(input("Let's start with your name: "))
family_name = str(input("What is your family name? "))
gender = str(input("Choose Your Gender: Male/Female: "))
job = str(input("Choose a job: Warrior/Mage/Rogue/Cleric/Archer: "))
status = 1 #Alive = 1
stats = str(input("Would you like to decide your character's stats yourself? Yes/No: "))
strength = 0
dexterity = 0
constitution = 0
intelligence = 0
wisdom = 0
charisma = 0
if stats == "Yes" or stats == "yes" or stats == "Y" or stats == "y":
    if gender == "Male" or gender == "M" or gender == "m":
        if job == "Warrior":
            print("Choose your stats:")
            strength = int(input("Strength(Physical Strength)(1-10):"))
            if strength >= 10:
                print("Please choose a value below 10 for Strength!")
            dexterity = int(input("Dexterity(Agility)(1-5):"))
            if dexterity > 5:
                print("Please choose a value below 6 for Dexterity!")
            constitution = int(input("Constitution(Health and Stamina(Stamina is not implemented yet)(1-10):"))
            if constitution >= 10:
                print("Please choose a value below 10 for Constitution!")
            intelligence = int(input("Intelligence(Ability to learn magic and skills)(1-5):"))
            if intelligence > 5:
                print("Please choose a value below 6 for Intelligence!")
            wisdom = int(input("Wisdom(The higher is it, the more choices you'll have(Max number of choices is 3)(1-5):"))
            if wisdom > 5:
                print("Please choose a value below 6 for Wisdom!")
            charisma = int(input("Charisma(Social skills and personality)(1-5):"))
            if charisma > 5:
                print("Please choose a value below 6 for Charisma!")
        if job == "Mage":
            print("Choose your stats:")
            strength = int(input("Strength(Physical Strength)(1-5):"))
            if strength > 5:
                print("Please choose a value below 6 for Strength!")
            dexterity = int(input("Dexterity(Agility)(1-5):"))
            if dexterity > 5:
                print("Please choose a value below 6 for Dexterity!")
            constitution = int(input("Constitution(Health and Stamina(Stamina is not implemented yet)(1-5):"))
            if constitution > 5:
                print("Please choose a value below 6 for Constitution!")
            intelligence = int(input("Intelligence(Ability to learn magic and skills)(1-10):"))
            if intelligence >= 10:
                print("Please choose a value below 10 for Intelligence!")
            wisdom = int(input("Wisdom(The higher is it, the more choices you'll have(Max number of choices is 3)(1-10):"))
            if wisdom >= 10:
                print("Please choose a value below 10 for Wisdom!")
            charisma = int(input("Charisma(Social skills and personality)(1-5):"))
            if charisma > 5:
                print("Please choose a value below 6 for Charisma!")
        if job == "Rogue":
            print("Choose your stats:")
            strength = int(input("Strength(Physical Strength)(1-5):"))
            if strength > 5:
                print("Please choose a value below 6 for Strength!")
            dexterity = int(input("Dexterity(Agility)(1-10):"))
            if dexterity >= 10:
                print("Please choose a value below 10 for Dexterity!")
            constitution = int(input("Constitution(Health and Stamina(Stamina is not implemented yet)(1-5):"))
            if constitution > 5:
                print("Please choose a value below 6 for Constitution!")
            intelligence = int(input("Intelligence(Ability to learn magic and skills)(1-10):"))
            if intelligence >= 10:
                print("Please choose a value below 10 for Intelligence!")
            wisdom = int(input("Wisdom(The higher is it, the more choices you'll have(Max number of choices is 3)(1-5):"))
            if wisdom > 5:
                print("Please choose a value below 6 for Wisdom!")
            charisma = int(input("Charisma(Social skills and personality)(1-10):"))
            if charisma >= 10:
                print("Please choose a value below 10 for Charisma!")
        if job == "Cleric":
            print("Choose your stats:")
            strength = int(input("Strength(Physical Strength)(1-5):"))
            if strength > 5:
                print("Please choose a value below 6 for Strength!")
            dexterity = int(input("Dexterity(Agility)(1-5):"))
            if dexterity > 5:
                print("Please choose a value below 6 for Dexterity!")
            constitution = int(input("Constitution(Health and Stamina(Stamina is not implemented yet)(1-5):"))
            if constitution > 5:
                print("Please choose a value below 6 for Constitution!")
            intelligence = int(input("Intelligence(Ability to learn magic and skills)(1-10):"))
            if intelligence >= 10:
                print("Please choose a value below 10 for Intelligence!")
            wisdom = int(input("Wisdom(The higher is it, the more choices you'll have(Max number of choices is 3)(1-10):"))
            if wisdom >= 10:
                print("Please choose a value below 10 for Wisdom!")
            charisma = int(input("Charisma(Social skills and personality)(1-10):"))
            if charisma >= 10:
                print("Please choose a value below 10 for Charisma!")
        if job == "Archer":
            print("Choose your stats:")
            strength = int(input("Strength(Physical Strength)(1-5):"))
            if strength > 5:
                print("Please choose a value below 6 for Strength!")
            dexterity = int(input("Dexterity(Agility)(1-10):"))
            if dexterity >= 10:
                print("Please choose a value below 10 for Dexterity!")
            constitution = int(input("Constitution(Health and Stamina(Stamina is not implemented yet)(1-5):"))
            if constitution > 5:
                print("Please choose a value below 6 for Constitution!")
            intelligence = int(input("Intelligence(Ability to learn magic and skills)(1-10):"))
            if intelligence >= 10:
                print("Please choose a value below 10 for Intelligence!")
            wisdom = int(input("Wisdom(The higher is it, the more choices you'll have(Max number of choices is 3)(1-10):"))
            if wisdom > 5:
                print("Please choose a value below 6 for Wisdom!")
            charisma = int(input("Charisma(Social skills and personality)(1-5):"))
            if charisma > 5:
                print("Please choose a value below 6 for Charisma!")
    elif gender == "Female" or gender == "F" or gender == "f":
        if job == "Warrior":
            print("Choose your stats:")
            strength = int(input("Strength(Physical Strength)(1-10):"))
            if strength >= 10:
                print("Please choose a value below 10 for Strength!")
            dexterity = int(input("Dexterity(Agility)(1-5):"))
            if dexterity > 5:
                print("Please choose a value below 6 for Dexterity!")
            constitution = int(input("Constitution(Health and Stamina(Stamina is not implemented yet)(1-10):"))
            if constitution >= 10:
                print("Please choose a value below 10 for Constitution!")
            intelligence = int(input("Intelligence(Ability to learn magic and skills)(1-5):"))
            if intelligence > 5:
                print("Please choose a value below 6 for Intelligence!")
            wisdom = int(input("Wisdom(The higher is it, the more choices you'll have(Max number of choices is 3)(1-5):"))
            if wisdom > 5:
                print("Please choose a value below 6 for Wisdom!")
            charisma = int(input("Charisma(Social skills and personality)(1-5):"))
            if charisma > 5:
                print("Please choose a value below 6 for Charisma!")
        if job == "Mage":
            print("Choose your stats:")
            strength = int(input("Strength(Physical Strength)(1-5):"))
            if strength > 5:
                print("Please choose a value below 6 for Strength!")
            dexterity = int(input("Dexterity(Agility)(1-5):"))
            if dexterity > 5:
                print("Please choose a value below 6 for Dexterity!")
            constitution = int(input("Constitution(Health and Stamina(Stamina is not implemented yet)(1-5):"))
            if constitution > 5:
                print("Please choose a value below 6 for Constitution!")
            intelligence = int(input("Intelligence(Ability to learn magic and skills)(1-10):"))
            if intelligence >= 10:
                print("Please choose a value below 10 for Intelligence!")
            wisdom = int(input("Wisdom(The higher is it, the more choices you'll have(Max number of choices is 3)(1-10):"))
            if wisdom >= 10:
                print("Please choose a value below 10 for Wisdom!")
            charisma = int(input("Charisma(Social skills and personality)(1-5):"))
            if charisma > 5:
                print("Please choose a value below 6 for Charisma!")
        if job == "Rogue":
            print("Choose your stats:")
            strength = int(input("Strength(Physical Strength)(1-5):"))
            if strength > 5:
                print("Please choose a value below 6 for Strength!")
            dexterity = int(input("Dexterity(Agility)(1-10):"))
            if dexterity >= 10:
                print("Please choose a value below 10 for Dexterity!")
            constitution = int(input("Constitution(Health and Stamina(Stamina is not implemented yet)(1-5):"))
            if constitution > 5:
                print("Please choose a value below 6 for Constitution!")
            intelligence = int(input("Intelligence(Ability to learn magic and skills)(1-10):"))
            if intelligence >= 10:
                print("Please choose a value below 10 for Intelligence!")
            wisdom = int(input("Wisdom(The higher is it, the more choices you'll have(Max number of choices is 3)(1-5):"))
            if wisdom > 5:
                print("Please choose a value below 6 for Wisdom!")
            charisma = int(input("Charisma(Social skills and personality)(1-10):"))
            if charisma >= 10:
                print("Please choose a value below 10 for Charisma!")
        if job == "Cleric":
            print("Choose your stats:")
            strength = int(input("Strength(Physical Strength)(1-5):"))
            if strength > 5:
                print("Please choose a value below 6 for Strength!")
            dexterity = int(input("Dexterity(Agility)(1-5):"))
            if dexterity > 5:
                print("Please choose a value below 6 for Dexterity!")
            constitution = int(input("Constitution(Health and Stamina(Stamina is not implemented yet)(1-5):"))
            if constitution > 5:
                print("Please choose a value below 6 for Constitution!")
            intelligence = int(input("Intelligence(Ability to learn magic and skills)(1-10):"))
            if intelligence >= 10:
                print("Please choose a value below 10 for Intelligence!")
            wisdom = int(input("Wisdom(The higher is it, the more choices you'll have(Max number of choices is 3)(1-10):"))
            if wisdom >= 10:
                print("Please choose a value below 10 for Wisdom!")
            charisma = int(input("Charisma(Social skills and personality)(1-10):"))
            if charisma >= 10:
                print("Please choose a value below 10 for Charisma!")
        if job == "Archer":
            print("Choose your stats:")
            strength = int(input("Strength(Physical Strength)(1-5):"))
            if strength > 5:
                print("Please choose a value below 6 for Strength!")
            dexterity = int(input("Dexterity(Agility)(1-10):"))
            if dexterity >= 10:
                print("Please choose a value below 10 for Dexterity!")
            constitution = int(input("Constitution(Health and Stamina(Stamina is not implemented yet)(1-5):"))
            if constitution > 5:
                print("Please choose a value below 6 for Constitution!")
            intelligence = int(input("Intelligence(Ability to learn magic and skills)(1-10):"))
            if intelligence >= 10:
                print("Please choose a value below 10 for Intelligence!")
            wisdom = int(input("Wisdom(The higher is it, the more choices you'll have(Max number of choices is 3)(1-10):"))
            if wisdom > 5:
                print("Please choose a value below 6 for Wisdom!")
            charisma = int(input("Charisma(Social skills and personality)(1-5):"))
            if charisma > 5:
                print("Please choose a value below 6 for Charisma!")
elif stats == "No" or stats == "no" or stats == "N" or stats == "n":
    if gender == "Male" or gender == "M" or gender == "m":
        if job == "Warrior":
            strength = random.randint(1, 9)
            dexterity = random.randint(1, 5)
            constitution = random.randint(1, 9)
            intelligence = random.randint(1, 5)
            wisdom = random.randint(1, 5)
            charisma = random.randint(1, 5)
        elif job == "Mage":
            strength = random.randint(1, 5)
            dexterity = random.randint(1, 5)
            constitution = random.randint(1, 5)
            intelligence = random.randint(1, 9)
            wisdom = random.randint(1, 9)
            charisma = random.randint(1, 5)
        elif job == "Rogue":
            strength = random.randint(1, 5)
            dexterity = random.randint(1, 9)
            constitution = random.randint(1, 5)
            intelligence = random.randint(1, 9)
            wisdom = random.randint(1, 5)
            charisma = random.randint(1, 9)
        elif job == "Cleric":
            strength = random.randint(1, 5)
            dexterity = random.randint(1, 5)
            constitution = random.randint(1, 5)
            intelligence = random.randint(1, 9)
            wisdom = random.randint(1, 9)
            charisma = random.randint(1, 9)
        elif job == "Archer":
            strength = random.randint(1, 5)
            dexterity = random.randint(1, 9)
            constitution = random.randint(1, 5)
            intelligence = random.randint(1, 9)
            wisdom = random.randint(1, 5)
            charisma = random.randint(1, 5)
    elif gender == "Female" or gender == "F" or gender == "f":
        if job == "Warrior":
            strength = random.randint(1, 9)
            dexterity = random.randint(1, 5)
            constitution = random.randint(1, 9)
            intelligence = random.randint(1, 5)
            wisdom = random.randint(1, 5)
            charisma = random.randint(1, 5)
        elif job == "Mage":
            strength = random.randint(1, 5)
            dexterity = random.randint(1, 5)
            constitution = random.randint(1, 5)
            intelligence = random.randint(1, 9)
            wisdom = random.randint(1, 9)
            charisma = random.randint(1, 5)
        elif job == "Rogue":
            strength = random.randint(1, 5)
            dexterity = random.randint(1, 9)
            constitution = random.randint(1, 5)
            intelligence = random.randint(1, 9)
            wisdom = random.randint(1, 5)
            charisma = random.randint(1, 9)
        elif job == "Cleric":
            strength = random.randint(1, 5)
            dexterity = random.randint(1, 5)
            constitution = random.randint(1, 5)
            intelligence = random.randint(1, 9)
            wisdom = random.randint(1, 9)
            charisma = random.randint(1, 9)
        elif job == "Archer":
            strength = random.randint(1, 5)
            dexterity = random.randint(1, 9)
            constitution = random.randint(1, 5)
            intelligence = random.randint(1, 9)
            wisdom = random.randint(1, 5)
            charisma = random.randint(1, 5)

print(" ")
print(f"You are {name} {family_name}, a young soul from New Lake, a quiet, remote town nestled in the countryside of the Valorian Empire—an empire renowned for its mastery of combat arts.\n"
      f"Fueled by a desire for adventure, you've set out on a journey across the vast and perilous Continent. Before departing, your parents urged you to join the Adventurer's Guild,\n"
      f"an organization that manages the spoils of those brave enough to face monsters, ensuring adventurers are supported financially and equipped for the dangers ahead.\n"
      f"After traveling for days, you finally reach Battlecrest, the capital city famed for its elite warriors and legendary training grounds.\n"
      f"Here, you decide to officially register at the Adventurer's Guild as a {job}, setting your sights on a future filled with endless possibilities.\n"
      f"This is the beginning of your journey—to become the strongest, forge your own path, or leave your mark on this world in any way you choose.\n"
      f"\nYour adventure starts now!")
if job == "Warrior":
    print(f"      \n"
          f"STATUS")
    print(f"Name: {name}\n"
      f"Job: {job}\n"
      f"Gender: {gender}\n"
      f"Statistics:\n"
      f" -Strength: {strength}\n"
      f" -Dexterity: {dexterity}\n"
      f" -Constitution: {constitution}\n"
      f" -Intelligence: {intelligence}\n"
      f" -Wisdom: {wisdom}\n"
      f" -Charisma: {charisma}\n"
      f" \n"
      f"Skills:\n"
      f" -Slash Lv.1\n"
      f" -Dodge Lv.1\n"
      f" -Stab Lv.1\n"
      f" -Lunge Lv.1\n"
      f" -Block Lv.1\n"
      f" -Parry Lv.1\n"
      f" -Headbutt Lv.1\n"
      f" -Kick Lv.1\n"
      f" -Punch Lv.1\n")
elif job == "Mage":
    print(f"      \n"
          f"STATUS")
    print(f"Name: {name}\n"
          f"Job: {job}\n"
          f"Gender: {gender}\n"
          f"Statistics:\n"
          f" -Strength: {strength}\n"
          f" -Dexterity: {dexterity}\n"
          f" -Constitution: {constitution}\n"
          f" -Intelligence: {intelligence}\n"
          f" -Wisdom: {wisdom}\n"
          f" -Charisma: {charisma}\n"
          f" \n"
          f"Skills:\n"
          f" -Fireball Lv.1\n"
          f" -Lightning Lv.1\n"
          f" -Cure Lv.1\n")
elif job == "Rogue":
    print(f"      \n"
          f"STATUS")
    print(f"Name: {name}\n"
          f"Job: {job}\n"
          f"Gender: {gender}\n"
          f"Statistics:\n"
          f" -Strength: {strength}\n"
          f" -Dexterity: {dexterity}\n"
          f" -Constitution: {constitution}\n"
          f" -Intelligence: {intelligence}\n"
          f" -Wisdom: {wisdom}\n"
          f" -Charisma: {charisma}\n"
          f" \n"
          f"Skills:\n"
          f" -Backstab Lv.1\n"
          f" -Ambush Lv.1\n"
          f" -Thief Lv.1\n"
          f" -Pickpocket Lv.1\n"
          f" -Stealth Lv.1\n"
          f" -Dodge Lv.1\n"
          f" -Block Lv.1\n"
          f" -Punch Lv.1\n"
          f" -Kick Lv.1\n")
elif job == "Cleric":
    print(f"      \n"
          f"STATUS")
    print(f"Name: {name}\n"
          f"Job: {job}\n"
          f"Gender: {gender}\n"
          f"Statistics:\n"
          f" -Strength: {strength}\n"
          f" -Dexterity: {dexterity}\n"
          f" -Constitution: {constitution}\n"
          f" -Intelligence: {intelligence}\n"
          f" -Wisdom: {wisdom}\n"
          f" -Charisma: {charisma}\n"
          f" \n"
          f"Skills:\n"
          f" -Heal Lv.1\n"
          f" -Prayer Lv.1\n"
          f" -Cure Lv.1\n"
          f" -Sanctuary Lv.1\n")
elif job == "Archer":
    print(f"      \n"
          f"STATUS")
    print(f"Name: {name}\n"
          f"Job: {job}\n"
          f"Gender: {gender}\n"
          f"Statistics:\n"
          f" -Strength: {strength}\n"
          f" -Dexterity: {dexterity}\n"
          f" -Constitution: {constitution}\n"
          f" -Intelligence: {intelligence}\n"
          f" -Wisdom: {wisdom}\n"
          f" -Charisma: {charisma}\n"
          f" \n"
          f"Skills:\n"
          f" -Bullseye Lv.1\n"
          f" -Wind Magic Lv.1\n"
          f" -Stealth Lv.1\n"
          f" -Block Lv.1\n"
          f" -Parry Lv.1\n"
          f" -Kick Lv.1\n"
          f" -Punch Lv.1\n"
          f" -Headbutt Lv.1\n")

print("   ")
choice = str(input("You are currently laying on the bed in thought of what to do:\n"
      "Choose:\n"
      "1. Get Up!\n"
      "2. Sleep."))
if intelligence > 3:
    if choice == "1" or choice == "Get Up!" or choice == "get up!" or choice == "Get up" or choice == "get up":
        print("You got up!\n"
              "Now what?\n"
              "1. Lay down on the bed.\n"
              "2. Go outside of the room.\n"
              "3. Read a book.\n")
        choice2 = str(input(""))
        if choice2 == "1" or choice2 == "Lay down on the bed." or choice2 == "lay down on the bed." or choice2 == "Lay down" or choice2 == "lay down" or choice2 == "Lay down on the bed" or choice2 == "lay down on the bed":
            print("You Slept\n"
                  "Next Day")
        elif choice2 == "2" or choice2 == "Go outside of the room." or choice2 == "go outside of the room." or choice2 == "Go outside" or choice2 == "go outside" or choice2 == "Go outside of the room" or choice2 == "go outside of the room":
            print("You went outside of the room.\n"
                  "You are now in the corridor of the Tavern\n"
                  "1. Go Back inside\n"
                  "2. Go to the lobby.\n")
        elif choice2 == "3" or choice2 == "Read a book." or choice2 == "read a book." or choice2 == "Read a book" or choice2 == "read a book" or choice2 == "Read a book" or choice2 == "read a book":
            print("You read a book.\n"
                  "It was a book about a Dragon.\n")
            xp = intelligence + 0.025
            print(f"Intelligence increased by:",xp)
            print("1. Read another book.\n"
                  "2. Leave the room.\n")
            choice3 = str(input(""))
            if choice3 == "1" or choice3 == "Read another book." or choice3 == "read another book." or choice3 == "Read another book" or choice3 == "read another book" or choice3 == "Read another book" or choice3 == "read another book":
                print("You read another book.\n"
                      "It was a book about a Dragon.\n"
                      "1. Read another book.\n")
                choice4 = str(input("Choose: "))
                if choice4 == "1" or choice4 == "Read another book." or choice4 == "read another book." or choice4 == "Read another book" or choice4 == "read another book" or choice4 == "Read another book" or choice4 == "read another book":
                    print("You read another book.\n"
                          "Now you are tired"
                )