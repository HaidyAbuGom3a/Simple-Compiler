import Lexer
from ErrorHandler import analyze_syntax
import SymbolTable
import FirstSet
import GrammarParser
import FollowSet
import ParseTable

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
    print('\n- Tree Structure Symbol table')
    SymbolTable.printTreeStructureSymoblTabl(filename)
    print('')
    print('--------------Printing first set example -------------\n')
    grammar = """
S -> bXY
X -> b|c
Y -> b|epsilon
    """ 
    grammar_dict = GrammarParser.parse_grammar(grammar)
    print('Grammer example is:', grammar)
    FirstSet.printFirstSets(grammar_dict)
    print('')
    print('--------------Printing follow set example -------------\n')
    FollowSet.printFollowSets(grammar_dict)
    print('')
    print('--------------Printing Parse table -------------\n')
    terminals, parse_table = ParseTable.getTerminalsWithParseTable(grammar_dict)
    # Print the parse table
    ParseTable.print_parse_table(parse_table, terminals)


