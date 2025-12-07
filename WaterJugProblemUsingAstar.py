import heapq

# Heuristic: how far any jug is from target
def heuristic(x, y, target):
    return min(abs(x - target), abs(y - target))

# Generate all possible next states
def get_successors(x, y, jug1, jug2):
    successors = []
    successors.append((jug1, y, 'fill x'))          # Fill jug X
    successors.append((x, jug2, 'fill y'))          # Fill jug Y
    successors.append((0, y, 'empty x'))            # Empty jug X
    successors.append((x, 0, 'empty y'))            # Empty jug Y

    # Pour X → Y
    pour = min(x, jug2 - y)
    successors.append((x - pour, y + pour, 'pour x to y'))

    # Pour Y → X
    pour = min(y, jug1 - x)
    successors.append((x + pour, y - pour, 'pour y to x'))

    return successors

# A* search for water jug problem
def astar(jug1, jug2, target):
    heap = []
    visited = set()
    start_state = (0, 0, [], 0)       # (x, y, path, g_cost)
    heapq.heappush(heap, (heuristic(0, 0, target), start_state))

    while heap:
        f_cost, (x, y, path, g_cost) = heapq.heappop(heap)

        if (x, y) in visited:
            continue
        visited.add((x, y))

        if x == target or y == target:
            print("Goal state:", x, y)
            return path

        for nx, ny, action in get_successors(x, y, jug1, jug2):
            if (nx, ny) not in visited:
                new_path = path + [action]
                new_g = g_cost + 1
                h = heuristic(nx, ny, target)
                heapq.heappush(heap, (new_g + h, (nx, ny, new_path, new_g)))

    return "No solution"

# Driver code
jug1 = 3
jug2 = 4
target = 2
solution = astar(jug1, jug2, target)
print("Solution steps:", solution)
