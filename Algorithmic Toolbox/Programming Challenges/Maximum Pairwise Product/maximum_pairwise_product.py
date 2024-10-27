# python3
def max_pairwise_product_naive(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    """ solution 1 2.99s
    numbers.sort()
    res = numbers[-1] * numbers[-2]
    """

    """ solution 2 2.83s
    biggest = -1
    for i in range(len(numbers)):
        if biggest == -1 or numbers[biggest] <= numbers[i]:
            biggest = i
    second = -1
    for i in range(len(numbers)):
        if i != biggest and (second == -1 or numbers[second] <= numbers[i]):
            second = i
    # print(biggest, second)
    res = numbers[biggest] * numbers[second]   
    """

    #"""solution 3 2.94s fastest
    def find_the_biggest(lst):
        biggest = -1
        for i in range(len(lst)):
            if biggest == -1 or numbers[biggest] <= lst[i]:
                biggest = i

        return biggest

    first_index = find_the_biggest(numbers)
    first = numbers[first_index]
    del numbers[first_index]
    second = numbers[find_the_biggest(numbers)]
    #print(first, second)
    res = first * second
    #"""

    return res


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
