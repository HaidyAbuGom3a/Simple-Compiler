def compute_first_sets(grammar_dict):
    # Initialize the First sets dictionary with empty sets
    first_sets = {nt: set() for nt in grammar_dict}
    
    # Helper function to compute First sets recursively
    def compute_first(nt):
        # If the First set for the non-terminal has already been computed, return it
        if first_sets[nt]:
            return first_sets[nt]
        
        # Process each production for the non-terminal
        for production in grammar_dict[nt]:
            # Handle the empty production (epsilon case)
            if production == 'epsilon':
                first_sets[nt].add('epsilon')
            else:
                # Process the production from left to right
                for symbol in production:
                    # If the symbol is a terminal, add it to the First set and stop
                    if symbol not in grammar_dict:
                        first_sets[nt].add(symbol)
                        break
                    else:
                        # If the symbol is a non-terminal, recursively compute its First set
                        sub_first_set = compute_first(symbol)
                        # Add all symbols from the sub First set, except epsilon
                        first_sets[nt].update(sub_first_set - {'epsilon'})
                        # If epsilon is in the sub First set, continue to the next symbol
                        if 'epsilon' not in sub_first_set:
                            break
                else:
                    # If all symbols in the production contained epsilon, add epsilon to the First set
                    first_sets[nt].add('epsilon')
        return first_sets[nt]
    
    # Compute First sets for each non-terminal in the grammar
    for nt in grammar_dict:
        compute_first(nt)
    
    return first_sets

def printFirstSets(grammar_dict):
    # Compute the First sets
    first_sets = compute_first_sets(grammar_dict)

    # Print the First sets in the desired format
    for nt, first_set in first_sets.items():
        print(f"First({nt}) = {first_set}")
    
    
