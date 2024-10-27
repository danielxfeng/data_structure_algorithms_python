# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.

    length = len(data)
    if length <= 1:
        return []

    swap = []
    i = length // 2
    while i >= 0:
        swap = swap_down(data, length, i, swap)
        i -= 1
    return swap


def swap_down(data, length, i, swap):
    index = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < length and data[l] < data[index]:
        index = l
        # print("l")
    if r < length and data[r] < data[index]:
        index = r
        # print("r")
    if i != index:
        swap.append((i, index))
        data[i], data[index] = data[index], data[i]
        # print(i, index, data)
        swap = swap_down(data, length, index, swap)
    return swap


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    # data = [1]
    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
