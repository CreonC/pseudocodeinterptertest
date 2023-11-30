import lexer
import parser
import execute as execengine

#External packages
import pprint

program2 = '''
READ num1
READ num2
PRINT "ENTER PLUS OR MINUS"
READ plusMinus
IF plusMinus = "+" THEN
    Answer <- num1 + num2
ELSE
    Answer <- num1 - num2
ENDIF

PRINT Answer
'''




tokens2 = lexer.lexer(program2)
for token in tokens2:
    pprint.pprint(token)
parse_tree = parser.parse(tokens2)
print("AST BELOW")
pprint.pprint(parse_tree)
print("AST ABOVE")

print("execengine.execute_ast()")
execengine.execute_ast(parse_tree)

