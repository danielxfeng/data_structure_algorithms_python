#Uses python3

import sys

sys.setrecursionlimit(200000)


def number_of_strongly_connected_components(adj):
    result = 0
    
    if_visited = []
    orders = []
    radj = get_reversed(adj)
    for i in range(len(adj)):
        explore(i, if_visited, radj, orders)
            
    orders = list(reversed(orders))
    # print("orders", [i + 1 for i in orders])
    
    if_visited = []
    for i in orders:
        # print("i", i)
        length = len(if_visited)
        explore(i, if_visited, adj, [])
        if len(if_visited) > length:
            # print("res", result)
            result += 1

    return result


def get_reversed(adj):
    radj = [[] for _ in range(len(adj))]
    
    for v in range(len(adj)):
        for e in adj[v]:
            radj[e].append(v)
    
    return radj


def explore(i, if_visited, adj, orders):
    if i in if_visited:
        return
    
    if_visited.append(i)
    for w in adj[i]:
        explore(w, if_visited, adj, orders)

    orders.append(i)
    return


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
        print(number_of_strongly_connected_components(adj))


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))


if __name__ == '__main__':
    main()
    # run_tests()
