import re

# Token types
TOKEN_INTEGER = "INTEGER"
TOKEN_ADD = "ADD"
TOKEN_SUBTRACT = "SUBTRACT"
TOKEN_MULTIPLY = "MULTIPLY"
TOKEN_DIVIDE = "DIVIDE"
TOKEN_ASSIGN = "ASSIGN"
TOKEN_IDENTIFIER = "IDENTIFIER"
TOKEN_LPAREN = "LPAREN"
TOKEN_RPAREN = "RPAREN"

# Token regular expressions
TOKEN_REGEX = [
    (TOKEN_INTEGER, r"\d+"),
    (TOKEN_ADD, r"\+"),
    (TOKEN_SUBTRACT, r"-"),
    (TOKEN_MULTIPLY, r"\*"),
    (TOKEN_DIVIDE, r"/"),
    (TOKEN_ASSIGN, r"\<\-"),
    (TOKEN_IDENTIFIER, r"[a-zA-Z_][a-zA-Z0-9_]*"),
    (TOKEN_LPAREN, r"\("),
    (TOKEN_RPAREN, r"\)"),
    (None, r"\s+"),  # Skip whitespace
]


# Tokenization
def tokenize(code):
    tokens = []
    position = 0

    while position < len(code):
        matched = False

        for token_type, regex_pattern in TOKEN_REGEX:
            pattern = re.compile(regex_pattern)
            match = pattern.match(code, position)

            if match:
                if token_type:
                    value = match.group(0)
                    tokens.append((token_type, value, position + 1, match.end()))
                position = match.end()
                matched = True
                break

        if not matched:
            invalid_token = code[position]
            start_position = position + 1
            end_position = position + 2
            error_message = "Invalid token '{}' at position {}:{}.".format(
                invalid_token, start_position, end_position
            )
            raise ValueError(error_message)

    return tokens
