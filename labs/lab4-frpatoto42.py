# lab4 - frpatoto42
# name: Finlay Patoto
# date: 7/12/2024 (Due date, current date: 5/22/2024)

# import the random module
import random

## functions
def welcome():
    # Prints Welcome Message
    print("Welcome to the Python Pokemon Battle Simulator!")
    print("#"*50)
    
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

def calcDamage(ap, crit = 1):
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


def battle():
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
    turn = 0

    # A while loop that keeps going until one pokemon faints
    while True:
        # increment turn; add 1 to it at the top of the loop
        turn += 1
        
        print("-"*50) 
        # this print will using the temporary variable *i* and print it
        print(f"Turn {turn}")
         
        ###### attacker 1 turn
        while True:
            print(f"{pokemon_1_name}'s turn!")
            # getting choice for pokemon 1
            choice_1 = printOptions()
            
            # pokemon_1 attacks pokemon_2
            if choice_1 == 1:
                damage = calcDamage(pokemon_1_ap, crit_multiplier)
                pokemon_2_hp = applyDamage(pokemon_2_hp, damage)
                printOutcome(pokemon_1_name, pokemon_2_name, damage, pokemon_2_hp)
                break
            elif choice_1 == 2:
                print(f"{pokemon_1_name} passes turn")
                break
            else:
                print("Not an option!")
            ### end of nested while loop
        
        # Check if pokemon 2 has fainted
        if pokemon_2_hp <= 0:
            # First print to make space for visually appealing.
            print()
            print(f"{pokemon_2_name} fainted!")
            break

        # Add space between pokemon turns
        print()

        ###### attacker 2 turn
        while True:
            print(f"{pokemon_2_name}'s turn!")
            # getting choice for pokemon 2
            choice_2 = printOptions()
            
            # pokemon_2 attacks pokemon_1
            if choice_2 == 1:
                damage = calcDamage(pokemon_2_ap)
                pokemon_1_hp = applyDamage(pokemon_1_hp, damage)
                printOutcome(pokemon_2_name, pokemon_1_name, damage, pokemon_1_hp)
                break
            elif choice_2 == 2:
                print(f"{pokemon_2_name} passes turn")
                break
            else:
                print("Not an option!")
            ### end of nested while loop
        
        # Check if pokemon 1 has fainted
        if pokemon_1_hp <= 0:
            # First print to make space for visually appealing.
            print()
            print(f"{pokemon_1_name} fainted!")
            break

        
# main function to control game flow
def main():
    while playing():
        battle()
        
##################### initiate main
# initiate main this way, as was explained in class
if __name__ == "__main__":
    main()