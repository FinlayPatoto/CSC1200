# lab3 - frpatoto42
# name: Finlay Patoto
# date: 6/28/2024 (Due date, current date: 5/22/2024)

# import the random module
import random

## functions
def welcome():
    # Prints Welcome Message
    print("Welcome to the Python Pokemon Battle Simulator!")
    print("#"*50)
    
# PLACE ALL FUNCTIONS HERE
def calcDamage(ap, crit):
    # this function is complete
    # returns attack power minus a random integer between 1 and 5.
    # this is then multiplied by passed crit_multiplier
    return (ap - random.randint(1,5)) * crit

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
    # Get user input and turn into in. 
    # Chapter 5 showed how to convert into string, I assumed it worked with int and it does.
    user_input = input("Press 1 or 2 to continue: ")
    choice = int(user_input)
    return choice

# print the outcome of the turn
def printOutcome(attacker, defender, damage, defender_hp):
    # this function is complete
    print(f"{attacker} attacks {defender} for {damage} damage.")
    print(f"{defender}'s HP is now {defender_hp}.")


def main():
    # print welcome message     
    # <code>
    welcome()
    
    # pokemon 1 information: name, hit points, attack points
    pokemon_1_name = 'Pikachu'
    pokemon_1_hp = 100  # Hit Points
    pokemon_1_ap = 20   # Attack Points

    # pokemon 2 information: name, hit points, attack points
    pokemon_2_name = 'Charmander'
    pokemon_2_hp = 90
    pokemon_2_ap = 25

    # multiplier for when a critical hit is landed
    crit_multiplier = 1.5

    # set the amount of turns in a variable
    turns = 4

    # for loop to simulate a full battle with turns. use variable for the amount of turns for range
    for i in range(turns): 
        print("-"*50) 
        # this print will using the temporary variable *i* and print it
        print(f"Turn {i}")
         
        # Print name
        print(f"{pokemon_1_name}'s turn!")
        # Getting choice for pokemon 1
        choice_1 = printOptions()
        
        # Do pokemon 1's turn
        if choice_1 == 1:
            ## pokemon_1 attacks pokemon_2 
            # damage = call calcDamage() with correct arguments; pokemon_1 will use crit_multiplier
            damage = calcDamage(pokemon_1_ap, crit_multiplier)
            # pokemon_2_hp = call applyDamage() with correct arguments 
            pokemon_2_hp = applyDamage(pokemon_2_hp, damage)
            # call printOutcome() with the correct arguments 
            printOutcome(pokemon_1_name, pokemon_2_name, damage, pokemon_2_hp)
        elif choice_1 == 2:
            print(f"{pokemon_1_name} passes turn")
        else:
            print("Not an options! Lost turn.")

        # add spacing between turns
        print()
        
        # Print name
        print(f"{pokemon_2_name}'s turn!")
        # Getting choice for pokemon 2
        choice_2 = printOptions()
        
        # Do pokemon 2's turn
        if choice_2 == 1:
            ## pokemon_2 attacks pokemon_1 
            # damage = call calcDamage() with correct arguments; pokemon_2 will use normal damage so crit is set to 1 
            damage = calcDamage(pokemon_2_ap, 1) 
            # pokemon_1_hp = call applyDamage() with correct arguments 
            pokemon_1_hp = applyDamage(pokemon_1_hp, damage)
            # call printOutcome() with the correct arguments
            printOutcome(pokemon_2_name, pokemon_1_name, damage, pokemon_1_hp)
        elif choice_2 == 2:
            print(f"{pokemon_2_name} passes turn")
        else:
            print("Not an options! Lost turn.")

        
##################### initiate main
# initiate main this way, as was explained in class
if __name__ == "__main__":
    main()