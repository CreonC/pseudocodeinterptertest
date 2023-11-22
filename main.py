import tkinter.messagebox
variables = {}  # Dictionary to store variable names and their values
LineCount = 1



def showErrorBox(message):
    tkinter.messagebox.showerror("IPC interpreter", message)
def declare_variable(name, value):
    if value.isdigit():
        variables[name] = int(value)
    elif value in variables:
        variables[name] = variables[value]
    else:
        showErrorBox(f"Error: Variable {name} is not defined at line: " + str(LineCount))
        raise Exception(f"Error: Variable {value} is not defined at line: " +str(LineCount))

def print_variable(name):
    if name in variables:
        print(variables[name])
    else:
        showErrorBox(f"Error: Variable {name} is not defined at line: " + str(LineCount))
        raise Exception(f"Error: Variable {name} is not defined at line: " + str(LineCount))

def interpret_line(line):
    tokens = line.split()
    #LineCount = LineCount + 1
    if tokens[1] == "<-":
        declare_variable(tokens[0], tokens[2])
    elif tokens[0] == "PRINT":
        print_variable(tokens[1])
    else:
        showErrorBox("Invalid code/syntax at: '" + line + "' Line: " + str(LineCount))
        raise InterruptedError("Invalid code at: '" + line + "' Line: " + str(LineCount))

# Make user enter a txt formatted file ending in .ipc



interpret_line("X <- 10")  # Declare variable X with value 10
interpret_line("PRINT X")  # Print the value of variable X
interpret_line("X <- X + 10")  # Update the value of variable X
interpret_line("Y <- X - 5")  # Declare variable Y with value X - 5
interpret_line("PRINT Y + X")  # Print the value of variable Y
#interpret_line("PRINT = 5") #this should error
interpret_line("WFA <- Y + at3t32") #make this error

print(variables)