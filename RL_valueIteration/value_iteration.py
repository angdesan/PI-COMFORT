from probability import probs as P
from rewards import R

N = 107
S = [*range(0, N+1)]
A = [0, 1, 2]
gamma = 0.2


def value_iteration(S, A, P, R, gamma):
    V = {s: 0 for s in S}
    i = 0
    while True:
        oldV = V.copy()
        optimal_policy = {s: 0 for s in S}
        Qs = []
        for s in S:

            Q = {}
            for a in A:
                Q[a] = R[s][a] + gamma*sum(P[s][a][s_next] * oldV[s_next]
                                           for s_next in S)
            Qs.append(Q)
            V[s] = max(Q.values())
            optimal_policy[s] = max(Q, key=Q.get)
        print(oldV == V)
        i += 1
        if all(oldV[s] == V[s] for s in S):
            break
    return V, optimal_policy


V, optimal_policy = value_iteration(S, A, P, R, gamma)






# Menu principal
