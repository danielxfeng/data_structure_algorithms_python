# python3


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29
    values, operators = split(dataset)
    M = [[None] * len(values) for _ in range(len(values))]
    m = [[None] * len(values) for _ in range(len(values))]

    for i in range(len(values)):
        m[i][i] = values[i]
        M[i][i] = values[i]

    for s in range(1, len(values)):
        for i in range(len(values) - s):
            j = i + s
            M[i][j], m[i][j] = min_and_max(i, j, operators, M, m)

    """for i in M:
        print(i)

    for i in m:
        print(i)"""

    return M[0][len(values) - 1]


def min_and_max(i, j, operators, M, m):

    min_res = float("inf")
    max_res = float("-inf")

    for k in range(i, j):
        a = calc(M[i][k], M[k+1][j], operators[k])
        b = calc(M[i][k], m[k+1][j], operators[k])
        c = calc(m[i][k], M[k+1][j], operators[k])
        d = calc(m[i][k], m[k+1][j], operators[k])

        min_res = min(min_res, a, b, c, d)
        max_res = max(max_res, a, b, c, d)

    return max_res, min_res


def split(dataset):

    values = []
    symbols = []

    for i in range(len(dataset)):
        if i % 2 == 0:
            values.append(int(dataset[i]))
        else:
            symbols.append(dataset[i])

    return values, symbols


def calc(first, second, op):

    if op == "+":
        return first + second
    elif op == "-":
        return first - second
    elif op == "*":
        return first * second
    elif op == "/":
        return first / second


if __name__ == "__main__":
    print(find_maximum_value(input()))

