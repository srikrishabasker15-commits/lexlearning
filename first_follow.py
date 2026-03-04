
from collections import defaultdict

# Grammar dictionary
grammar = defaultdict(list)

# Input Grammar
# Example:
# E -> T E'
# E' -> + T E' | ε
# T -> F T'
# T' -> * F T' | ε
# F -> ( E ) | id

grammar["E"] = [["T", "E'"]]
grammar["E'"] = [["+", "T", "E'"], ["ε"]]
grammar["T"] = [["F", "T'"]]
grammar["T'"] = [["*", "F", "T'"], ["ε"]]
grammar["F"] = [["(", "E", ")"], ["id"]]

first = defaultdict(set)
follow = defaultdict(set)
start_symbol = "E"

# FIRST function
def compute_first(symbol):
    if symbol not in grammar:
        return {symbol}

    if first[symbol]:
        return first[symbol]

    for production in grammar[symbol]:
        for sym in production:
            sym_first = compute_first(sym)
            first[symbol].update(sym_first - {"ε"})
            if "ε" not in sym_first:
                break
        else:
            first[symbol].add("ε")

    return first[symbol]

# FOLLOW function
def compute_follow():
    follow[start_symbol].add("$")

    changed = True
    while changed:
        changed = False
        for head, productions in grammar.items():
            for production in productions:
                trailer = follow[head].copy()
                for symbol in reversed(production):
                    if symbol in grammar:
                        before = len(follow[symbol])
                        follow[symbol].update(trailer)
                        if "ε" in first[symbol]:
                            trailer.update(first[symbol] - {"ε"})
                        else:
                            trailer = first[symbol]
                        if len(follow[symbol]) > before:
                            changed = True
                    else:
                        trailer = {symbol}

# Compute FIRST
for non_terminal in grammar:
    compute_first(non_terminal)

# Compute FOLLOW
compute_follow()

# Display results
print("FIRST sets:")
for nt in grammar:
    print(f"FIRST({nt}) = {first[nt]}")

print("\nFOLLOW sets:")
for nt in grammar:
    print(f"FOLLOW({nt}) = {follow[nt]}")
