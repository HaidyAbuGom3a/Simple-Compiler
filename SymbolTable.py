import FileManager
import Lexer
import Tokens
from nltk import word_tokenize
from collections import OrderedDict

def printUnorderedSymoblTable(filename, isOrdered):
    refrence = 0
    identifiers = getIdentifiers(filename)
    if(isOrdered):
        identifiers.sort()
    dataTypes = getDataTypes(filename, identifiers)
    lines = getLines(filename)
    
    print('counter\t variable_name\tobject_refrence \t data_type \tdimenson\tline_dec\tline_ref')
    for i in range(1, len(identifiers)+1):
        dataTypeMemorySpace = {'int':2, 'boolean':1, 'float':4}
        lineDec = getLineDec(identifiers[i-1], lines)
        linesRef = getLinesRef(identifiers[i-1], lines)
        space = '\t\t'
        if len(identifiers[i-1]) > 5:
            space ='\t'
        print(i,'\t\t', identifiers[i-1],space, refrence, '\t\t',dataTypes[i-1],space,0,'\t\t', lineDec, '\t\t', linesRef)
        refrence += dataTypeMemorySpace[dataTypes[i-1]]

def getLineDec(identifier, lines):
    for index, line in enumerate(lines):
        if identifier in line:
            return index + 1
    return -1

def getLinesRef(identifier, lines):
    linesRef = []
    for index, line in enumerate(lines):
        if identifier in line:
            linesRef.append(index+1)
    linesRef.pop(0)
    return linesRef
    

def getIdentifiers(filename):
    identifiers = OrderedDict()
    lexemes, tokens = Lexer.getLexemesWithTokens(filename)
    for i in range(len(lexemes)):
        if(tokens[i] == "Identifier"):
            identifiers[lexemes[i]] = None
    return list(identifiers.keys())

def getLines(filename):
    code = FileManager.openFile(filename)
    lines = code.split('\n')
    return lines
        
def getLineDecs(filename, identifiers):
    lineDecs = []
    lines = getLines(filename)
    for identifier in identifiers:
        lineDec = getLineDec(identifier, lines)
        lineDecs.append(lineDec)
    return lineDecs

def getDataTypes(filename, identifiers):
    dataTypes = []
    lineDecs = getLineDecs(filename, identifiers)
    lines = getLines(filename)
    for lineIndex in lineDecs:
        words = word_tokenize(lines[lineIndex-1])
        for word in words:
            if word in Tokens.data_types:
                dataTypes.append(word)
    return dataTypes