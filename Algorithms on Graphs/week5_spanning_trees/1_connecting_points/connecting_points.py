#Uses python3
import sys
import math


def minimum_distance(x, y):
    result = 0.
    
    # print(x, y)
    length = len(x)
    parent = [None] * length
    cost = [None] * length
    visited = [False] * length
    cost[0] = 0
    q = [0]
    while q:
        v = get_min(q, cost)
        visited[v] = True
        for z in range(length):
            if z == v:
                continue
            distance = get_distance(x[v], y[v], x[z], y[z])
            if not visited[z] and (cost[z] is None or cost[z] > distance):
                cost[z] = distance
                parent[z] = v
                q.append(z)
    
    for c in cost:
        result += c
    
    return result


def get_min(q, cost):
    mini = None
    for v in q:
        if mini is None or cost[v] < cost[mini]:
            mini = v
    q.remove(mini)
    return mini


def get_distance(ax, ay, bx, by):
    return abs(((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5)


def run_tests():
    test_data = (
        (
            (4,),
            (0, 0),
            (0, 1),
            (1, 0),
            (1, 1),
        ),
        (
            (5,),
            (0, 0),
            (0, 2),
            (1, 1),
            (3, 0),
            (3, 2),
        ),
    )
    for td in test_data:
        x = []
        y = []
        for t in td[1:]:
            x.append(t[0])
            y.append(t[1])
        print("{0:.9f}".format(minimum_distance(x, y)))
    

def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
    
    
if __name__ == '__main__':
    main()
    # run_tests()
