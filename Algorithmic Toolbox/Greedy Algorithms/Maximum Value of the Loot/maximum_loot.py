# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    ups = [prices[i]/weights[i] for i in range(len(prices))]
    ups_index = get_index(ups)
    value = 0
    for i in ups_index:
        if capacity < weights[i]:
            value += capacity * ups[i]
            break
        else:
            capacity -= weights[i]
            value += prices[i]

    return value


def get_index(numbers):
    num_index = []
    for i in range(len(numbers)):
        big = -1
        for i1 in range(len(numbers)):
            if i1 != big and (i1 not in num_index) and (big == -1 or numbers[big] <= numbers[i1]):
                #print(i1)
                big = i1
        num_index.append(big)
    return(num_index)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
