import time, math

def minimax(depth, idx, isMax, scores, d):
    if depth == d: return scores[idx]
    left = minimax(depth+1, idx*2, not isMax, scores, d)
    right = minimax(depth+1, idx*2+1, not isMax, scores, d)
    return max(left, right) if isMax else min(left, right)

scores = [3, 5, 2, 9, 12, 5, 23, 23]
start = time.time()
print("Minimax:", minimax(0, 0, True, scores, 3))
print("Time:", time.time() - start, "seconds")