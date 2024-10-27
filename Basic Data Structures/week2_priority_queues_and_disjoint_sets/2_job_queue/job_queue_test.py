import unittest
import os
from job_queue import assign_jobs

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


class TestSolution(unittest.TestCase):
    def test(self):
        files = get_files()
        c = 0
        for f in files:
            c += 1
            if not c:
                return

            if "08" not in f:
                continue
            with open(f, 'r') as fs:
                text = fs.read().strip()
            lst = text.split("\n")
            n_workers, n_jobs = map(int, lst[0].split())
            jobs = list(map(int, lst[1].split()))
            assert len(jobs) == n_jobs
            assigned_jobs = assign_jobs(n_workers, jobs)

            with open(f + ".a", "r") as fs:
                answers = fs.read().strip()
            answers = answers.split("\n")
            final_answers = []
            for a in answers:
                x = a.split()
                final_answers.append(AssignedJob(int(x[0]), int(x[1])))

            answers = final_answers
            print("file is", f)

            self.assertEqual(assigned_jobs, answers)


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
