import unittest
from quicksort import randomized_quick_sort
from random import randint


class TestQuickSort(unittest.TestCase):
    def test_small(self):
        for array in [
            ([1, 2, 3]),
            ([3, 2, 1]),
            ([2, 1, 3]),
            ([3, 1, 2]),
            ([1, 1, 2, 2, 3, 3]),
            ([1, 0, 1, 1, 2, 2]),
            ([2, 2, 2, 2, 0, 0]),
            ([0, 0, 1, 1, 2, 2]),
            ([3, 3, 2, 2, 1, 1]),
            ([0, 0, 2, 1, 1, 1, 0,1,1,0,0,0,1,2,2,2,2,2,0]),
            ([3, 0, 0, 0, 2, 1, 1, 1, 1, 1, 0, 3, 8, 4, 1, 2, 4, 3, 2, 2, 4, 4, 4, 5, 4, 3, 0, 8, 4, 4, 3, 4, 5, 2, 0, 0, 5, 5, 4, 0, 2, 4, 0, 9, 5, 10, 5, 2, 4, 4, 6, 6, 6, 6, 6, 6, 6, 10, 9, 9, 9, 8, 9, 7, 8, 7, 9, 8, 4, 3, 8, 3, 10, 9, 7, 1, 9, 7, 8, 10, 8, 9, 8, 7, 10, 8, 9, 10, 7, 9, 10, 10, 7, 10, 9, 8, 10, 8, 10, 9]),
        ]:
            sorted_array = sorted(list(array))
            randomized_quick_sort(array, 0, len(array) - 1)
            self.assertEqual(array, sorted_array)

    def test_large(self):
        for n in (10, 100, 10 ** 5):
            for max_value in (1, 2, 10, 10 ** 5):
                array = [randint(0, max_value) for _ in range(n)]
                sorted_array = sorted(list(array))
                randomized_quick_sort(array, 0, len(array) - 1)
                #print("query", array)
                self.assertEqual(array, sorted_array)


if __name__ == '__main__':
    unittest.main()
