#Uses python3

import sys
import queue


def bipartite(adj):
    dic = {}
    for v in range(len(adj)):
        dic[v] = 0
    for v in range(len(adj)):
        if dic[v] == 0:
            res = bfs(adj, dic, v)
            if res == 0:
                return 0
            
    return 1
    
    
def bfs(adj, dic, start):
    # print(adj)
    q = queue.Queue()
    q.put(start)
    dic[start] = 1
    res = 1
    while q.qsize() > 0:
        u = q.get()
        # print("u", u)
        for v in adj[u]:
            if dic[v] == 0:
                q.put(v)
                dic[v] = -1 * dic[u]
            elif dic[v] == dic[u]:
                res = 0
    
    return res


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
            (6, 4),
            (5, 2),
            (4, 2),
            (3, 4),
            (1, 4),
        ),
    )
    for td in test_data:
        vertices = td[0][0]
        adj = [[] for _ in range(vertices)]
        for i in td[1:]:
            adj[i[0] - 1].append(i[1] - 1)
            adj[i[1] - 1].append(i[0] - 1)
        print(bipartite(adj))
        
        
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
    print(bipartite(adj))
    
    
if __name__ == '__main__':
    main()
    # run_tests()
