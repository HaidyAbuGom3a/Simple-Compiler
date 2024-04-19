import FirstSet

def compute_follow_sets(grammar_dict, first_sets):
    # Initialize the Follow sets dictionary with empty sets
    follow_sets = {nt: set() for nt in grammar_dict}
    
    # Add $ to the Follow set of the start symbol (first non-terminal defined)
    start_symbol = list(grammar_dict.keys())[0]
    follow_sets[start_symbol].add('$')
    
    # Define a function to update the Follow sets based on the grammar
    def update_follow_sets():
        updated = False
        
        # Iterate through each production in the grammar
        for lhs, productions in grammar_dict.items():
            for production in productions:
                # Process the production from left to right
                for i in range(len(production)):
                    symbol = production[i]
                    
                    # If the symbol is a non-terminal, compute its Follow set
                    if symbol in grammar_dict:
                        # Check the remaining symbols in the production
                        for j in range(i + 1, len(production)):
                            next_symbol = production[j]
                            
                            # If the next symbol is a terminal, add it to the Follow set of the current symbol
                            if next_symbol not in grammar_dict:
                                if next_symbol not in follow_sets[symbol]:
                                    follow_sets[symbol].add(next_symbol)
                                    updated = True
                                break
                            
                            # If the next symbol is a non-terminal, add its First set (except epsilon) to the Follow set of the current symbol
                            next_first_set = first_sets[next_symbol]
                            next_first_set_without_epsilon = next_first_set - {'epsilon'}
                            
                            if not next_first_set_without_epsilon.issubset(follow_sets[symbol]):
                                follow_sets[symbol].update(next_first_set_without_epsilon)
                                updated = True
                            
                            # If the next First set contains epsilon, continue to the next symbol
                            if 'epsilon' not in next_first_set:
                                break
                        
                        # If we've reached the end of the production or there was epsilon propagation, add Follow of LHS to the current symbol
                        else:
                            if not follow_sets[lhs].issubset(follow_sets[symbol]):
                                follow_sets[symbol].update(follow_sets[lhs])
                                updated = True
        
        return updated
    
    # Repeatedly update the Follow sets until no more changes occur
    while update_follow_sets():
        pass
    
    return follow_sets

def printFollowSets(grammar_dict):
    first_sets = FirstSet.compute_first_sets(grammar_dict)
    follow_sets = compute_follow_sets(grammar_dict, first_sets)

    # Print the Follow sets in the expected format
    for nt, follow_set in follow_sets.items():
        # Convert the set to a sorted list to keep consistent ordering in output
        print(f"Follow({nt}) = {sorted(follow_set)}")

