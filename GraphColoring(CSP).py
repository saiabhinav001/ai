colors = ['Red', 'Green', 'Blue']
states = ['A', 'B', 'C', 'D']
adj = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

def is_valid(state, color, assignment):
    for neighbor in adj[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(states):
        return assignment

    for state in states:
        if state not in assignment:
            var = state
            break

    for color in colors:
        if is_valid(var, color, assignment):
            assignment[var] = color
            result = backtrack(assignment)
            if result is not None:
                return result
            assignment.pop(var) 

    return None

solution = backtrack({})
print("Solution:", solution)
