#Uses python3

import sys
import queue


def distance(adj, s, t):
    # print(adj, s, t)
    dic = {}
    for v in range(len(adj)):
        dic[v] = -1
    dic[s] = 0
    q = queue.Queue()
    q.put(s)
    while q.qsize() > 0:
        u = q.get()
        # print("u", u)
        for v in adj[u]:
            if dic[v] == -1:
                q.put(v)
                dic[v] = dic[u] + 1
    # print(dic[t])
    
    return dic[t]


def run_tests():
    test_data = (
        (
            (4, 4),
            (1, 2),
            (4, 1),
            (2, 3),
            (3, 1),
            (2, 4),
        ),
        (
            (5, 4),
            (5, 2),
            (1, 3),
            (3, 4),
            (1, 4),
            (3, 5),
        ),
    )
    for td in test_data:
        vertices = td[0][0]
        adj = [[] for _ in range(vertices)]
        for i in td[1:-1]:
            adj[i[0] - 1].append(i[1] - 1)
            adj[i[1] - 1].append(i[0] - 1)
        s, t = td[-1][0] - 1, td[-1][1] - 1
        print(distance(adj, s, t))
        

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))


if __name__ == '__main__':
    main()
    # run_tests()
    