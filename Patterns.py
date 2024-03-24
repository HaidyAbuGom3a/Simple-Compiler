import re
from Tokens import *

data_types_pattern = '|'.join(data_types)
keywords_pattern = '|'.join(map(re.escape, keywords))
math_operators_pattern = '|'.join(map(re.escape, math_operators))
logical_operators_pattern = '|'.join(map(re.escape, logical_operators))
number_pattern = '\d+(\.\d+)?'
constant_pattern = 'true|false|' + number_pattern
identifier_pattern = rf'(?!{keywords_pattern})[a-zA-Z]+_*[0-9]*'


comparison_pattern = rf'{number_pattern}\s*({logical_operators_pattern})\s*{number_pattern}|'

#condition:
#comparisoin
#comparisoin [and|or] comparisoin
#true|
#false
condition_pattern = rf'({comparison_pattern}|{comparison_pattern}\s*(and|or)\s*{comparison_pattern}|true|false)'

#operation:
#id math_oprator id   |
#id math_operator num |
#num math_operator id |
#num math_operator num
operation_pattern = rf'({identifier_pattern}\s*({math_operators_pattern})\s*{identifier_pattern}|{identifier_pattern}\s*({math_operators_pattern})\s*{number_pattern}|{number_pattern}\s*({math_operators_pattern})\s*{identifier_pattern})|{number_pattern}\s*({math_operators_pattern})\s*{number_pattern}'


#expression:
#operation |
#id  |
#constant|
#condtition
expression_pattern = rf'({operation_pattern}|{identifier_pattern}|{constant_pattern}|{condition_pattern})'

assignment_pattern = rf'(({data_types_pattern})\s+{identifier_pattern}\s*=\s*{expression_pattern})'

#statement:
#assignment term |
#expressoin term |
#print      term
statement_pattern = rf'{assignment_pattern}\;|{expression_pattern}\;|print\(({identifier_pattern}|{constant_pattern})\)\;'

def match_statement(text):
    match = re.match(statement_pattern, text)
    if(match):
        print('matched well')
    else:
        print('syntax error in statement', text)

def match_assignment(text):
    match = re.fullmatch(assignment_pattern, text)
    if(not match):
        #print('error in assignment pattern', text)
        return 'error in assignment'
    return ''