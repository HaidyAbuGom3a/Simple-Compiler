import FirstSet
import FollowSet


def create_parse_table(grammar_dict, first_sets, follow_sets):
    # Initialize the parse table as a dictionary of dictionaries
    parse_table = {nt: {} for nt in grammar_dict}
    
    # Fill in the parse table based on First and Follow sets
    for nt, productions in grammar_dict.items():
        for production in productions:
            # Calculate the First set of the production
            production_first_set = set()
            idx = 0
            while idx < len(production):
                symbol = production[idx]
                
                if symbol in grammar_dict:
                    # If the symbol is a non-terminal
                    # Add the First set of the non-terminal to production first set, excluding epsilon
                    production_first_set.update(first_sets[symbol] - {'epsilon'})
                    
                    # If epsilon is in the First set of the non-terminal
                    if 'epsilon' in first_sets[symbol]:
                        idx += 1
                        # If we have reached the end, continue adding epsilon
                        if idx == len(production):
                            production_first_set.add('epsilon')
                        continue
                
                else:
                    # If the symbol is a terminal
                    production_first_set.add(symbol)
                    break

            # If the production's First set contains epsilon, add the production under the Follow set of the non-terminal
            if 'epsilon' in production_first_set:
                # Add epsilon to the parse table under the Follow set of the non-terminal
                for follow_symbol in follow_sets[nt]:
                    if follow_symbol in parse_table[nt]:
                        parse_table[nt][follow_symbol] += f", {production}"
                    else:
                        parse_table[nt][follow_symbol] = production
                # Remove epsilon from the production first set for filling the table
                production_first_set.remove('epsilon')
            
            # Fill in the parse table with the production for each terminal in production first set
            for terminal in production_first_set:
                if terminal in parse_table[nt]:
                    parse_table[nt][terminal] += f", {production}"
                else:
                    parse_table[nt][terminal] = production
    
    return parse_table





def print_parse_table(parse_table, terminals):
    # Get the list of non-terminals
    non_terminals = list(parse_table.keys())
    
    # Calculate the width for each column based on the maximum length of the values
    col_widths = {}
    for terminal in terminals:
        max_width = max(len(terminal), max(len(parse_table[nt].get(terminal, '')) for nt in non_terminals))
        col_widths[terminal] = max_width
    col_widths['non-terminals'] = max(len('non-terminals'), max(len(nt) for nt in non_terminals))
    
    # Print the header row (terminals)
    header_row = f"{'non-terminals':<{col_widths['non-terminals']}}"
    for terminal in terminals:
        header_row += f" | {terminal:<{col_widths[terminal]}}"
    print(header_row)
    
    # Print a separator line
    separator_line = '-' * len(header_row)
    print(separator_line)
    
    # Print each row for each non-terminal
    for nt in non_terminals:
        # Start with the non-terminal name
        row = f"{nt:<{col_widths['non-terminals']}}"
        
        # Add the productions for each terminal
        for terminal in terminals:
            production = parse_table[nt].get(terminal, '')
            row += f" | {production:<{col_widths[terminal]}}"
        
        print(row)

def getTerminalsWithParseTable(grammar_dict):
    terminals = set()
    first_sets = FirstSet.compute_first_sets(grammar_dict)
    follow_sets = FollowSet.compute_follow_sets(grammar_dict, first_sets)
    for first_set in first_sets.values():
        terminals.update(first_set)
    for follow_set in follow_sets.values():
        terminals.update(follow_set)
    terminals.discard('epsilon')
    
    # Add the special terminal '$'
    terminals.add('$')
    
    # Sort terminals for consistent output
    terminals = sorted(terminals)
    
    # Create the parse table
    parse_table = create_parse_table(grammar_dict, first_sets, follow_sets)
    
    return terminals, parse_table