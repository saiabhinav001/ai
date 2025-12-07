import time, math

def alphabeta(depth, idx, isMax, scores, d, alpha, beta):
    if depth == d: return scores[idx]
    for i in range(2):
        val = alphabeta(depth+1, idx*2+i, not isMax, scores, d, alpha, beta)
        if isMax:
            alpha = max(alpha, val)
            if beta <= alpha: break
        else:
            beta = min(beta, val)
            if beta <= alpha: break
    return alpha if isMax else beta

scores = [3, 5, 2, 9, 12, 5, 23, 23]
start = time.time()
print("Alpha-Beta:", alphabeta(0, 0, True, scores, 3, float('-inf'), float('inf')))
print("Time:", time.time() - start, "seconds")