#Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    # print(adj, cost, s, t)
    dist = [-1] * len(adj)
    visited = [False] * len(adj)
    prev = [None] * len(adj)
    dist[s] = 0
    h = queue.PriorityQueue()
    h.put((0, s))
    while not h.empty():
        u = h.get()
        visited[u[1]] = True
        # print("u: ", u)
        # print("adj[u[1]]: ", adj[u[1]])
        for i, v in enumerate(adj[u[1]]):
            # print("dist[v]: ", dist[v], "dist[u[1]]: ", dist[u[1]], "u[0]: ", u[0], "u[1]: ", u[1], "cost[u[1]][i]", cost[u[1]][i])
            if (visited[v] is False) and (dist[v] == -1 or dist[v] > dist[u[1]] + cost[u[1]][i]):
                dist[v] = dist[u[1]] + cost[u[1]][i]
                prev[v] = u[1]
                # print("put", dist[v], v)
                h.put((dist[v], v))
                
    # print("dist: ", dist, "dist[t]: ", dist[t])
    return dist[t]


def run_tests():
    test_data = (
        (
            (4, 4),
            (1, 2, 1),
            (4, 1, 2),
            (2, 3, 2),
            (1, 3, 5),
            (1, 3),
        ),
        (
            (5, 9),
            (1, 2, 4),
            (1, 3, 2),
            (2, 3, 2),
            (3, 2, 1),
            (2, 4, 2),
            (3, 5, 4),
            (5, 4, 1),
            (2, 5, 3),
            (3, 4, 4),
            (1, 5),
        ),
        (
            (3, 3),
            (1, 2, 7),
            (1, 3, 5),
            (2, 3, 2),
            (3, 2),
        ),
    )
    for td in test_data:
        vertices = td[0][0]
        adj = [[] for _ in range(vertices)]
        cost = [[] for _ in range(vertices)]
        for i in td[1:-1]:
            adj[i[0] - 1].append(i[1] - 1)
            cost[i[0] - 1].append(i[2])
        s, t = td[-1][0] - 1, td[-1][1] - 1
        print(distance(adj, cost, s, t))
        
        
def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
    
    
if __name__ == '__main__':
    main()
    # run_tests()
    
