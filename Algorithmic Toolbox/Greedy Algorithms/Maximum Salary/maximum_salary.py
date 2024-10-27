# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    #print("income", numbers)

    numbers = sorted([str(n) for n in numbers], reverse=True)

    #print("numbers", numbers)
    for i in range(1, len(numbers)):
        circle = sorted(list(range(1, i + 1)), reverse=True)
        #print("circle", circle)
        for i1 in circle:
            if (numbers[i1 - 1] + numbers[i1]) < (numbers[i1] + numbers[i1 - 1]):
                numbers[i1], numbers[i1 - 1] = numbers[i1 - 1], numbers[i1]
                i1 -= 1

    numbers = "".join(numbers)

    return(int(numbers))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
