import math
from collections import deque


def BFS(capacity, start, end):
    pred = {}
    pred[start] = start
    q = deque()
    q.append([start, math.inf])
    while q:
        v, flow = q.popleft()
        for nbr in capacity[v]:
            if not nbr in pred and capacity[v][nbr] > 0:
                pred[nbr] = v
                newFlow = min(flow, capacity[v][nbr])
                q.append[nbr, newFlow]
                if nbr == end:
                    return newFlow, pred
    return 0, pred


def EdmondsKarp(capacity, start, end):
    maxFlow = 0
    flow, pred = BFS(capacity, start, end)
    while flow > 0:
        v = end
        while v != start:
            u = pred[v]
            capacity[u][v] -= flow
            capacity[v][u] += flow
            v = u
        maxFlow += flow
        flow, pred = BFS(capacity, start, end)
    return maxFlow