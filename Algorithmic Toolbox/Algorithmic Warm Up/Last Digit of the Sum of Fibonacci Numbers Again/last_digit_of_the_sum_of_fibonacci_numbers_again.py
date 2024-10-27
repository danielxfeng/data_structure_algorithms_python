# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    #test 999999999999999999
    #get Fn mod m circle
    res = []
    for i in range(to_index + 1):
        if i <= 1:
            res.append(i)
        else:
            mod = (res[-2] + res[-1]) % 10
            res.append(mod)

        half = int(len(res)/2)
        start = res[:half]
        end = res[half:]
        if start != end:
            if i == to_index:
                circle = res
        else:
            circle = start
            break

    to_pos, to_mul = get_pos(to_index, circle)
    from_pos, from_mul = get_pos(from_index, circle)

    res = ((to_mul - from_mul) * sum(circle) + sum(circle[:to_pos + 1]) - sum(circle[:from_pos])) % 10

    return (res)


def get_pos(index, lst):
    pos = int(index % len(lst))
    mul = int(index / len(lst))
    return pos, mul


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
