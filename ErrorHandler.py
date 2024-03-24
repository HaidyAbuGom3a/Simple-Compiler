import re
from Tokens import *
from Patterns import *
import FileManager

def analyze_syntax(filename):
    text = FileManager.openFile(filename).split(';')
    modified_list = [item.replace('\n', '') + ';' for item in text]
    modified_list.remove(';')
    errors = []
    for line in modified_list:
        match = re.match(statement_pattern, line)
        
        if(not match):
            errors.append('error in line ' + line)
        

    if(len(errors) == 0):
        print('Code syntax is valid!')
    else:
        for error in errors:
            print('Syntax error:', error)

