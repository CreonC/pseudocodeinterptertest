import re

token_patterns = [
    (re.compile(r'READ|PRINT|IF|THEN|ELSE|ENDIF'), 'KEYWORD'),
    (re.compile(r'<-|=|\+|-|\*|/'), 'OPERATOR'),
    (re.compile(r'[a-zA-Z][a-zA-Z0-9]*'), 'IDENTIFIER'),
    (re.compile(r'\d+|"[^"]*"'), 'LITERAL'),
]

def lexer(program):
    tokens = []
    position = 0
    inside_statement = 0

    while position < len(program):
        match = None
        for pattern, token_type in token_patterns:
            regex_match = pattern.match(program, position)
            if regex_match:
                match = regex_match.group(0)
                if token_type == 'LITERAL' and match.startswith('"') and match.endswith('"'):
                    # Remove quotation marks from string literals
                    match = match[1:-1]

                if token_type == 'KEYWORD':
                    if match in ['IF', 'FOR', 'WHILE']:  # Opening statement keyword
                        inside_statement += 1
                    elif match in ['ENDIF', 'NEXT', 'ENDWHILE']:  # Closing statement keyword
                        inside_statement -= 1
                        inside_statement = max(inside_statement, 0)  # Ensure inside_statement is non-negative

                tokens.append((token_type, match, inside_statement))  # Include inside_statement in token tuple
                position = regex_match.end()
                break

        if not match:
            if program[position].isspace():
                position += 1
            else:
                # Handle unrecognized characters or raise an error
                raise ValueError(f"Invalid token at position {position}")

    return tokens