import unittest
import numpy as np
from topsis import Topsis

class TestTopsis(unittest.TestCase):
    def test_calculate(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        weights = [0.5, 0.3, 0.2]
        impacts = ['+', '+', '-']
        topsis = Topsis(data, weights, impacts)
        scores = topsis.calculate()
        self.assertEqual(len(scores), 3)

if __name__ == '__main__':
    unittest.main()
