# lab5 - frpatoto42
# name: Finlay Patoto
# date: 7/19/2024 (Due date, current date: 5/22/2024)

# The dictionaries are new to me. I have never properly used
# python for anything besides (some) automation at my workplace. 
# I found this to be a great practice in implementing them! 
# Thank you!

# import the random module
import random

## functions
def welcome():
    # Prints Welcome Message
    print("Welcome to the Python Pokemon Battle Simulator!")
    print("#" * 50)
    
# Function to ask user if they want to play--or continue playing.
def playing():
    # Loop to repeat question if faulty input
    while True:
        # Get user input
        user_input = input("Would you like to start a battle? (y/n): ")
        # Check user input, if valid, it breaks loop and returns the true/false value. 
        # Otherwise repeats while loop.
        if user_input.lower() == 'y':
            play = True
            break
        elif user_input.lower() == 'n':
            play = False
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    return play

def calcDamage(ap, crit=1):
    # this function is complete
    # returns attack power minus a random integer between 1 and 5.
    # this is then multiplied by passed crit_multiplier
    return (ap - random.randint(1, 5)) * crit

def applyDamage(defender_hp, damage):
    # Calculation from lab 2, (MODIFIED)
    defender_remaining_hp = defender_hp - damage
    # Check if hp is less than 0, if so, set zero
    if defender_remaining_hp <= 0:
        defender_remaining_hp = 0
    return defender_remaining_hp

# Function to print turn options
def printOptions():
    print("Press 1 for Attack")
    print("Press 2 for Pass")
    print("Press 3 for Item")
    # Get user input and turn into in. 
    # Chapter 5 showed how to convert into string, I assumed it worked with int and it does.
    user_input = input("Press 1, 2, or 3 to continue: ")
    choice = int(user_input)
    return choice

# print the outcome of the turn
def printOutcome(attacker, defender, damage, defender_hp):
    # this function is complete
    print(f"{attacker} attacks {defender} for {damage} damage.")
    print(f"{defender}'s HP is now {defender_hp}.")

# pokemon_atk and pokemon_def are dictionaries.
# these will be passed by reference
def attack(pokemon_atk, pokemon_def, crit_multiplier=1):
    # Modified the code provided to use the dictionaries passed
    damage = calcDamage(pokemon_atk["AP"], crit_multiplier)
    pokemon_def["HP"] = applyDamage(pokemon_def["HP"], damage)
    printOutcome(pokemon_atk["Name"], pokemon_def["Name"], damage, pokemon_def["HP"])

# pokemon is a dictionary and items is a list
def useItem(pokemon, items):
    while True:
        # print 1. Use potion items[0]
        # print 2. Use attack_up items[1]
        # print 3. Cancel
        print(f"1. Use potion ({items[0]})")
        print(f"2. Use attack_up ({items[1]})")
        print(f"3. Cancel")
        # create variable choice and assign it the value of user input
        choice = int(input("Choose an option: "))
        # Doing the option picked. Based off provided comments on lab report.
        if choice == 1 and items[0] > 0:
            pokemon["HP"] += 10
            items[0] -= 1
            print(f"{pokemon['Name']}'s HP was increased by 10 to {pokemon['HP']}.")
            break
        elif choice == 2 and items[1] > 0:
            pokemon["AP"] += 10
            items[1] -= 1
            print(f"{pokemon['Name']}'s AP was increased by 10 to {pokemon['AP']}.")
            break
        elif choice == 3:
            break
        else:
            print("Not an option or insufficient items!")
            

def battle():
    # print welcome message
    welcome()
    
    # pokemon 1 information
    pokemon_1 = {"Name": "Pikachu", "HP": 100, "AP": 20}
    pokemon_1_items = [3, 1]  # 3 potions, 1 attack_up

    # pokemon 2 information
    pokemon_2 = {"Name": "Charmander", "HP": 90, "AP": 25}
    pokemon_2_items = [2, 2]  # 2 potions, 2 attack_ups

    # multiplier for when a critical hit is landed
    crit_multiplier = 1.5

    # set the amount of turns in a variable
    turn = 0

    # A while loop that keeps going until one pokemon faints
    while True:
        # increment turn; add 1 to it at the top of the loop
        turn += 1
        
        print("-" * 50)
        print(f"Turn {turn}")
         
        ###### attacker 1 turn
        while True:
            print(f"{pokemon_1['Name']}'s turn!")
            # getting choice for pokemon 1
            choice_1 = printOptions()
            
            # pokemon_1 attacks pokemon_2
            if choice_1 == 1:
                attack(pokemon_1, pokemon_2, crit_multiplier)
                break
            elif choice_1 == 2:
                print(f"{pokemon_1['Name']} passes turn")
                break
            elif choice_1 == 3:
                useItem(pokemon_1, pokemon_1_items)
                break
            else:
                print("Not an option!")
            ### end of nested while loop
        
        # Check if pokemon 2 has fainted
        if pokemon_2["HP"] <= 0:
            # First print to make space for visually appealing.
            print()
            print(f"{pokemon_2['Name']} fainted!")
            break

        # Add space between pokemon turns
        print()

        ###### attacker 2 turn
        while True:
            print(f"{pokemon_2['Name']}'s turn!")
            # getting choice for pokemon 2
            choice_2 = printOptions()
            
            # pokemon_2 attacks pokemon_1
            if choice_2 == 1:
                attack(pokemon_2, pokemon_1)
                break
            elif choice_2 == 2:
                print(f"{pokemon_2['Name']} passes turn")
                break
            elif choice_2 == 3:
                useItem(pokemon_2, pokemon_2_items)
                break
            else:
                print("Not an option!")
            ### end of nested while loop
        
        # Check if pokemon 1 has fainted
        if pokemon_1["HP"] <= 0:
            # First print to make space for visually appealing.
            print()
            print(f"{pokemon_1['Name']} fainted!")
            break

# main function to control game flow
def main():
    while playing():
        battle()
        
##################### initiate main
# initiate main this way, as was explained in class
if __name__ == "__main__":
    main()
