# python3

position = None


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    #assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    #assert 1 <= len(keys) <= 3 * 10 ** 4
    global position
    position = None
    search(keys, 0, len(keys) - 1, query)
    #print("position", keys, query, position)

    if position is None:
        return -1
    else:
        return position


def search(keys, left, right, query):
    #print(left, right, query)
    if left > right:
        return

    if query < keys[left] or query > keys[right]:
        return

    half = left + (right - left) // 2
    #print(keys, query, left, right, half)

    if query == keys[half]:
        #print("hit", half)
        update_position(half)
        search(keys, left, half - 1, query)
        return
    elif query < keys[half]:
        search(keys, left, half - 1, query)
        return
    elif query > keys[half]:
        search(keys, half + 1, right, query)
        return
    return


def update_position(index):
    global position
    #print("update", position)
    if (position is None) or (index < position):
        position = index
    return


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries
    """
    input_keys= [2,4,4,4,7,7,9]
    input_queries = [9, 4, 5, 2]"""
    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')