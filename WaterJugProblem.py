from collections import deque

def water_jug_bfs(cap1, cap2, target):
    # State representation: (jug1, jug2, path_of_actions)
    queue = deque([(0, 0, [])])
    visited = set()

    while queue:
        j1, j2, path = queue.popleft()

        # 1. Goal Test
        if j1 == target or j2 == target:
            return path

        # 2. Add current state to visited
        if (j1, j2) in visited:
            continue
        visited.add((j1, j2))

        # 3. Generate all 6 possible next moves
        next_states = [
            (cap1, j2, "Fill J1"),
            (j1, cap2, "Fill J2"),
            (0,    j2, "Empty J1"),
            (j1,   0,  "Empty J2"),
            # Pour J1 -> J2 (Amount is min of J1 or space left in J2)
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2), "Pour J1->J2"),
            # Pour J2 -> J1 (Amount is min of J2 or space left in J1)
            (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1), "Pour J2->J1")
        ]

        # 4. Add next moves to queue ONLY if not visited yet
        for n_j1, n_j2, action in next_states:
            if (n_j1, n_j2) not in visited:
                queue.append((n_j1, n_j2, path + [action]))

    return "No solution found"

# Driver Code
result = water_jug_bfs(5, 3, 2)
for step in result:
    print(step)