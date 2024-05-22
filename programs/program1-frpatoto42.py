# Program Name: program1-frpatoto42.py
# Name: Finlay Patoto
# Date Modified: 5/22/2024
# Date Due: 6/28/2024

# I added a lot of comments to help explain the process.
# Should be fairly straight forward.


# This function prints bottom of the squares
def print_tb_sides(m):
    # Loops through the m to print tops/bottoms of squares
    for i in range(m):
        print("+ - - - - ", end="")
    # Prints the last + on the square
    print("+")

# This function prints the sides of the sqaures
def print_sides(m):
    # Loops through the m to print the sides of squares
    for i in range(4):  
        for i in range(m):
            print("|         ", end="")
        # Prints the last | on the square
        print("|")

# This function prints the 2 by N sqaure grid of Ascii
def print2byN(n):
    # Loops through the height and prints the width 2
    for i in range(n):
        print_tb_sides(2)
        print_sides(2)
    print_tb_sides(2)

# This function prints the 4 by N sqaure grid of Ascii
def print4byN(n):
    # Loops through the height and prints the width 4
    for i in range(n):
        print_tb_sides(4)
        print_sides(4)
    print_tb_sides(4)

# This function prints the M by N square grid of Ascii
def printMbyN(m, n):
    # Loops through the height and prints the width m
    for i in range(n):
        print_tb_sides(m)
        print_sides(m)
    print_tb_sides(m)

def main():
    # Accept user input for the different grid sizes
    n_input_2byN = input("What is 'n' value for 2byN?: ")
    n_2byN = int(n_input_2byN)
    
    n_input_4byN = input("What is 'n' value for 4byN?: ")
    n_4byN = int(n_input_4byN)
    
    m_input_MbyN = input("What is 'm' value for MbyN?: ")
    m_MbyN = int(m_input_MbyN)
    
    n_input_MbyN = input("What is 'n' value for MbyN?: ")
    n_MbyN = int(n_input_MbyN)

    # Print the different grids
    print2byN(n_2byN)
    print4byN(n_4byN)
    printMbyN(m_MbyN, n_MbyN)

# Run the main function
if __name__ == "__main__":
    main()
