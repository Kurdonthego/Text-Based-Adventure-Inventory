# Course: CS 30
# Period: 3
# Date created: Ocotober 2nd, 2021
# Date modified: October 18th, 2021
# Name: Zana Osman
# Description: Inventory System for Text-Based Adventure
import sys

# Starting function to create username for player
print("Text-Based Adventure Menu")
print("Welcome user_")
Username_ = input("What shall I call you? ")
print("Ok " + Username_ + " what would you like to do?")

# Actions and directions possible
possible_actions = ["Attack [1]", "Inventory [2]", "Explore [3]", "Heal[4]",
                    "Character[5]", "Quit[6]"]
possible_directions = ["North [1]", "East [2]", "South [3]", "West [4]"]

# Characters with description
character_selection = ["Wonder Boy [1]", "Beefy Man [2]"]
character_s = {
    "Wonder Boy":
        {"Description": "A ninja raised in the forest who "
            "chases bears in his spare time",
            "Bonuses": "Has +3 Speed and +2 Damage points"},
    "Beefy Man":
        {"Description": "Average joe who might have lifted "
            "a little too much weights",
            "Bonuses": "Has +1 Damage and +4 Defense points"}
            }

# Inventory (Starting weapons)
inventory_s = {
    "Small Knife":
        {"Description": "Provides small damage and "
            "can be used for utilities", "Damage": 5, "Protection": 0},
    "Axe":
        {"Description": "Can cut down wooden and metal doors",
            "Damage": 15, "Protection": 0},
    "Shield":
        {"Description": "Provides protection against arrows,"
            " swords and bullets",
            "Damage": 0, "Protection": 20}
        }


# Function to only list name of weapons
def start_inventory_fnct():
    for weapon in inventory_s:
        print(f"{weapon}")


# Function to list name of weapons plus description
def inventory_description():
    for weapon in inventory_s:
        print(f"\n{weapon}:")
        for item in inventory_s[weapon]:
            print(f"{item} - {inventory_s[weapon][item]}")


# Function to write out characters plus a mini description
def character_choice():
    for character in character_s:
        print(f"\n{character}")
        for item in character_s[character]:
            print(f"{item} - {character_s[character][item]}")


# While loop for menu to stay active, will not close unless 'quit' is chosen
while True:
    """Definition for the menu"""
    for action in possible_actions:
        print(f" {action}")
    menu_c = str(input("\nWhat action would u like to choose? "))
    if menu_c == "1":
        print("Attacking!\n")
    elif menu_c == "2":
        print("\nInventory:")
        start_inventory_fnct()
        inv_desc = input("\nShow descriptions? \nYes [1], No [2] ") 
        if inv_desc == "1":
            inventory_description()
        else:
            print("No problemo")
    elif menu_c == "3":
        for direction in possible_directions:
            print(f" {direction}")
        directions_chosen = str(input("What direction would you like to go? "))
        if directions_chosen == "1":
            print("Going North!")
        elif directions_chosen == "2":
            print("Going East!")
        elif directions_chosen == "3":
            print("Going South!")
        elif directions_chosen == "4":
            print("Going West!")
    elif menu_c == "4":
            print("Healing!")
    elif menu_c == "5":
        print("\nCharacters:")
        character_choice()
        character_chosen = input("\nWhich character will you choose?\n")
        if character_chosen == "Wonder Boy":
            print("Wonder Boy 'SELECTED'")
            print("Great choice, Extra speed will be on your side")
        elif character_chosen == "Beefy Man":
            print("Beefy Man 'SELECTED'")
            print("Excellent, Defense bonuses will come in handy")
        else:
            print("Maybe try to actually print a characters name correctly")
    # Quit function will work with the sys.exit command
    elif menu_c == "6":
        if menu_c == "6":
            choice_s = str(input("Are you sure you would like to exit? [1] "))
            if choice_s.lower() == "1":
                print("Exiting, Goodbye " + Username_)
                sys.exit()
        else:
            print("Countinue!")
    else:
        print("Sorry that does not work, Choose a different option ")
