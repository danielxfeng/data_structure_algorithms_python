# python3

import sys


class Solver:
    def __init__(self, s):
        self.s = s
        self.m1 = 10 ** 9 + 7
        self.m2 = 10 ** 9 + 9
        self.x = 263
        self.h1 = [0] * (len(self.s) + 1)
        self.h2 = [0] * (len(self.s) + 1)
        self.__set_h()

    def __set_h(self):
        for i in range(1, len(self.h1)):
            # print(self.h1, i, self.s[i - 1])
            self.h1[i] = (self.x * self.h1[i - 1] + ord(self.s[i - 1])) % self.m1
            self.h2[i] = (self.x * self.h2[i - 1] + ord(self.s[i - 1])) % self.m2

    def get_sub_hash(self, l, length):
        return self.__get_single_sub_hash(self.h1, self.m1, l, length), \
            self.__get_single_sub_hash(self.h2, self.m2, l, length)

    def __get_single_sub_hash(self, hashes, p, start, length):
        last = hashes[start + length]
        y = pow(self.x, length, p)
        substring_hash = (last - y * hashes[start]) % p
        return substring_hash

    def ask(self, a, b, l):
        if l == 0:
            return True

        h1a, h2a = self.get_sub_hash(a, l)
        h1b, h2b = self.get_sub_hash(b, l)

        found = False
        if h1a == h1b and h2a == h2b:
            found = True

        return found


def main():
    s = sys.stdin.readline()
    q = int(sys.stdin.readline())
    solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(a, b, l) else "No")


def p_test():
    s = "bbbabbabaa"
    q = [
        (7, 0, 1),
        (1, 7, 1),
        (2, 7, 1),
        (6, 1, 3),
        (2, 5, 5),
        (4, 6, 4),
        (9, 4, 1),
        (8, 3, 2),
        (5, 4, 4),
        (5, 1, 4),
        (0, 0, 3),
        (3, 4, 6),
        (5, 3, 2),
    ]
    solver = Solver(s)
    for i in range(len(q)):
        a, b, l = q[i]
        print("Yes" if solver.ask(a, b, l) else "No")


if __name__ == '__main__':
    # test()
    main()
