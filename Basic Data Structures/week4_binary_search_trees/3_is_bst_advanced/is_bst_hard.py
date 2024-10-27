#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10 ** 9)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):
    if len(tree) < 1:
        return True
    res = []
    go_in_order(tree, 0, res)

    for i in range(len(res) - 1):
        if res[i][0] > res[i + 1][0] or (res[i][0] == res[i + 1][0] and res[i][0] == tree[res[i][1]]):
            return False

    return True


def go_in_order(tree, i, res):

    if i == -1:
        return

    go_in_order(tree, tree[i][1], res)

    res.append((tree[i][0], tree[i][2]))

    go_in_order(tree, tree[i][2], res)

    return


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    # print(tree)
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


def run_tests():
    test_data = [
        [
            [2, 1, 2],
            [1, -1, -1],
            [3, -1, -1]
        ],
        [
            [1, 1, 2],
            [2, -1, -1],
            [3, -1, -1]
        ],
        [
            [2, 1, 2],
            [1, -1, -1],
            [2, -1, -1]
        ],
        [
            [2, 1, 2],
            [2, -1, -1],
            [3, -1, -1]
        ],
        [],
        [[2147483647, -1, -1]],
        [
            [1, -1, 1],
            [2, -1, 2],
            [3, -1, 3],
            [4, -1, 4],
            [5, -1, -1]
        ],
        [
            [4, 1, 2],
            [2, 3, 4],
            [6, 5, 6],
            [1, -1, -1],
            [3, -1, -1],
            [5, -1, -1],
            [7, -1, -1]
        ],
        [
            [4, 1, -1],
            [2, 2, 3],
            [1, -1, -1],
            [5, -1, -1]
        ],
    ]
    for t in test_data:
        tree = t
        if IsBinarySearchTree(tree):
            print("CORRECT")
        else:
            print("INCORRECT")

    # C I C I C C C C


if __name__ == '__main__':
    threading.Thread(target=main).start()
    # run_tests()
