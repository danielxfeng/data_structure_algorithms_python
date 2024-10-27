import unittest
import os
from process_packages import process_requests
from process_packages import Buffer

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])


class TestSolution(unittest.TestCase):
    def test(self):
        files = get_files()
        c = 0
        for f in files:
            c += 1
            if not c:
                return

            if "22" not in f:
                continue
            with open(f, 'r') as fs:
                text = fs.read().strip()
            lst = text.split("\n")
            buffer_size, n_requests = list(map(int, lst[0].split()))
            buffer = Buffer(buffer_size)
            requests = []
            for i in range(n_requests):
                arrived_at, time_to_process = map(int, lst[i + 1].split())
                requests.append(Request(arrived_at, time_to_process))
            with open(f + ".a", "r") as fs:
                answer = fs.read().strip()
            responses = process_requests(requests, buffer)
            res = ""
            for response in responses:
                if not response.was_dropped:
                    res += str(response.started_at) + "\n"
                else:
                    res += "-1\n"
            print("file is", f)
            self.assertEqual(res[:-1], answer)


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