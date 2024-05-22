# lab2 - student
# updated: 2/8/2024
# name: 
# date: 

# import the random module
import random

## functions

# PLACE ALL FUNCTIONS HERE


def main():
    # print welcome message
    # <code>

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
    # <code>

    # for loop to simulate a full battle with turns. use variable for the amount of turns for range
    for i in range(turns): 
        print("-"*50) 
        # this print will using the temporary variable *i* and print it
        print(f"Turn {i}") 
        ## pokemon_1 attacks pokemon_2 
        # damage = call calcDamage() with correct arguments; pokemon_1 will use crit_multiplier
        # pokemon_2_hp = call applyDamage() with correct arguments 
        # call printOutcome() with the correct arguments 

        ## pokemon_2 attacks pokemon_1 
        # damage = call calcDamage() with correct arguments; pokemon_2 will use normal damage so crit is set to 1 
        # pokemon_1_hp = call applyDamage() with correct arguments 
        # call printOutcome() with the correct arguments

        
##################### initiate main
# initiate main this way, as was explained in class
if __name__ == "__main__":
    main()