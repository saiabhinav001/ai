def solve_n_queens(n):
    cols, diag1, diag2 = set(), set(), set()
    solutions = []

    def is_safe(row, col):
        return (col not in cols and
                (row - col) not in diag1 and
                (row + col) not in diag2)

    def backtrack(row, path):
        if row == n:
            solutions.append(path)
            return

        for col in range(n):
            if is_safe(row, col):
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                backtrack(row + 1, path + [col])
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
    backtrack(0, [])

    for sol in solutions:
        for col in sol:
            print("." * col + "Q" + "." * (n - col - 1))
        print()

solve_n_queens(4)
