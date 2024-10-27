# python3

import sys


class Rope:
    def __init__(self, s):
        self.s = s
        self.root = None
        self.generate_tree_insert()

    def result(self):
        res = []
        self.get_res(self.root, res)
        return "".join(res)

    def print_supp(self, tree):
        res = []
        self.get_res(tree, res)
        print("".join(res))

    def get_res(self, tree, res):
        if tree is None:
            return

        if tree.left is None:
            left = None
        else:
            left = tree.left
        if tree.right is None:
            right = None
        else:
            right = tree.right

        if left:
            self.get_res(left, res)

        res.append(tree.m_str)

        if right:
            self.get_res(right, res)

        return

    def process_naive(self, i, j, k):
        part1 = self.s[: i]
        part2 = self.s[i: j + 1]
        part3 = self.s[j + 1:]
        self.s = part1 + part3
        part1 = self.s[:k]
        part3 = self.s[k:]
        self.s = part1 + part2 + part3

    def process(self, i, j, k):
        if j < i or k < 0:
            return
        left, start = split(self.root, i)
        print("left", "start", "i", i)
        self.print_supp(left)
        self.print_supp(start)
        cut, right = split(start, j + 1)
        print("cut", "right", "j", j + 1)
        self.print_supp(cut)
        self.print_supp(right)
        new = merge(left, right)
        print("new")
        self.print_supp(new)
        if new is None:
            return
        left, right = split(new, k)
        print("left", "right", "k", k)
        self.print_supp(left)
        self.print_supp(right)
        self.root = merge(merge(left, cut), right)
        return

    def generate_tree_insert(self):
        for i, x in enumerate(self.s):
            self.root = insert(self.root, i, x)
        print("init", self.result())
        return

    def generate_tree(self):
        self.root = self.generate_tree_single(0, len(self.s) - 1, None)
        return

    def generate_tree_single(self, l, r, p):
        if l > r:
            return
        mid = (r - l) // 2 + l
        if mid == 0:
            left = None
        else:
            left = self.generate_tree_single(l, mid - 1, mid)
        if mid == len(self.s) - 1:
            right = None
        else:
            right = self.generate_tree_single(mid + 1, r, mid)

        new = Vertex(mid, self.s[mid], left, right, p)
        return new


class Vertex:
    def __init__(self, key, m_str, left, right, parent):
        (self.key, self.m_str, self.left, self.right, self.parent) = (key, m_str, left, right, parent)


def update(v):
    if v == None:
        return
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
def insert(root, i, x):
    if root is None:
        left, right = None, None
    else:
        left, right = split(root, i)
    new_vertex = None
    if right == None or right.key != i:
        new_vertex = Vertex(i, x, None, None, None)
    return merge(merge(left, new_vertex), right)


def main():
    rope = Rope(sys.stdin.readline().strip())
    q = int(sys.stdin.readline())
    for _ in range(q):
        i, j, k = map(int, sys.stdin.readline().strip().split())
        rope.process(i, j, k)
    print(rope.result())


def run_tests():
    test_data = (
        (
            ("hlelowrold"),
            (
                (1, 1, 2),
                (6, 6, 7),
            )

        ),
        (
            ("abcdef"),
            (
                (0, 1, 1),
                (4, 5, 0)
            )
        )
    )
    for t in test_data:
        # print("s", t[0], t[1])
        d = Rope(t[0])
        # d.print_supp(d.root)
        for n in t[1]:
            d.process(int(n[0]), int(n[1]), int(n[2]))
        print(d.result())


if __name__ == '__main__':
    # main()
    run_tests()
