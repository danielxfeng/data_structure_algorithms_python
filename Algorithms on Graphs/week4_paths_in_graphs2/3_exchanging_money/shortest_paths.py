#Uses python3

import sys


def shortet_paths(adj, cost, s, distance, reachable, shortest):
    # print("adj", adj, "cost", cost, "s", s)
    length = len(adj)
    distance[s] = 0
    reachable[s] = 1
    q = []
    for i in range(length):
        for u in range(length):
            # print("u", u)
            for iv, v in enumerate(adj[u]):
                if distance[v] > distance[u] + cost[u][iv]:
                    if i == length - 1:
                        if v not in q:
                            # print("-", v)
                            q.append(v)
                    else:
                        distance[v] = distance[u] + cost[u][iv]
                        # print("*", v)
                        reachable[v] = 1

    visited = [False] * length
    while q:
        u = q.pop(0)
        visited[u] = True
        shortest[u] = 0
        for v in adj[u]:
            if not visited[v] and v not in q:
                q.append(v)


def run_tests():
    test_data = (
        (
            (6, 7),
            (1, 2, 10),
            (2, 3, 5),
            (1, 3, 100),
            (3, 5, 7),
            (5, 4, 10),
            (4, 3, -18),
            (6, 1, -1),
            (1,),
        ),
        (
            (5, 4),
            (1, 2, 1),
            (4, 1, 2),
            (2, 3, 2),
            (3, 1, -5),
            (4,),
        ),
    )
    for td in test_data:
        vertices = td[0][0]
        adj = [[] for _ in range(vertices)]
        cost = [[] for _ in range(vertices)]
        for i in td[1:-1]:
            adj[i[0] - 1].append(i[1] - 1)
            cost[i[0] - 1].append(i[2])
        s = td[-1][0] - 1
        distance = [10 ** 19] * vertices
        reachable = [0] * vertices
        shortest = [1] * vertices
        shortet_paths(adj, cost, s, distance, reachable, shortest)
        for x in range(vertices):
            if reachable[x] == 0:
                print('*')
            elif shortest[x] == 0:
                print('-')
            else:
                print(distance[x])
        
    
def main():
    u_input = sys.stdin.read()
    data = list(map(int, u_input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])


if __name__ == '__main__':
    main()
    # run_tests()
    