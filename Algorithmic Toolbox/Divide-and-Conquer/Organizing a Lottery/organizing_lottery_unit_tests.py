import random
import unittest
from organizing_lottery import points_cover, points_cover_naive


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([0, 0], [1, 1], [1, 3, 5]),
            ([0, 10], [1, 8], [15]),
            ([0, 10], [1, 8], [0, 9]),
            ([5, 6], [1, 5], [0, 7]),
            ([5, 6], [1, 5], [2, 2,2,7]),
            ([1,1], [1, 1], [1]),
            ([5,1],[2,3],[1, 1]),
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    def test_random(self):
        starts = [random.randint(0, 5000) for _ in range(5000)]
        ends = [random.randint(starts[i], 10000) for i in range(len(starts))]
        points = [random.randint(0, 50000) for _ in range(5000)]
        points_cover(list(starts), list(ends), list(points)),
        self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                         points_cover_naive(starts, ends, points))

    def test_large(self):
        pass


if __name__ == '__main__':
    unittest.main()
