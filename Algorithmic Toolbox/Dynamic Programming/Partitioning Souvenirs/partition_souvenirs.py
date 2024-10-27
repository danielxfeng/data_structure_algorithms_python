from itertools import product
from sys import stdin

import logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

# logger.setLevel(logging.DEBUG)
logging.Logger.disabled = True


def partition3_naive(values):
    for c in product(range(3), repeat=len(values)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(values[k] for k in range(len(values)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)

    length = len(values)
    target_value, mod = divmod(sum(values), 3)

    if (length < 3) or mod > 0 or max(values) > target_value:
        return 0

    matrix = [[[False] * (length + 1) for _ in range(target_value + 1)] for __ in range(target_value + 1)]

    for i in range(length + 1):
        value = values[i - 1]
        for w1 in range(target_value + 1):
            r1 = w1 - value
            for w2 in range(target_value + 1):
                r2 = w2 - value

                if w1 == 0 and w2 == 0:
                    matrix[0][0][i] = True

                elif value == w1 and True in [matrix[m][w2][i - 1] for m in range(target_value + 1)]:
                    print("1", w1, w2, i - 1)
                    matrix[w1][w2][i] = True
                elif value == w2 and True in [matrix[w1][m][i - 1] for m in range(target_value + 1)]:
                    print("2", w1, w2, i - 1)
                    matrix[w1][w2][i] = True
                elif matrix[w1][w2][i - 1]:
                    print("3", w1, w2, i - 1)
                    matrix[w1][w2][i] = True
                elif r1 > 0 and matrix[r1][w2][i - 1]:
                    print("4", w1, w2, i - 1)
                    matrix[w1][w2][i] = True
                elif r2 > 0 and matrix[w1][r2][i - 1]:
                    print("5", w1, w2, i - 1)
                    matrix[w1][w2][i] = True

    c1 = 0
    for m in matrix:
        print("c1 is: %d" % c1)
        c1 += 1
        c2 = 0
        for n in m:
            print("c2 is: %d" % c2)
            print(n)
            c2 += 1

    res = matrix[target_value][target_value][length]
    if res is True:
        return 1
    return 0


if __name__ == '__main__':
    #input_n, *input_values = list(map(int, stdin.read().split()))
    #assert input_n == len(input_values)
    #print(partition3(input_values))
    print(partition3([2,2,2]))