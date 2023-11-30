from collections import deque

def parse(tokens):
    tokens = deque(tokens)  # Convert tokens list to deque object

    def program():
        return statement_list()

    def statement_list():
        statements = []
        while tokens:
            statement = parse_statement()
            if statement is None:
                break
            statements.append(statement)
        return statements

    def parse_statement():
        if tokens and tokens[0][0] == 'IDENTIFIER':
            return assignment()
        elif tokens and tokens[0][0] == 'KEYWORD' and tokens[0][1] == 'PRINT':
            return print_statement()
        elif tokens and tokens[0][0] == 'KEYWORD' and tokens[0][1] == 'IF':
            return if_statement()
        elif tokens and tokens[0][0] == 'KEYWORD' and tokens[0][1] == 'READ':
            return read_statement()

    def assignment():
        identifier = tokens.popleft()[1]
        if tokens and tokens[0][1] == '<-':
            tokens.popleft()  # Consume the '<-' token
            expression_value = expression()
            return ('assignment', identifier, expression_value)

    def print_statement():
        tokens.popleft()  # Consume the 'PRINT' keyword
        if tokens and (tokens[0][0] == 'LITERAL' or tokens[0][0] == 'IDENTIFIER'):
            value = tokens.popleft()[1]
            return ('print', value)

    def if_statement():
        tokens.popleft()  # Consume the 'IF' keyword
        condition = expression()
        if tokens and tokens[0][0] == 'KEYWORD' and tokens[0][1] == 'THEN':
            tokens.popleft()  # Consume the 'THEN' keyword
            statements = statement_list()
            if tokens and tokens[0][0] == 'KEYWORD' and tokens[0][1] == 'ENDIF':
                tokens.popleft()  # Consume the 'ENDIF' keyword
            else:
                raise SyntaxError("Expected 'ENDIF' keyword, Got <placeholder>")
            return ('if', condition, statements)

    def read_statement():
        tokens.popleft()  # Consume the 'READ' keyword
        if tokens and tokens[0][0] == 'IDENTIFIER':
            identifier = tokens.popleft()[1]
            return ('read', identifier)

    def expression():
        term_value = term()
        while tokens and tokens[0][0] == 'OPERATOR' and (tokens[0][1] == '+' or tokens[0][1] == '-'):
            operator = tokens.popleft()[1]
            term_value = ('expression', operator, term_value, term())
        return term_value

    def term():
        factor_value = factor()
        while tokens and tokens[0][0] == 'OPERATOR' and (tokens[0][1] == '*' or tokens[0][1] == '/'):
            operator = tokens.popleft()[1]
            factor_value = ('term', operator, factor_value, factor())
        return factor_value

    def factor():
        if tokens and tokens[0][0] == 'IDENTIFIER':
            return tokens.popleft()[1]
        elif tokens and tokens[0][0] == 'LITERAL':
            return int(tokens.popleft()[1])

    return program()