# IGCSE Interpreter Pseudocode

# Define the variables
variables = {}


# Define the main interpreter function
def interpreter():
    # Read the user input
    user_input = input(">> ")

    # Check if the user wants to exit
    if user_input == "exit":
        return

    # Split the input into tokens
    tokens = user_input.split()

    # Check the first token
    if tokens[0] == "PRINT":
        # Handle the PRINT command
        if len(tokens) > 1:
            # Print the value of the variable
            variable_name = tokens[1]
            if variable_name in variables:
                print(variables[variable_name])
            else:
                print("Variable not found.")
        else:
            print("Invalid PRINT command.")
    elif tokens[0] == "LET":
        # Handle the LET command
        if len(tokens) == 3 and tokens[2].isdigit():
            # Assign a value to a variable
            variable_name = tokens[1]
            variable_value = int(tokens[2])
            variables[variable_name] = variable_value
        else:
            print("Invalid LET command.")
    else:
        print("Invalid command.")

    # Continue the interpreter
    interpreter()