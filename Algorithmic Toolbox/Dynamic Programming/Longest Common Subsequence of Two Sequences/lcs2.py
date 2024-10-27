# python3

import logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

# logger.setLevel(logging.DEBUG)
logging.Logger.disabled = True


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    logging.debug("income is: %s, %s" % (str(first_sequence), str(second_sequence)))

    len1 = len(first_sequence)
    len2 = len(second_sequence)

    matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for f in range(len1 + 1):
        for s in range(len2 + 1):

            if f == 0 or s == 0:
                continue

            if first_sequence[f - 1] == second_sequence[s - 1]:
                matrix[f][s] = matrix[f - 1][s - 1] + 1
            else:
                matrix[f][s] = max(matrix[f][s - 1], matrix[f - 1][s])

    logging.debug("lcs is %d, %s" % (matrix[f][s], str(matrix)))
    return matrix[f][s]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
