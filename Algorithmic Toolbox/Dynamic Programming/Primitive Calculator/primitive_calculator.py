# python3

import logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

# logger.setLevel(logging.DEBUG)
logging.Logger.disabled = True


def compute_operations(n):
    assert 1 <= n <= 10 ** 6

    memo = [[], [1]]

    for number in range(2, n + 1):

        cal = Cals(memo, number)
        min_len = n + 1
        min_value = None

        for i in range(cal.length):

            if cal.run(i):
                value = cal.run(i, 1).copy()
                length = len(value) + 1
                logging.debug("cal, value is %s, number is: %d, cal id is: %d, min_len is %d, length is %d" % (str(value), number, i, min_len, length))
                if min_len > length:
                    value.append(number)
                    min_len = length
                    min_value = value.copy()
        memo.append(min_value)

    return memo[n]


class Cals:
    def __init__(self, lst, d):
        self.memo = lst
        self.number = d
        self.length = 3

    def __plus_one_con(self):
        return (self.number - 1) >= 0

    def __plus_one(self):
        return self.memo[self.number - 1]

    def __multiply_two_con(self):
        return self.number % 2 == 0

    def __multiply_two(self):
        return self.memo[self.__get_multiply(2)]

    def __multiply_three_con(self):
        return self.number % 3 == 0

    def __multiply_three(self):
        return self.memo[self.__get_multiply(3)]

    def __get_multiply(self, item):
        return self.number // item

    def run(self, i, c=0):
        if i == 0:
            if c == 0:
                return self.__plus_one_con()
            if c == 1:
                return self.__plus_one()
        if i == 1:
            if c == 0:
                return self.__multiply_two_con()
            if c == 1:
                return self.__multiply_two()
        if i == 2:
            if c == 0:
                return self.__multiply_three_con()
            if c == 1:
                return self.__multiply_three()


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
