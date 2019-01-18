import unittest
from stats_adt import *
from query import *


class TestSuite(unittest.TestCase):
    def test_createChampionQuery(self):
        champion = Query(2, 'Ahri')
        self.assertEqual(champion.champion, 'Ahri')
        self.assertEqual(champion.level, 2)
        self.assertEqual(champion.multiplier, 1)

    def test_multiply(self):
        champion = Query(2, 'Ahri')
        rtn_dict = champion.multiply()
        

if __name__ == '__main__':
    lowercase_all_dict_items(champions)
    unittest.main()
