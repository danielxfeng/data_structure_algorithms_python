# python3
from sys import stdin
from bisect import bisect_left, bisect_right

import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

# logger.setLevel(logging.DEBUG)
logging.Logger.disabled = True


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    assert len(starts) == len(ends)

    lst_data = starts + ends + points
    lst_type = [0] * len(starts) + [2] * len(ends) + [1] * len(points)

    assert len(lst_data) == len(lst_type)

    logger.debug("send to merge_sort %s, %s, %d, %d" % (str(lst_data), str(lst_type), 0, len(lst_data) - 1))

    s_data, s_type = merge_sort(lst_data, lst_type)
    logger.debug("final s_data is: %s, %s" % (s_data, s_type))

    count = {}
    csg = 0
    for d, t in zip(s_data, s_type):
        if t == 0:
            csg += 1
        elif t == 2:
            csg -= 1
        elif t == 1:
            if csg < 0:
                count[d] = 0
            else:
                count[d] = csg


    res = [count[i] for i in points]
    logger.debug("final result is: %s" % res)

    return res


def merge_sort(lst_data, lst_type):
    length = len(lst_data)

    if length <= 1:
        return lst_data, lst_type

    mid = length // 2

    s_data, s_type = merge(merge_sort(lst_data[0: mid], lst_type[0: mid]),
                           merge_sort(lst_data[mid: length], lst_type[mid: length]))

    return s_data, s_type


def merge(left, right):
    l_data, l_type = left
    r_data, r_type = right
    s_data = []
    s_type = []
    while True:
        if (len(l_data) == 0) and (len(r_data) == 0):
            break

        if len(l_data) == 0:
            s_data += r_data
            s_type += r_type
            break

        if len(r_data) == 0:
            s_data += l_data
            s_type += l_type
            break

        if l_data[0] > r_data[0]:
            do_right(r_data, r_type, s_data, s_type)
        elif l_data[0] < r_data[0]:
            do_left(l_data, l_type, s_data, s_type)
        elif l_data[0] == r_data[0]:
            if l_type[0] > r_type[0]:
                do_right(r_data, r_type, s_data, s_type)
            elif l_type[0] < r_type[0]:
                do_left(l_data, l_type, s_data, s_type)
            elif l_data[0] == r_data[0]:
                do_left(l_data, l_type, s_data, s_type)
                do_right(r_data, r_type, s_data, s_type)

    return s_data, s_type


def do_right(r_data, r_type, s_data, s_type):
    s_data.append(r_data[0])
    s_type.append(r_type[0])
    r_data.pop(0)
    r_type.pop(0)
    return


def do_left(l_data, l_type, s_data, s_type):
    s_data.append(l_data[0])
    s_type.append(l_type[0])
    l_data.pop(0)
    l_type.pop(0)
    return


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
