# Program Name: program2-frpatoto42.py
# Name: Finlay Patoto
# Date Modified: 5/22/2024
# Date Due: 7/26/2024

def addStudent(student_dict):
    # Get new user T number.
    t_num = input("Enter new user ID number: ")
    
    # Check if they exist to not have errors
    if t_num in student_dict:
        print("Student with this T-number already exists.")
        return
    
    # Get users information
    name = input("Enter new user NAME field: ")
    username = input("Enter new user USERNAME field: ")
    major = input("Enter new user MAJOR field: ")
    
    # Add user to the database.
    student_dict[t_num] = {"NAME": name, "USERNAME": username, "MAJOR": major}
    # Adds more segments. Makes it easier to read.
    print()

# This function lets you modify all the 
def modifyStudent(student_dict):
    # I changed your wording. You reused "new" and it makes more sense
    # for it to say existsing/updated.
    
    # Gets user input
    t_num = input("Enter existing user ID number: ")
    
    # Checks if they do NOT exist
    if t_num not in student_dict:
        print("Student with this T-number does not exist.")
        return
    
    # Gets user input for each component
    name = input(f"Enter updated user NAME field: ")
    username = input(f"Enter updated user USERNAME field: ")
    major = input(f"Enter updated user MAJOR field: ")
    
    # Make sure inputs weren't blank, otherwise it will not update that value.
    if name:
        student_dict[t_num]['NAME'] = name
    if username:
        student_dict[t_num]['USERNAME'] = username
    if major:
        student_dict[t_num]['MAJOR'] = major
    # Adds more segments. Makes it easier to read.
    print()

# This function displays all the students inside the database provided
def viewStudents(student_dict):
    # This makes sure no error happens when there are no students
    if not student_dict:
        print("No students in the database.")
        return
    
    # Match example output
    print()
    
    # Print all students inside database
    for t_num, details in student_dict.items():
        print(f"{t_num}")
        # This is to mathc given example output
        print("*"*6) 
        # Print all data inside student
        for key, value in details.items():
            print(f"{key} - {value}")
        print()

# This function removes a student when given the correct T number.
def removeStudent(student_dict):
    # Takes users input
    t_num = input("Please specify ID of student to remove: ")
    
    # Finds student, if they do not exist, it returns before trying to remove.
    if t_num not in student_dict:
        print("Student doesnt exist.")
        return
    
    # If student exists, then remove them and print out the example output from given ouput.
    del student_dict[t_num]
    print("Student Removed!")
    # Adds more segments. Makes it easier to read.
    print()

# This function displays all the actions the user can do.
def menu():
    print("TN Tech University Student Database")
    print("Please make a selection:")
    print("1. View all current students")
    print("2. Enter new student data")
    print("3. Remove student data")
    print("4. Modify student data")
    print("5. Quit")

def main():
    # Provided starter data
    student_data = {
        "T123": {"NAME": "Travis Lee", "USERNAME": "tlee", "MAJOR": "CSC"},
        "T124": {"NAME": "Jeremy Potts", "USERNAME": "jpotts", "MAJOR": "CHEM"}
    }
    
    # Loop to keep function going
    while True:
        menu()
        
        # Get user input for selection
        choice = input("Selection: ")
        
        # Do the corresponding function with the users input.
        if choice == '1':
            viewStudents(student_data)
        elif choice == '2':
            addStudent(student_data)
        elif choice == '3':
            removeStudent(student_data)
        elif choice == '4':
            modifyStudent(student_data)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Needs to be from '1' to '5'.")

if __name__ == "__main__":
    main()
