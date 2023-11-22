variables = {}  # Dictionary to store variable names and their values

def declare_variable(name, value):
    if value.isdigit():
        variables[name] = int(value)
    elif value in variables:
        variables[name] = variables[value]
    else:
        print(f"Error: Variable {value} is not defined.")

def print_variable(name):
    if name in variables:
        print(variables[name])
    else:
        print(f"Error: Variable {name} is not defined.")

def interpret_line(line):
    tokens = line.split()

    if tokens[1] == "<-":
        declare_variable(tokens[0], tokens[2])
    elif tokens[0] == "PRINT":
        print_variable(tokens[1])
    else:
        print("Error: Invalid syntax.")


interpret_line("X <- 10")  # Declare variable X with value 10
interpret_line("PRINT X")  # Print the value of variable X
interpret_line("X <- X + 10")  # Update the value of variable X
interpret_line("Y <- X - 5")  # Declare variable Y with value X - 5
interpret_line("PRINT Y + X")  # Print the value of variable Y
interpret_line("WFA <- Y + %")

print(variables)