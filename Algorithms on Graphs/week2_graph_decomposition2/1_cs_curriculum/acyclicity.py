#Uses python3

import sys
# sys.setrecursionlimit(100000)


def acyclic(adj):
    # print(adj)
    if dfs(adj):
        return 1
    return 0


def dfs(adj):
    if_visited = [False] * len(adj)
    if_cycle = False
    for i in range(len(adj)):
        # print("i start")
        if if_visited[i]:
            continue

        if_cycle = explore(i, adj, [], if_visited)
        if if_cycle is True:
            return True
    return if_cycle


def explore(i, adj, path, if_visited):
    if i in path:
        return True

    if_visited[i] = True
    path.append(i)

    for w in adj[i]:

        if explore(w, adj, path, if_visited):
            return True

    path.remove(i)

    return False


def run_tests():
    test_data = (
        (
            (4, 4),
            (1, 2),
            (4, 1),
            (2, 3),
            (3, 1),
        ),
        (
            (5, 7),
            (1, 2),
            (2, 3),
            (1, 3),
            (3, 4),
            (1, 4),
            (2, 5),
            (3, 5),
        ),
        (
            (10, 20),
            (7, 8),
            (4, 10),
            (3, 2),
            (1, 3),
            (4, 9),
            (2, 6),
            (8, 3),
            (8, 2),
            (6, 1),
            (6, 10),
            (10, 6),
            (1, 4),
            (3, 8),
            (1, 5),
            (8, 9),
            (5, 3),
            (3, 4),
            (5, 1),
            (8, 5),
            (8, 4),
        ),
    )
    for td in test_data:
        vertices = td[0][0]
        adj = [[] for _ in range(vertices)]
        for i in td[1:]:
            adj[i[0] - 1].append(i[1] - 1)
        print(acyclic(adj))


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))


if __name__ == '__main__':
    main()
    # run_tests()
