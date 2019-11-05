import unittest
from unittest.mock import MagicMock, patch
from api import Api


class Test(unittest.TestCase):

    def test_api_positions(self):
        json1 = {"response": True, "size": "9", "squares": [{"x": 0, "y": 1, "value": 5}, {"x": 0, "y": 2, "value": 2}, {"x": 0, "y": 4, "value": 3}, {"x": 0, "y": 6, "value": 9}, {"x": 0, "y": 7, "value": 8}, {"x": 1, "y": 0, "value": 3}, {"x": 1, "y": 4, "value": 5}, {"x": 1, "y": 5, "value": 9}, {"x": 1, "y": 8, "value": 2}, {"x": 2, "y": 0, "value": 9}, {"x": 2, "y": 3, "value": 7}, {"x": 2, "y": 4, "value": 1}, {"x": 2, "y": 5, "value": 2}, {"x": 2, "y": 7, "value": 5}, {"x": 3, "y": 1, "value": 3}, {"x": 3, "y": 2, "value": 9}, {"x": 3, "y": 3, "value": 2}, {"x": 3, "y": 4, "value": 8}, {"x": 3, "y": 6, "value": 7}, {
            "x": 4, "y": 2, "value": 5}, {"x": 4, "y": 6, "value": 8}, {"x": 4, "y": 8, "value": 6}, {"x": 5, "y": 1, "value": 7}, {"x": 5, "y": 2, "value": 8}, {"x": 5, "y": 4, "value": 6}, {"x": 5, "y": 5, "value": 5}, {"x": 5, "y": 6, "value": 2}, {"x": 6, "y": 0, "value": 8}, {"x": 6, "y": 3, "value": 3}, {"x": 6, "y": 5, "value": 6}, {"x": 7, "y": 0, "value": 5}, {"x": 7, "y": 1, "value": 2}, {"x": 7, "y": 2, "value": 7}, {"x": 7, "y": 6, "value": 3}, {"x": 7, "y": 8, "value": 4}, {"x": 8, "y": 1, "value": 6}, {"x": 8, "y": 2, "value": 3}, {"x": 8, "y": 4, "value": 2}, {"x": 8, "y": 6, "value": 1}, {"x": 8, "y": 7, "value": 9}]}
        magicmock = MagicMock()
        magicmock.json = MagicMock(return_value=json1)
        with patch("api.requests.get", return_value=magicmock):
            response = Api().positions_fixed()
        self.assertEqual(response, {1: 5, 2: 2, 4: 3, 6: 9, 7: 8, 9: 3, 13: 5, 14: 9, 17: 2, 18: 9, 21: 7, 22: 1, 23: 2, 25: 5, 28: 3, 29: 9, 30: 2, 31: 8, 33: 7,
                                    38: 5, 42: 8, 44: 6, 46: 7, 47: 8, 49: 6, 50: 5, 51: 2, 54: 8, 57: 3, 59: 6, 63: 5, 64: 2, 65: 7, 69: 3, 71: 4, 73: 6, 74: 3, 76: 2, 78: 1, 79: 9})

    def test_api_make_board(self):
        json1 = {"response": True, "size": "9", "squares": [{"x": 0, "y": 1, "value": 5}, {"x": 0, "y": 2, "value": 2}, {"x": 0, "y": 4, "value": 3}, {"x": 0, "y": 6, "value": 9}, {"x": 0, "y": 7, "value": 8}, {"x": 1, "y": 0, "value": 3}, {"x": 1, "y": 4, "value": 5}, {"x": 1, "y": 5, "value": 9}, {"x": 1, "y": 8, "value": 2}, {"x": 2, "y": 0, "value": 9}, {"x": 2, "y": 3, "value": 7}, {"x": 2, "y": 4, "value": 1}, {"x": 2, "y": 5, "value": 2}, {"x": 2, "y": 7, "value": 5}, {"x": 3, "y": 1, "value": 3}, {"x": 3, "y": 2, "value": 9}, {"x": 3, "y": 3, "value": 2}, {"x": 3, "y": 4, "value": 8}, {"x": 3, "y": 6, "value": 7}, {
            "x": 4, "y": 2, "value": 5}, {"x": 4, "y": 6, "value": 8}, {"x": 4, "y": 8, "value": 6}, {"x": 5, "y": 1, "value": 7}, {"x": 5, "y": 2, "value": 8}, {"x": 5, "y": 4, "value": 6}, {"x": 5, "y": 5, "value": 5}, {"x": 5, "y": 6, "value": 2}, {"x": 6, "y": 0, "value": 8}, {"x": 6, "y": 3, "value": 3}, {"x": 6, "y": 5, "value": 6}, {"x": 7, "y": 0, "value": 5}, {"x": 7, "y": 1, "value": 2}, {"x": 7, "y": 2, "value": 7}, {"x": 7, "y": 6, "value": 3}, {"x": 7, "y": 8, "value": 4}, {"x": 8, "y": 1, "value": 6}, {"x": 8, "y": 2, "value": 3}, {"x": 8, "y": 4, "value": 2}, {"x": 8, "y": 6, "value": 1}, {"x": 8, "y": 7, "value": 9}]}
        magicmock = MagicMock()
        magicmock.json = MagicMock(return_value=json1)
        with patch("api.requests.get", return_value=magicmock):
            response = Api().make_board()
        self.assertEqual(
            response, "x52x3x98x3xxx59xx29xx712x5xx3928x7xxxx5xxx8x6x78x652xx8xx3x6xxx527xxx3x4x63x2x19x")


if __name__ == '__main__':
    unittest.main()
