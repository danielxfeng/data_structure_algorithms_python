# python3
import os
import unittest
from sys import stdin


# Splay tree implementation

# Vertex of a splay tree
class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)


def update(v):
    if v == None:
        return
    v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v


def smallRotation(v):
    parent = v.parent
    if parent == None:
        return
    grandparent = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v):
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)


# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
    v = root
    last = root
    next = None
    while v != None:
        if v.key >= key and (next == None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return next, root


def split(root, key):
    result, root = find(root, key)
    if result == None:
        return (root, None)
    right = splay(result)
    left = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return left, right


def merge(left, right):
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root = None


def insert(x):
    global root
    (left, right) = split(root, x)
    new_vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)

    # print_supp(root)


def erase(x):
    global root

    found = search(x)
    if not found:
        # print("not found")
        return

    left, right = split(root, x)
    right = merge(right.left, right.right)
    root = merge(left, right)
    if root is not None:
        root.parent = None

    # print_supp(root)


def search(x):
    global root
    next_root, root = find(root, x)
    # print_supp(next_root, 1)
    if next_root is None or next_root.key != x:
        return False
    return True


def my_sum(fr, to):
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    # print_supp(root)
    ans = 0
    if middle is not None:
        ans = middle.sum
    # Complete the implementation of sum
    root = merge(merge(left, middle), right)

    return ans


def print_supp(v, tp=0):
    if v is None:
        print("None")
        return

    if v.left is None:
        left = None
    else:
        left = v.left.key

    if v.right is None:
        right = None
    else:
        right = v.right.key

    if v.parent is None:
        parent = None
    else:
        parent = v.parent.key

    if tp == 1:
        print(v.key, v.sum, left, right, parent)

    if left:
        print_supp(v.left)

    if tp == 0:
        print(v.key, v.sum, left, right, parent)

    if right:
        print_supp(v.right)


def main():
    MODULO = 1000000001
    n = int(stdin.readline())
    last_sum_result = 0
    for i in range(n):
        line = stdin.readline().split()
        if line[0] == '+':
            x = int(line[1])
            insert((x + last_sum_result) % MODULO)
        elif line[0] == '-':
            x = int(line[1])
            erase((x + last_sum_result) % MODULO)
        elif line[0] == '?':
            x = int(line[1])
            print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
        elif line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            res = my_sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
            print(res)
            last_sum_result = res % MODULO


"""
class TestSolution(unittest.TestCase):
    def test(self):
        MODULO = 1000000001
        files = get_files()
        for f in files:
            print(f)
            with open(f, 'r') as fs:
                lists = fs.read().strip().split("\n")
            with open(f + ".a", "r") as fs:
                answers = fs.read().strip().split("\n")
            res = []
            n = int(lists[0])
            last_sum_result = 0
            global root
            root = None
            for i in range(1, n + 1):
                print(i, lists[i])
                line = lists[i].split()
                if line[0] == '+':
                    x = int(line[1])
                    insert((x + last_sum_result) % MODULO)
                elif line[0] == '-':
                    x = int(line[1])
                    erase((x + last_sum_result) % MODULO)
                elif line[0] == '?':
                    x = int(line[1])
                    if search((x + last_sum_result) % MODULO):
                        print("found", len(res) + 1)
                        res.append('Found')
                    else:
                        print("not found", len(res) + 1)
                        res.append('Not found')
                elif line[0] == 's':
                    l = int(line[1])
                    r = int(line[2])
                    r2 = my_sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
                    print(r2, len(res) + 1)
                    res.append(str(r2))
                    last_sum_result = r2 % MODULO
            self.assertEqual(res, answers)
"""


def get_files():

    files = []
    path = os.path.join(os.getcwd(), "tests")
    for file in os.listdir(path):
        if file.split(".")[-1] == "a":
            continue
        files.append(os.path.join(path, file))

    return files


if __name__ == '__main__':
    main()
    # TestSolution().test()
