#Uses python3

import sys


def reach(adj, x, y):
    # print(adj, x, y)
    ccs = [1] * len(adj)
    ccs = dfs(adj, ccs)
    if ccs[x] == ccs[y]:
        return 1
    return 0


def dfs(adj, ccs):
    if_visited = [False] * len(adj)
    cc = 1
    for i in range(len(adj)):
        if if_visited[i] is False:
            if_visited, ccs = explore(i, ccs, cc, if_visited, adj)
            cc += 1
    return ccs


def explore(i, ccs, cc, if_visited, adj):
    if_visited[i] = True
    ccs[i] = cc
    for w in adj[i]:
        if if_visited[w] is False:
            if_visited, ccs = explore(w, ccs, cc, if_visited, adj)
    return if_visited, ccs


def run_tests():
    test_data = (
        (
            (4, 4),
            (1, 2),
            (3, 2),
            (4, 3),
            (1, 4),
            (1, 4)
        ),
        (
            (4, 2),
            (1, 2),
            (3, 2),
            (1, 4)
        )
    )
    for td in test_data:
        vertices = td[0][0]
        adj = [[] for _ in range(vertices)]
        for (a, b) in td[1: -1]:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)
        print(reach(adj, td[-1][0] - 1, td[-1][1] - 1))


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))


if __name__ == '__main__':
    main()
    # run_tests()
