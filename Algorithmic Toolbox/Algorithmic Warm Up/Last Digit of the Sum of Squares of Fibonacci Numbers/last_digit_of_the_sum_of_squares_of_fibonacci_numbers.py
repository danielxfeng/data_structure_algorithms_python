# python3


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum([f ** 2 for f in fibonacci_numbers]) % 10


def last_digit_of_the_sum_of_squares_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n
    res = []

    # get Fn mod m circle
    for i in range(n + 1):
        if i <= 1:
            res.append(i)
        else:
            mod = (res[-2] + res[-1]) % 10
            res.append(mod)
            if i == n:
                return res[-1] * (res[-1] + res[-2]) % 10

            if len(res) and len(res) % 2 == 1:
                continue
            half = int(len(res) / 2)
            start = res[:half]
            end = res[half:]
            if start != end:
                continue
            circle = start
            break

    pos = int(n % len(circle))

    current = circle[pos]
    if pos == 0:
        previous = circle[-1]
    previous = circle[pos - 1]
    res = (current * (current + previous)) % 10

    return (res)


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_squares_of_fibonacci_numbers(input_n))
