# lab2 - student
# updated: 2/8/2024
# name: Finlay Patoto
# date: 6/14/2024 (Due date, current date: 5/22/2024)

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

# applies damage to attacked pokemon
def applyDamage(defender_hp, damage):
    # do the following:
    # code to return hp - damage... Added () because it makes more sense from my C++ days.
    return (defender_hp - damage)

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
         
        ## pokemon_1 attacks pokemon_2 
        # damage = call calcDamage() with correct arguments; pokemon_1 will use crit_multiplier
        damage = calcDamage(pokemon_1_ap, crit_multiplier)
        # pokemon_2_hp = call applyDamage() with correct arguments 
        pokemon_2_hp = applyDamage(pokemon_2_hp, damage)
        # call printOutcome() with the correct arguments 
        printOutcome(pokemon_1_name, pokemon_2_name, damage, pokemon_2_hp)

        ## pokemon_2 attacks pokemon_1 
        # damage = call calcDamage() with correct arguments; pokemon_2 will use normal damage so crit is set to 1 
        damage = calcDamage(pokemon_2_ap, 1) 
        # pokemon_1_hp = call applyDamage() with correct arguments 
        pokemon_1_hp = applyDamage(pokemon_1_hp, damage)
        # call printOutcome() with the correct arguments
        printOutcome(pokemon_2_name, pokemon_1_name, damage, pokemon_1_hp)

        
##################### initiate main
# initiate main this way, as was explained in class
if __name__ == "__main__":
    main()