# Dictionary of programming terms and their definitions
programming_terms = {
    1: ("Algorithm", "is a set of instructions that are followed to solve a problem."),
    2: ("Variable", "container that holds a single number, word, or other information that you can use throughout a program."),
    3: ("Variable Type (data type)", "Basic variable types include: string (words and phrases), char (short for 'character;' a single letter or symbol you can type), int (short for 'integer;' for whole numbers), double or float (for decimal numbers), and bool (short for 'boolean;' for true or false values."),
    4: ("Array", "containers that hold variables of the same data type."),
    5: ("If statement", "runs a block of code based on whether or not a condition is true."),
    6: ("Loop","check a condition and then run a code block.  The loop will continue to check and run until a specified condition is reached."),
    7: ("Function","block of code that can be referenced by name to run the code it contains."),
    8: ("Class","template definition of the methods and variables in a particular kind of object."),
    9: ("Object","data type that has unique attributes and behavior."),
    10: ("Method","programmed procedure that is defined as part of a class and is available to any object instantiated from that class."),
    11: ("Programming Language","system of notation for writing computer programs.  Python is an example."),
    12: ("Control Structure","basic blocks for decision making processes in computing."),
    13: ("Error!","Not a valid choice."),
}

# Function to display the menu and provide definitions
def display_menu():
    print("This program will provide definitions to important programming terms.")
    print("Choose a number to see the term's definition.\n")
    print("Terms:")
    # Prints the terms in the list and breaks at 13 so i can hide the error term ;)
    for key, value in programming_terms.items():
        if key <= 12:
            print(f"{key}: {value[0]}")
    # player input
    player_input = input("\nEnter the number of the term you want to learn about: ")

    try:
        #turns input variable to string and if its in the available terms it will print corresponding term and def
        player = int(player_input)
        if player in programming_terms:
            term, definition = programming_terms[player]
            print(f"\n{term}: {definition}\n")
        #IF theyre stupid itll print the error term
        else:
            term, definition = programming_terms[13]
            print(f"\n{term} {definition}\n")
    # My IDE and autograder both add values after running the program so when that happens it will also print error term ;)
    except ValueError:
        term, definition = programming_terms[13]
        print(f"\n{term} {definition}\n")

# Main program loop
while True:
    display_menu()
   
