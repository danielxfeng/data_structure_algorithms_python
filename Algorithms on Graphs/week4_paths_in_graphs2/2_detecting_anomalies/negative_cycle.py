#Uses python3

import sys


def negative_cycle(adj, cost):
    
    length = len(adj)
    dist = [-1] * length
    dist[0] = 0
    
    for i in range(length):
        if_return = False
        if i == length - 1:
            if_return = True
            
        res = bellman_ford(adj, length, dist, cost, if_return)
        
        if res == 1:
            return 1
        
    return 0


def bellman_ford(adj, length, dist, cost, if_return):
    for u in range(length):
        for i, v in enumerate(adj[u]):
            if dist[v] == -1 or dist[v] > dist[u] + cost[u][i]:
                if if_return:
                    return 1
                dist[v] = dist[u] + cost[u][i]
                
    return 0
    
    
def run_tests():
    test_data = (
        (
            (4, 4),
            (1, 2, -5),
            (4, 1, 2),
            (2, 3, 2),
            (3, 1, 1),
        ),
    )
    for td in test_data:
        vertices = td[0][0]
        adj = [[] for _ in range(vertices)]
        cost = [[] for _ in range(vertices)]
        for i in td[1:]:
            adj[i[0] - 1].append(i[1] - 1)
            cost[i[0] - 1].append(i[2])
        print(negative_cycle(adj, cost))
        
        
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
    print(negative_cycle(adj, cost))


if __name__ == '__main__':
    main()
    # run_tests()
    