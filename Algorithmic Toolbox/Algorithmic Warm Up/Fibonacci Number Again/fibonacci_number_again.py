# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    res = []
    #get Fn mod m circle
    for i in range(n + 1):
        if i <= 1:
            res.append(i)
        else:
            mod = (res[-2] + res[-1]) % m

            #if has not found the circle
            if i == n:
                return mod

            res.append(mod)
            if len(res) and len(res) % 2 == 1: continue
            half = int(len(res)/2)
            start = res[:half]
            end = res[half:]
            if start != end: continue
            circle = start
            #print(circle)
            break

    pos = int(n % len(circle))
    #print(pos)
    res = circle[pos]
    return(res)


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
