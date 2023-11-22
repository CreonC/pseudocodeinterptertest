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

    while position < len(program):
        match = None
        for pattern, token_type in token_patterns:
            regex_match = pattern.match(program, position)
            if regex_match:
                match = regex_match.group(0)
                tokens.append((token_type, match))
                position = regex_match.end()
                break

        if not match:
            if program[position].isspace():
                position += 1
            else:
                # Handle unrecognized characters or raise an error
                raise ValueError(f"Invalid token at position {position}")

    return tokens