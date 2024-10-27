# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    #assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    #assert 1 <= len(keys) <= 3 * 10 ** 4

    res = search(keys, 0, len(keys) - 1, query)
    if res is not None:
        return res
    else:
        return -1


def search(keys, left, right, query):
    if left > right:
        return

    if query < keys[left]:
        return

    if query > keys[right]:
        return

    if query == keys[left]:
        return left

    if query == keys[right]:
        return right

    half = left + int((right - left + 1) / 2)

    if query == keys[half]:
        return half

    if right - left < 3:
        return

    if query < keys[half]:
        return search(keys, left, half, query)

    if query > keys[half]:
        return search(keys, half + 1, right, query)


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
