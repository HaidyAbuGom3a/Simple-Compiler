def openFile(filename):
    with open(filename, 'r') as file:
        return file.read()