# python3

from random import randint


def partition3(array, left, right):

    j = left
    k = left
    i = left + 1
    if left >= right:
        return
    while i <= right:
        j_plus = True
        if array[i] == array[left]:
            k += 1
            j += 1
            j_plus = False
            swap(array, i, k)
        if array[i] <= array[left]:
            if j_plus is True:
                j += 1
            if i > j:
                swap(array, i, j)
        i += 1

    for m in range(j - k):
        swap(array, left + m, j - m)

    return j - k + left, j


def randomized_quick_sort(array, left, right):

    if left >= right:
        return
    k = randint(left, right)
    swap(array, left, k)
    j, k = partition3(array, left, right)
    if j >= 1:
        randomized_quick_sort(array, left, j - 1)
    randomized_quick_sort(array, k + 1, right)

    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
