import heapq

# 1. Manhattan Heuristic
def manhattan(curr_state, goal_state, size):
    return sum(
        abs(curr_state.index(tile)//size - goal_state.index(tile)//size) +
        abs(curr_state.index(tile)%size - goal_state.index(tile)%size)
        for tile in curr_state if tile
    )

# 2. Generate Neighbor States
def get_neighbors(state, size):
    zero_pos = state.index(0)
    row, col = divmod(zero_pos, size)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    neighbors = []

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < size and 0 <= nc < size:
            swap_pos = nr * size + nc
            new_state = list(state)
            new_state[zero_pos], new_state[swap_pos] = new_state[swap_pos], new_state[zero_pos]
            neighbors.append(tuple(new_state))

    return neighbors

# 3. A* Solver
def solve(start_state, goal_state, size):
    # priority queue: (f_score, g_score, state, path)
    pq = [(manhattan(start_state, goal_state, size), 0, start_state, [start_state])]
    visited = set()

    while pq:
        f_score, g_score, curr, path = heapq.heappop(pq)

        if curr == goal_state:
            return path

        if curr not in visited:
            visited.add(curr)

            for next_state in get_neighbors(curr, size):
                new_path = path + [next_state]
                new_g = g_score + 1
                new_f = new_g + manhattan(next_state, goal_state, size)
                heapq.heappush(pq, (new_f, new_g, next_state, new_path))

    return None

# Driver Code
if __name__ == "__main__":
    size = 3

    start_state = (
        1, 2, 3,
        4, 0, 6,
        7, 5, 8
    )

    goal_state = (
        1, 2, 3,
        4, 5, 6,
        7, 8, 0
    )

    result_path = solve(start_state, goal_state, size)

    if result_path:
        print(f"Solved in {len(result_path)-1} moves:\n")
        for step_num, state in enumerate(result_path):
            print(f"Step {step_num}:")
            for i in range(0, size*size, size):
                print(state[i:i+size])
            print()
    else:
        print("No solution found.")
