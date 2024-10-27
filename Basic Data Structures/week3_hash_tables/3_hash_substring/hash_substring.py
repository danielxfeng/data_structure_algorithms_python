# python3

def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    p = 1000000007
    x = 263
    res = []
    lt = len(text)
    lp = len(pattern)
    p_hash = poly_hash(pattern, p, x)
    t_hashes = pre_hash(p, x, text, lt, lp)

    for i in range(lt - lp + 1):
        if p_hash != t_hashes[i]:
            continue
        if pattern == text[i: (i + lp)]:
            res.append(i)
    return res


def poly_hash(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans


def pre_hash(p, x, text, lt, lp):
    res = [None] * (lt - lp + 1)
    s = text[(lt - lp): lt]
    res[lt - lp] = poly_hash(s, p, x)
    y = 1
    for i in range(lp):
        y = (y * x) % p
    for i in range(lt - lp - 1, -1, -1):
        res[i] = (x * res[i + 1] + ord(text[i]) - y * ord(text[i + lp])) % p
    return res


def p_test():
    values = [
        ("aba", "abacaba"),
        ("Test", "testTesttesT"),
        ("aaaaa", "baaaaaaa")
    ]
    for v in values:
        print_occurrences(get_occurrences(v[0], v[1]))


if __name__ == '__main__':
    # p_test()
    print_occurrences(get_occurrences(*read_input()))
