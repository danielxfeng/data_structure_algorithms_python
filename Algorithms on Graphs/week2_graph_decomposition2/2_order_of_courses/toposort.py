#Uses python3

import sys


def dfs(adj):
    if_visited = [False] * len(adj)
    orders = []
    for i in range(len(adj)):
        if if_visited[i] is False:
            explore(i, if_visited, adj, orders)

    return orders


def explore(i, if_visited, adj, orders):
    if_visited[i] = True
    for w in adj[i]:
        if if_visited[w] is False:
            explore(w, if_visited, adj, orders)

    orders.append(i)
    return


def toposort(adj):
    # print(adj)
    orders = list(reversed(dfs(adj)))
    # print(orders)
    return orders


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')


def run_tests():
    test_data = (
        (
            (4, 3),
            (1, 2),
            (4, 1),
            (3, 1),
        ),
        (
            (4, 1),
            (3, 1),
        ),
        (
            (5, 7),
            (2, 1),
            (3, 2),
            (3, 1),
            (4, 3),
            (4, 1),
            (5, 2),
            (5, 3),
        ),
    )
    for td in test_data:
        vertices = td[0][0]
        adj = [[] for _ in range(vertices)]
        for i in td[1:]:
            adj[i[0] - 1].append(i[1] - 1)
        order = toposort(adj)
        for x in order:
            print(x + 1, end=' ')


if __name__ == '__main__':
    main()
    # run_tests()

