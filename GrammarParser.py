def parse_grammar(grammar):
    # Parse the grammar input and return a dictionary mapping non-terminal symbols to their productions
    grammar_dict = {}
    lines = grammar.strip().split('\n')
    for line in lines:
        # Split the line into the non-terminal and the production rule
        lhs, rhs = line.split('->')
        lhs = lhs.strip()
        rhs = rhs.strip().split('|')
        # Add the productions to the grammar dictionary
        grammar_dict[lhs] = [production.strip() for production in rhs]
    return grammar_dict