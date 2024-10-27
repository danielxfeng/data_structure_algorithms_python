#Uses python3
import os
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


def build_trie(patterns):
    # print(patterns)
    tree = dict()
    key = 0
    for pattern in patterns:
        parent = 0
        for i in range(len(pattern)):
            if parent not in tree.keys():
                key += 1
                tree[parent] = {pattern[i]: key}
                # print(1, pattern, pattern[i], parent, key)
                parent += 1
            elif pattern[i] not in tree[parent].keys():
                key += 1
                tree[parent][pattern[i]] = key
                # print(2, pattern, pattern[i], parent, key)
                parent = key
            elif pattern[i] in tree[parent].keys():
                parent = tree[parent][pattern[i]]
                # print(3, pattern, pattern[i], parent, key)
    # print(tree)
    return tree


def run_tests():
    files = get_files()
    files.sort(key=lambda x: x[-1])
    for f in files:
        with open(f, 'r') as fs:
            text = fs.read().strip()
        patterns = text.split("\n")[1:]
        tree = build_trie(patterns)
        for node in tree:
            for c in tree[node]:
                print("{}->{}:{}".format(node, tree[node][c], c))


def get_files():
    files = []
    path = os.path.join(os.getcwd(), "sample_tests")
    for file in os.listdir(path):
        if file.split(".")[-1] == "a":
            continue
        files.append(os.path.join(path, file))

    return files


def main():
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))


if __name__ == '__main__':
    main()
    # run_tests()
    