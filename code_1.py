import Lexer
from ErrorHandler import analyze_syntax

filename = "hello.ota"
Lexer.print_table(filename)
errors = Lexer.errors
if(len(errors) == 0):
    print('')
    print('--------------Checking if syntax is valid -------------\n')
    analyze_syntax(filename)
    print('')