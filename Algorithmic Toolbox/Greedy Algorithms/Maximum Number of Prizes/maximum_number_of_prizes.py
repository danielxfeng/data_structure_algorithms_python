# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    
    # print(999999999)
    
    summands = []

    if n == 1:
        summands.append(1)

    for i in range(1, n):
        summands.append(i)
        sum_lst = int((summands[0] + summands[-1]) * len(summands) / 2)
        if (sum_lst + i + 1) > n:
            summands[-1] = n - sum_lst + summands[-1]
            break

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
