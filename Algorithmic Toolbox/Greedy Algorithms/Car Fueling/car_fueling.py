# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    count = 0
    rg = m

    for i in range(len(stops)):

        # print("We are at stop: ", i)
        if d <= stops[i]:
            arrived = True
            stop = d
        else:
            arrived = False
            stop = stops[i]

        # cal the range
        if i == 0:
            start = 0
        else:
            start = stops[i - 1]
        rg = rg - (stop - start)

        # the range can not reach the station
        if rg < 0:
            # print("Can not reach the stop")
            return -1

        if arrived:
            break

        if i + 1 == len(stops) or d < stops[i + 1]:
            next_stop = d - stops[i]
        else:
            next_stop = stops[i + 1] - stops[i]

        if next_stop > m:
            return -1

        # print("rg", rg)
        if rg < next_stop:
            # print("Fuel at station: ", i)
            count += 1
            rg = m

    return count


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
