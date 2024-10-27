# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5

    length = len(elements)
    half = length / 2
    dic = {}
    res = merge_sort(0, length, half, dic, elements)
    return res


def merge_sort(start, end, half, dic, elements):
    #print("cal", start, end)
    if end - start <= 1:
        element = elements[start]
        if element not in dic.keys():
            dic[element] = 1
        else:
            dic[element] += 1
        if dic[element] > half:
            #print("return true", dic[element], half)
            return 1
        return 0
    mid = start + int((end - start) / 2)
    res = merge_sort(start, mid, half, dic, elements)
    if res == 1:
        return 1
    res = merge_sort(mid, end, half, dic, elements)
    return res




if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
