def evaluate_expression(expression, symbol_table):
    if isinstance(expression, int):
        return expression  # Return integer literal value

    if isinstance(expression, str):
        if expression.startswith('"') and expression.endswith('"'):
            return expression[1:-1]  # Return string literal value
        elif expression in symbol_table:
            return symbol_table[expression]  # Return value from symbol table
        else:
            raise ValueError("Undefined variable or invalid identifier: {}".format(expression))

    operator = expression[0]
    if operator == '+':
        return evaluate_expression(expression[1], symbol_table) + evaluate_expression(expression[2], symbol_table)
    elif operator == '-':
        return evaluate_expression(expression[1], symbol_table) - evaluate_expression(expression[2], symbol_table)
    elif operator == '*':
        return evaluate_expression(expression[1], symbol_table) * evaluate_expression(expression[2], symbol_table)
    elif operator == '/':
        return evaluate_expression(expression[1], symbol_table) / evaluate_expression(expression[2], symbol_table)
    else:
        raise ValueError("Invalid operator: {}".format(operator))
def execute_ast(parse_tree):
    print("Begin exec")
    symbol_table = {}  # A dictionary to store variable assignments
    result = None  # Variable to store the result of the 'Answer' assignment

    for statement in parse_tree:
        if statement[0] == 'assignment':
            identifier = statement[1]
            value = evaluate_expression(statement[2], symbol_table)
            symbol_table[identifier] = value

            if identifier == 'Answer':
                result = value  # Store the result of 'Answer' assignment
        elif statement[0] == 'print':
            value = evaluate_expression(statement[1], symbol_table)
            print(value)
        elif statement[0] == 'read':
            identifier = statement[1]
            input_value = input("Enter a value for {}: ".format(identifier))

            # Check if input value is an integer or string
            if input_value.isdigit():
                symbol_table[identifier] = int(input_value)  # Store integer input
            else:
                symbol_table[identifier] = input_value  # Store string input
        elif statement[0] == 'if':
            condition = evaluate_expression(statement[1], symbol_table)
            if condition:
                execute_ast(statement[2])

    if result is not None:
        print(result)