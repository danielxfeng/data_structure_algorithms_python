# python3
import sys


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7
    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(n - 1):
        a, b = b, (b + a) % 10
        #print(a, b)
    return b


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
