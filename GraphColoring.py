# CSP using Backtracking (Map Coloring Example)

colors = ['Red', 'Green', 'Blue']
states = ['A', 'B', 'C', 'D']
adj = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

def is_valid(state, color, assign):
    for n in adj[state]:
        if n in assign and assign[n] == color:
            return False
    return True

def backtrack(assign):
    if len(assign) == len(states):
        return assign
    var = [s for s in states if s not in assign][0]
    for c in colors:
        if is_valid(var, c, assign):
            assign[var] = c
            result = backtrack(assign)
            if result: return result
            assign.pop(var)
    return None

solution = backtrack({})
print("Solution:", solution)