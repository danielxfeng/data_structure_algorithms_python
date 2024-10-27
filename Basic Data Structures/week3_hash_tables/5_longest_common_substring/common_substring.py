# python3

import sys
from collections import namedtuple
import random

Answer = namedtuple('answer_type', 'i j len')


class ComputeHash:
    def __init__(self, s):
        self.s = s
        self.m1 = 87178291199 # 10 ** 8 + 31
        self.m2 = 3314192745739 # 10 ** 9 + 3
        self.x = 1234
        self.length = len(s)
        self.h1 = [0] * (self.length + 1)
        self.h2 = self.h1[:]
        self.__set_h()

    def __set_h(self):
        for i in range(1, self.length + 1):
            self.h1[i] = (self.x * self.h1[i - 1] + ord(self.s[i - 1])) % self.m1
            self.h2[i] = (self.x * self.h2[i - 1] + ord(self.s[i - 1])) % self.m2

    def get_sub_hash(self, l, r):
        return self.__get_single_sub_hash(self.h1, self.m1, l, r), self.__get_single_sub_hash(self.h2, self.m2, l, r)

    def __get_single_sub_hash(self, hashes, p, l, r):
        last = hashes[r]
        y = pow(self.x, r - l, p)
        substring_hash = (last - y * hashes[l]) % p
        return substring_hash


def solve(s, t):
    # print(s, t)
    ans = Answer(0, 0, 0)
    ls = len(s)
    lt = len(t)
    ml = min(ls, lt)
    ans = solve_s(ComputeHash(s), ComputeHash(t), 1, ml, ans, ls, lt)
    return ans


def solve_s(cs, ct, l, r, ans, ls, lt):
    while True:
        if l > r:
            break

        mid = (l + r) // 2
        # print("mid", mid)

        found = False

        csl = {}

        for i in range(ls - mid + 1):
            csl[cs.get_sub_hash(i, i + mid)] = i

        # print(csl)

        for i in range(lt - mid + 1):
            ctv = ct.get_sub_hash(i, i + mid)
            if ctv in csl.keys() and mid > ans.len:

                ans = Answer(csl[ctv], i, mid)
                found = True
                # print("match", ans, "ctv", ctv)

        if found:
            l = mid + 1
        else:
            r = mid - 1
        # print("l", l, "r", r)

    return ans


def solve_naive(s1, s2):
    ans = Answer(0, 0, 0)
    for i in range(len(s1)):
        for j in range(len(s2)):
            for l in range(min(len(s1) - i, len(s2) - j) + 1):
                if (l > ans.len) and (s1[i:i + l] == s2[j:j + l]):
                    ans = Answer(i, j, l)
    return ans


def run_tests():
    tests = [
        ("cool", "toolbox", (1, 1, 3)),
        ("aaa", "bb", (0, 0, 0)),
        ("aabaa", "babbaab", (2, 3, 3)),
        ("zsaizkvr", "ugxnv", (6, 4, 1)),
    ]

    for s1, s2, output in tests:
        # answer = solve_naive(s1, s2)
        answer = solve(s1, s2)
        answer = (answer.i, answer.j, answer.len)
        assert answer == output, f"""
		Input: s1={s1} | s2={s2}
		Expected: {output}
		Got:      {answer}
		"""
        print("Test passed!\n")


def run_stress_test():
    # alphabet = "abcdefghigklmnopqrstuvwxyz"
    alphabet = "abcde"
    while True:
        s1 = "".join([random.choice(alphabet) for _ in range(random.randint(0, 5))])
        s2 = "".join([random.choice(alphabet) for _ in range(random.randint(0, 5))])
        answer = solve(s1, s2)
        assert answer.len == solve_naive(s1, s2).len
        assert s1[answer.i:answer.i + answer.len] == s2[answer.j:answer.j + answer.len], f"""
				Input: s1={s1} | s2={s2}
				Got:      {answer}
				"""
        print(f"Input: s1={s1} | s2={s2}\nEqual: {s1[answer.i:answer.i + answer.len]}")
        print("Test passed!\n")


def main():
    for line in sys.stdin.readlines():
        s, t = line.split()
        ans = solve(s, t)
        print(ans.i, ans.j, ans.len)


if __name__ == '__main__':
    # run_tests()
    # run_stress_test()
    main()
