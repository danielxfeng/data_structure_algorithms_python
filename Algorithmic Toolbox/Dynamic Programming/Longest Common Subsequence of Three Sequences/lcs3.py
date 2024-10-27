# python3

import logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

# logger.setLevel(logging.DEBUG)
logging.Logger.disabled = True


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    len1 = len(first_sequence)
    len2 = len(second_sequence)
    len3 = len(third_sequence)

    matrix = [[([0] * (len3 + 1)) for _ in range(len2 + 1)] for __ in range(len1 + 1)]

    for f in range(len1 + 1):
        for s in range(len2 + 1):
            for t in range(len3 + 1):

                if f == 0 or s == 0 or t == 0:
                    continue
                if first_sequence[f - 1] == second_sequence[s - 1] == third_sequence [t - 1]:
                    matrix[f][s][t] = matrix[f - 1][s - 1][t - 1] + 1
                else:
                    matrix[f][s][t] = max(
                        matrix[f][s][t-1],
                        matrix[f][s-1][t],
                        matrix[f][s-1][t-1],
                        matrix[f][s][t-1],
                        matrix[f-1][s][t],
                        matrix[f-1][s][t-1],
                        matrix[f-1][s-1][t],
                        matrix[f-1][s][t],
                        matrix[f][s-1][t],
                    )

    return matrix[len1][len2][len3]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
