import unittest
import os
from tree_height import compute_height_fast


class TestSolution(unittest.TestCase):
    def test(self):
        files = get_files()
        c = 0
        for f in files:
            c += 1
            if not c:
                return
            with open(f, 'r') as fs:
                text = fs.read().strip()
            lst = text.split("\n")
            n = int(lst[0])
            parents = list(map(int, lst[1].split()))
            with open(f + ".a", "r") as fs:
                answer = int(fs.read().strip())
            value = compute_height_fast(n, parents)
            self.assertEqual(value, answer)


def get_files():

    files = []
    path = os.path.join(os.getcwd(), "tests")
    for file in os.listdir(path):
        if file.split(".")[-1] == "a":
            continue
        files.append(os.path.join(path, file))

    return files


if __name__ == "__main__":
    unittest.main()