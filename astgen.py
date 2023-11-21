def generate_ast(tokens):
    ast = []
    stack = []
    current_node = None

    for token_type, value, _, _ in tokens:
        if token_type == "IDENTIFIER":
            node = {"type": "IDENTIFIER", "value": value, "children": []}
        elif token_type == "INTEGER":
            node = {"type": "INTEGER", "value": value, "children": []}
        elif token_type == "ASSIGN":
            node = {"type": "ASSIGN", "children": []}
        else:
            raise ValueError("Invalid token type: {}".format(token_type))

        if not stack:
            ast.append(node)
        else:
            parent_node = stack[-1]
            parent_node["children"].append(node)

        if token_type == "ASSIGN":
            stack.append(node)
        elif token_type == "INTEGER" or token_type == "IDENTIFIER":
            current_node = node

    return ast