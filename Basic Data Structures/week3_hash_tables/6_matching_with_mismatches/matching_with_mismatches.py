# python3

import sys
from functools import lru_cache


class ComputeHash:
    def __init__(self, s):
        self.s = s
        self.m1 = 87178291199  # 10 ** 8 + 31
        # self.m2 = 3314192745739  # 10 ** 9 + 3
        self.x = 1234
        self.length = len(s)
        self.h1 = [0] * (self.length + 1)
        self.h2 = self.h1[:]
        self.__set_h()

    def __set_h(self):
        for i in range(1, self.length + 1):
            self.h1[i] = (self.x * self.h1[i - 1] + ord(self.s[i - 1])) % self.m1
            # self.h2[i] = (self.x * self.h2[i - 1] + ord(self.s[i - 1])) % self.m2

    @lru_cache(maxsize=1024 * 4)
    def get_sub_hash(self, l, r):
        return self.__get_single_sub_hash(self.h1, self.m1, l, r) # , self.__get_single_sub_hash(self.h2, self.m2, l, r)

    def __get_single_sub_hash(self, hashes, p, l, r):
        # print("len", len(hashes), l, r)
        last = hashes[r]
        y = pow(self.x, r - l, p)
        substring_hash = (last - y * hashes[l]) % p
        return substring_hash


def solve(k, text, pattern):

    lp = len(pattern)
    lt = len(text)
    if lt < lp:
        return []

    res = []
    cp = ComputeHash(pattern)
    ct = ComputeHash(text)
    for i in range(lt - lp + 1):
        k_i = 0
        a = i
        base_b = i + lp - 1
        b = base_b
        while k_i <= k:
            mismatch = -1
            while a <= b:
                # print("l", "r", a, b)
                mid = (a + b) // 2

                t_s_hash = ct.get_sub_hash(a, mid + 1)
                p_s_hash = cp.get_sub_hash(a - i, mid - i + 1)
                """print("text", text, "p", pattern)
                print("ts", text[a:mid+1], "ps", text[a-i:mid-i+1])
                print(t_s_hash, p_s_hash)"""

                if t_s_hash == p_s_hash:
                    # print("match")
                    a = mid + 1
                else:
                    # print("mismatch", mid)
                    mismatch = mid
                    b = mid - 1

            if mismatch != -1:
                k_i += 1
                a = mismatch + 1
                b = base_b
            else:
                # print("add", i)
                res.append(i)
                break

    return res


def main():
    for line in sys.stdin.readlines():
        k, t, p = line.split()
        ans = solve(int(k), t, p)
        print(len(ans), *ans)


def run_tests():
	tests = (
		(0, "ababab", "baaa", []),
		(1, "ababab", "baaa", [1]),
		(1, "xabcabc", "ccc", []),
		(2, "xabcabc", "ccc", [1, 2, 3, 4]),
		(3, "aaa", "xxx", [0]),
		(0, "aaabbaa", "aa", [0, 1, 5]),
	)

	for i, (k, s1, s2, output) in enumerate(tests):
		res = solve(k, s1, s2)
		print(f"Result: {res}")
		assert res == output, f"""
		Input: s1={s1} | s2={s2} | k={k}
		Expected: {output}
		Got:      {res}
		"""
		print(f"#{i+1} test passed!")


if __name__ == '__main__':
    main()
    # run_tests()
