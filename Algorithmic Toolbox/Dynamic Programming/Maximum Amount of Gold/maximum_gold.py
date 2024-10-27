# python3

from sys import stdin

import logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

# logger.setLevel(logging.DEBUG)
logging.Logger.disabled = True


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)

    length = len(weights)

    matrix = [[0] * (capacity + 1) for _ in range(length + 1)]

    for i in range(length + 1):

        for w in range(capacity + 1):
            if i == 0 or w == 0:
                continue

            if weights[i - 1] > w:
                logging.debug("> %d, %d, %d" % (weights[i - 1], w, matrix[i - 1][w]))
                matrix[i][w] = matrix[i - 1][w]
            else:
                logging.debug("<= %d, %d, %d, %d" % (weights[i - 1], w, matrix[i - 1][w], matrix[i - 1][capacity - weights[i - 1]] + weights[i - 1]))
                matrix[i][w] = max(matrix[i - 1][w], matrix[i - 1][w - weights[i - 1]] + weights[i - 1])

            logging.debug("i, w, weights[i-1] is %d, %d, %d" % (i, w, weights[i - 1]))

    logging.debug("matrix is: %d" % matrix[length][capacity])
    """for m in matrix:
        print(m)"""
    return matrix[length][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))

