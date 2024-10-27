# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):

    lst = sorted(segments, key=lambda x: x[1])
    point = 0
    res = []
    for i in range(len(lst)):
        begin, end = lst[i]
        if begin > point:
            res.append(end)
            point = end

    return res


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    #input_segments = [(1,4), (1,3),(5,6),(6,8)]
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
