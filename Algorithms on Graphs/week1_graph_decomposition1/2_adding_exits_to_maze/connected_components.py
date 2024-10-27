#Uses python3

import sys


def number_of_components(adj):
    # print(adj)
    ccs = [1] * len(adj)
    ccs, cc = dfs(adj, ccs)
    return cc


def dfs(adj, ccs):
    if_visited = [False] * len(adj)
    cc = 1
    for i in range(len(adj)):
        if if_visited[i] is False:
            if_visited, ccs = explore(i, ccs, cc, if_visited, adj)
            cc += 1

    if cc == 1:
        res = 1
    else:
        res = cc - 1
    return ccs, res


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
        ),
        (
            (4, 3),
            (1, 2),
            (3, 2),
            (4, 3),
        ),
    )
    for td in test_data:
        vertices = td[0][0]
        adj = [[] for _ in range(vertices)]
        for i in td[1:]:
            adj[i[0] - 1].append(i[1] - 1)
            adj[i[1] - 1].append(i[0] - 1)
        print(number_of_components(adj))


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))


if __name__ == '__main__':
    main()
    # run_tests()
