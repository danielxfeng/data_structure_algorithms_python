# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:

    def read_test(self, n, data):
        self.n = n
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, data[i])
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        result = []
        self.go_in_order(0, result)
        return result

    def preOrder(self):
        result = []
        self.go_pre_order(0, result)
        return result

    def postOrder(self):
        result = []
        self.go_post_order(0, result)

        return result

    def go_in_order(self, i, result):
        if i == -1:
            return
        if self.left[i] == -1 and self.right[i] == -1:
            result.append(self.key[i])
            return
        self.go_in_order(self.left[i], result)
        result.append(self.key[i])
        self.go_in_order(self.right[i], result)

    def go_pre_order(self, i, result):
        if i == -1:
            return
        if self.left[i] == -1 and self.right[i] == -1:
            result.append(self.key[i])
            return
        result.append(self.key[i])
        self.go_pre_order(self.left[i], result)
        self.go_pre_order(self.right[i], result)

    def go_post_order(self, i, result):
        if i == -1:
            return
        if self.left[i] == -1 and self.right[i] == -1:
            result.append(self.key[i])
            return
        self.go_post_order(self.left[i], result)
        self.go_post_order(self.right[i], result)
        result.append(self.key[i])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


def run_tests():
    tree = TreeOrders()
    test_data = (
        (
            (4,1,2),
            (2,3,4),
            (5,-1,-1),
            (1,-1,-1),
            (3,-1,-1)
        ),
        (
            (0,7,2),
            (10,-1,-1),
            (20,-1,6),
            (30,8,9),
            (40,3,-1),
            (50,-1,-1),
            (60,1,-1),
            (70,5,4),
            (80,-1,-1),
            (90,-1,-1)
        ),
        (
            (4, 1, 2),
            (2, 3, 4),
            (6, 5, 6),
            (1, -1, -1),
            (3, -1, -1),
            (5, -1, -1),
            (7, -1, -1),
        ),
    )
    for t in test_data:
        tree.read_test(len(t), t)
        print(tree.key)
        print(tree.left)
        print(tree.right)
        print(" ".join(str(x) for x in tree.inOrder()))
        print(" ".join(str(x) for x in tree.preOrder()))
        print(" ".join(str(x) for x in tree.postOrder()))


if __name__ == '__main__':
    # threading.Thread(target=main).start()
    run_tests()