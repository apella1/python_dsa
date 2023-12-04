import heapq
import math


def apportion_congress(s_population, R):
    states = len(s_population)
    reps = [1] * states
    PQ = []

    # give every state its first representative
    for s in range(states):
        heapq.heappush(PQ, (s_population[s] / math.sqrt(2), s))

    # allocate remaining n - R reps
    for i in range(states - R):
        # start from 0 instead of 1
        s = heapq.heappop(PQ)[1]
        reps[s] += 1
        priority = s_population[s] / math.sqrt(reps[s] * (reps[s] + 1))
        heapq.heappush(PQ, (priority, s))
    return reps


Pop = [100, 200, 300, 400, 500]
R = 2
print(apportion_congress(Pop, R))
