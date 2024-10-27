# python3

from itertools import combinations
import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

#logger.setLevel(logging.DEBUG)
logging.Logger.disabled = True

count = 0
c2 = 0


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def compute_inversions(elements):
    global count, c2
    logger.debug(elements)
    count = 0
    c2 = 0
    res = merge_sort(elements)
    # logger.debug(str(res))
    return count


def merge_sort(elements):
    length = len(elements)

    if length <= 1:
        return elements

    mid = length // 2

    return merge(merge_sort(elements[0: mid]), merge_sort(elements[mid: length]))


def merge(left, right):

    global count, c2
    """for i in left:
        for j in right:
            if i > j:
                c2 += 1"""
    logger.debug(str(left) + str(right) + str(count))

    res = []
    rc = 0
    rce = None
    while True:
        if len(left) == 0 and len(right) == 0:
            break

        if len(left) == 0:
            res += right
            break
        elif len(right) == 0:
            if (rce is not None) and (left[0] > rce):
                logger.debug("rc %d" % rc)
                count += len(left) * rc
                logger.debug("left %d %d %d" % (count, len(left), rc))
                res += left
                break

            rc = 1
            res.append(left[0])
            left.pop(0)
            logger.debug("left!")

            continue

        if left[0] == right[0]:
            if (rce is not None) and left[0] > rce:
                count += len(left) * rc
                logger.debug("= %d %d %d" % (count, len(left), rc))
                rc = 0
            rc += 1
            rce = left[0]
            logger.debug("jump= %d, %d" % (rc, rce))
            res += [left[0], right[0]]
            left.pop(0)
            right.pop(0)
        elif left[0] < right[0]:
            if (rce is not None) and left[0] > rce:
                count += len(left) * rc
                logger.debug("< %d %d %d" % (count, len(left), rc))
                rc, rce = 0, None
            res.append(left[0])
            left.pop(0)
        else:
            rce = None
            count += len(left) * (rc + 1)
            logger.debug("> %d %d %d" % (count, len(left), rc))
            rc = 0
            res.append(right[0])
            right.pop(0)

    '''if c2 != count:
        logger.debug("hi,hi,hi,%d, %d" % (count, c2))'''

    return res


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
    #print(merge([4,4,10], [2,2,4]))
