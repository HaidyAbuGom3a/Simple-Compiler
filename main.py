import Lexer
from ErrorHandler import analyze_syntax
import SymbolTable

filename = "hello.ota"
Lexer.print_table(filename)
errors = Lexer.errors

if(len(errors) == 0):
    print('')
    print('--------------Checking if syntax is valid -------------\n')
    analyze_syntax(filename)
    print('')
    print('--------------Printing sybmol table -------------\n')
    print('- Unordered Symbol table')
    SymbolTable.printSymoblTable(filename, False)
    print('\n- Ordered Symbol table')
    SymbolTable.printSymoblTable(filename, True)
    print('\n- Hash Symbol table')
    SymbolTable.printHashSymbolTable(filename)
    print('')

