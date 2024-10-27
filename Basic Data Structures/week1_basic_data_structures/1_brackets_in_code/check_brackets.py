# python3

from collections import namedtuple

import unittest
import os
import logging
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)
logging.Logger.disabled = True

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):

    opening_brackets_stack = []
    stack_id = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            stack_id.append(i)
        elif next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            elif are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop(-1)
                stack_id.pop(-1)
            else:
                logging.debug("text is: %s; res is: %d, lis is %s" % (text, i + 1, opening_brackets_stack))
                return i + 1

    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        logging.debug("text is: %s; res is: %d, lis is %s" % (text, len(text), opening_brackets_stack))
        return stack_id[0] + 1


"""
class TestSolution(unittest.TestCase):
    def test(self):
        files = get_files()
        for f in files:
            with open(f, 'r') as fs:
                text = fs.read().strip()
            with open(f + ".a", "r") as fs:
                answer = fs.read().strip()
            if answer != "Success":
                answer = int(answer)
            value = find_mismatch(text)
            logging.debug("text is: %s, value is: %s, answer is: %s" % (text, str(value), str(answer)))
            self.assertEqual(value, answer)
"""


def get_files():

    files = []
    path = os.path.join(os.getcwd(), "tests")
    for file in os.listdir(path):
        if file.split(".")[-1] == "a":
            continue
        files.append(os.path.join(path, file))

    return files


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
