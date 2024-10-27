# python3

import sys
import threading

import os
import logging
import datetime

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)
# logger.setLevel(logging.INFO)
logging.Logger.disabled = True


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def compute_height_fast(n, parents):
    if n < 2:
        return n

    logging.debug("n is %d" % n)
    logging.debug("parents is %s" % parents)
    logging.debug("parents id %s" % list(range(n)))

    start_time = datetime.datetime.now()
    lst = [None] * (max(parents) + 1)

    keys = []
    for i, parent in enumerate(parents):
        if parent == -1:
            keys.append(i)
            continue
        if lst[parent] is None:
            lst[parent] = [i]
        else:
            lst[parent].append(i)

    """if len(keys) == 0:
        return 0"""
    end_time = datetime.datetime.now() - start_time
    logging.info("prepare time is %s" % end_time)
    logging.debug("lst is %d, %s" % (len(lst), lst))
    max_height, count = compute_height_lst(lst, keys, 1, 0)
    logging.info("count is %d" % count)

    return max_height


def compute_height_lst(lst, starts, max_height, count):
    while True:
        stime = datetime.datetime.now()
        count += 1
        keys = []
        go = False
        for start in starts:
            if start < len(lst) and lst[start]:
                go = True
                keys += lst[start]
                lst[start] = None
        if go is False:
            break
        max_height += 1
        starts = keys
        etime = datetime.datetime.now() - stime
        # logging.info("each time is %s" % etime)

    return max_height, count


def get_files():
    files = []
    path = os.path.join(os.getcwd(), "tests")
    for file in os.listdir(path):
        if file.split(".")[-1] == "a":
            continue
        files.append(os.path.join(path, file))

    return files


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height_fast(n, parents))


if __name__ == "__main__":
    main()
    # unittest.main()
# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
#sys.setrecursionlimit(10 ** 7)  # max depth of recursion
#threading.stack_size(2 ** 27)  # new thread will get stack of such size
#threading.Thread(target=main).start()
