#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def IsBinarySearchTree(tree):

    if len(tree) == 0:
        return True

    res = go_in_order(tree, 0, tree[0][0], 2)
    return res


def go_in_order(tree, i, last, direction):

    if i == -1:
        return True
    if tree[i][1] == -1 and tree[i][2] == -1:
        return True

    # print("v", tree[i][0], "l", tree[tree[i][1]][0], "r", tree[tree[i][2]][0], "last", last)

    if tree[i][1] != -1 and (tree[tree[i][1]][0] >= tree[i][0] or (direction == 1 and tree[tree[i][1]][0] <= last)):
        # print("left")
        return False

    if tree[i][2] != -1 and (tree[tree[i][2]][0] <= tree[i][0] or (direction == 0 and tree[tree[i][2]][0] >= last)):
        # print("right")
        return False

    if go_in_order(tree, tree[i][1], tree[i][0], 0) is False:
        return False

    if go_in_order(tree, tree[i][2], tree[i][0], 1) is False:
        return False
    return True


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
        [],
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


if __name__ == '__main__':
    threading.Thread(target=main).start()
    # run_tests()

