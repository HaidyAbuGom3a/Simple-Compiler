from Tokens import *
from Patterns import identifier_pattern
from nltk import word_tokenize
import re
import FileManager


    
def getLexemes(filename):
    text = FileManager.openFile(filename)
    # string_pattern = r"'(?:[^'\\]|\\.)*'"
    # matches = re.findall(string_pattern, text)
    # new_text = re.sub(string_pattern, 'PLACEHOLDER', text)
    # tokenized_text = word_tokenize(new_text)
    # j = 0
    # for index in range(0, len(tokenized_text)):
    #     if(tokenized_text[index] == 'PLACEHOLDER'):
    #         tokenized_text[index] = matches[j]
    #         j += 1
    tokenized_text = word_tokenize(text)
    return tokenized_text

errors = []

def getLexemesWithTokens(filename):
    lexemes = getLexemes(filename)
    tokens = []
    for word in lexemes:
        if(word in keywords):
            tokens.append('Keyword')
        elif(word in parentheses):
            tokens.append('Parentheses')
        elif(word in operators):
            tokens.append('Operator')
        elif(word in symbols):
            tokens.append('Symbol')
        elif(word.isnumeric() or word == 'true' or word == 'false'):
            tokens.append('Constant')
        elif(re.match(identifier_pattern, word)):
            tokens.append('Identifier')
        else:
            error = 'Lexical error, input: ' + word + ' Not matched!'
            errors.append(error)
    return lexemes, tokens


def print_table(filename):
    lexemes, tokens = getLexemesWithTokens(filename)
    if(len(errors) == 0):
        print('Lexemes \t\t Tokens')
        for i in range(len(tokens)):
            space = '\t\t\t'
            if(len(lexemes[i]) > 6):
                space = '\t\t'
            print(lexemes[i], space, tokens[i])
        return 
    for error in errors:
        print(error)
    