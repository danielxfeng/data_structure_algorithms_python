# python3

import logging

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
# logger.setLevel(# logging.debug)


# logger.setLevel(logging.INFO)
logging.Logger.disabled = True


class MyQueue:
    def __init__(self, max_length):
        self.__in_stack = []
        self.__out_stack = []
        self.__max_stack = []
        self.__max_in_stack = 0
        self.__max_length = max_length

    def push(self, a):
        self.__in_stack.append(a)
        if a > self.__max_in_stack:
            self.__max_in_stack = a
        if len(self.__in_stack) + len(self.__out_stack) > self.__max_length:
            self.pop()
        # logging.debug("in_stack %s" % self.__in_stack)
        # logging.debug("out_stack %s" % self.__out_stack)
        # logging.debug("max_stack %s" % self.__max_stack)
        return

    def pop(self):
        if len(self.__out_stack) == 0:
            while len(self.__in_stack) > 0:
                v = self.__in_stack.pop()
                if len(self.__max_stack) == 0 or v >= self.__max_stack[-1]:
                    self.__max_stack.append(v)
                self.__out_stack.append(v)
            self.__max_in_stack = 0

        v = self.__out_stack.pop()
        if v == self.__max_stack[-1]:
            self.__max_stack.pop()
        # logging.debug("in_stack %s" % self.__in_stack)
        # logging.debug("out_stack %s" % self.__out_stack)
        # logging.debug("max_stack %s" % self.__max_stack)
        return v

    def max(self):
        if len(self.__max_stack) == 0 or self.__max_stack[-1] <= self.__max_in_stack:
            # logging.debug("max is %d" % self.__max_in_stack)
            return self.__max_in_stack
        # logging.debug("max is %d" % self.__max_stack[-1])
        return self.__max_stack[-1]


def max_sliding_window_naive(sequence, m):
    maximums = []
    my_queue = MyQueue(m)

    for i, s in enumerate(sequence):
        # logging.debug("i is %d" % i)
        my_queue.push(s)
        if i > m - 2:
            maximums.append(my_queue.max())

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))
    # print(max_sliding_window_naive([0]*100000, 33333))
    # print(max_sliding_window_naive([2, 7, 3, 1, 5, 2, 6, 2], 4))
