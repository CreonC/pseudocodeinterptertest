import lexer
import parser
import execute as execengine

program2 = '''
x <- 10
y <- 20
PRINT x 
PRINT y
PRINT "If x does not equal to 5 then it's broken"
IF x = 10 THEN
    x - 5
    PRINT x
ENDIF
'''




tokens2 = lexer.lexer(program2)
for token in tokens2:
    print(token)
parse_tre2e = parser.parse(tokens2)
print(parse_tre2e)


print("NOW RUNNING")
execengine.execute_ast(parse_tre2e)