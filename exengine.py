def execute(ast):
    for node in ast:
        execute_node(node)

def execute_node(node):
    node_type = node['type']
    if node_type == 'IDENTIFIER':
        # Handle identifier node
        value = node['value']
        print(f'Identifier: {value}')
    elif node_type == 'INTEGER':
        # Handle integer node
        value = node['value']
        print(f'Integer: {value}')
    elif node_type == 'ASSIGN':
        # Handle assignment node
        execute_assignment(node)
    else:
        raise ValueError(f'Invalid node type: {node_type}')

def execute_assignment(node):
    # Handle assignment node
    children = node['children']
    identifier_node = children[0]
    value_node = children[1]

    identifier = identifier_node['value']
    value = value_node['value']
    print(f'Assignment: {identifier} <- {value}')

