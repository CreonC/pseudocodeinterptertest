import astgen
import tokengen
import exengine


# Test tokenizer
code = ("""howjrhiwr <- 1

local <- 2
proint <- 3
""")
tokens = tokengen.tokenize(code)
print(tokens)

ast = astgen.generate_ast(tokens)
print(ast)

exengine.execute(ast)