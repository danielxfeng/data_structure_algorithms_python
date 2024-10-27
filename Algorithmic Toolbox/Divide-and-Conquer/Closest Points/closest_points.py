# python3
import logging
import random
from collections import namedtuple
from itertools import combinations
from math import sqrt


logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

# logger.setLevel(logging.DEBUG)
logging.Logger.disabled = True

Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2
    # return round(((first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2), 8)


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def min_d(points, if_d=False, d=0):
    if if_d:
        mv = d
    else:
        mv = float("inf")

    for i in range(len(points)):
        if if_d:
            end = min(15, len(points))
        else:
            end = len(points)
        for j in range(i + 1, end):
            if if_d and (abs(points[i][1] - points[j][1]) > d):
                break
            distance = distance_squared(points[i], points[j])
            if min(mv, distance) == distance:
                mv = distance

    return mv


def minimum_distance_squared(points):
    points = sorted(points, key=lambda p: p[0])
    # points = quick_sort(points, 0, len(points) - 1, 0)
    logging.debug("sorted points is %s" % str(points))

    res = find_min(points, 0, len(points) - 1)

    logging.debug("res is %s" % "{0:.9f}".format(sqrt(res)))
    return res


def find_min(points, left, right):
    if right - left <= 3:
        return min_d(points[left: right + 1])

    mid = left + ((right - left) // 2)

    logging.debug("dl is: %d, %d" % (left, mid))
    logging.debug("dr is: %d, %d" % (mid + 1, right))
    dl = find_min(points, left, mid)
    dr = find_min(points, mid + 1, right)

    d = min(dl, dr)
    logging.debug("d is %s" % "{0:.9f}".format(sqrt(d)))

    if d == 0:
        return d

    mid_point = points[mid]
    strip = [point for point in points[left: right + 1] if ((point[0] - mid_point[0]) < d)]
    strip = sorted(strip, key=lambda s: s[1])
    # strip = quick_sort(strip, 0, len(strip) - 1, 1)
    min_strip = min_d(strip, True, d)
    logging.debug("min_strip is %s" % "{0:.9f}".format(sqrt(min_strip)))

    return min(d, min_strip)


def quick_sort(points, left, right, key):
    if left >= right:
        return points

    k = random.randint(left, right)
    swap(points, left, k)

    logging.debug("quick sort partition: %s, %d, %d, %d" % (str(points), left, right, key))

    k = partition(points, left, right, key)
    if k > 0:
        quick_sort(points, left, k - 1, key)
    quick_sort(points, k + 1, right, key)

    logging.debug("sorted point is: %s" % str(points))
    return points


def partition(points, left, right, key):

    logging.debug("partition in is: %d, %d" % (left, right))
    if left >= right:
        return

    j = left
    i = left + 1

    while i <= right:
        if points[i][key] <= points[left][key]:
            j += 1
            swap(points, i, j)

        i += 1

    swap(points, left, j)

    logging.debug("partition result is: %d" % j)
    return j


def swap(points, a, b):
    points[a], points[b] = points[b], points[a]


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
