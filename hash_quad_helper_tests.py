import unittest
from hash_quad import *

class TestList(unittest.TestCase):
    def test_05(self):
        hasht = HashTable(7)
        hasht.insert("mouse", 3)
        hasht.insert("mouse", 6)
        hasht.insert("hello", 6)
        hasht.insert("olleh", 6)
        self.assertEqual(hasht.get_table_size(),7)
        self.assertAlmostEqual(hasht.get_load_factor(), 3/7)
        hasht.insert("olleh", 1234)
        self.assertAlmostEqual(hasht.get_load_factor(), 3/7)
        self.assertEqual(hasht.get_index("mouse"), 4)
        hasht.insert("gop", 1)
        self.assertAlmostEqual(hasht.get_load_factor(), 4/15)
        self.assertEqual(hasht.get_index("mouse"), 13)
        self.assertEqual(hasht.get_index("gop"), 11)
        self.assertEqual(hasht.get_index("olleh"), 8)
        self.assertEqual(hasht.get_index("hello"), 7)
        self.assertEqual(hasht.get_all_keys(), ["hello", "olleh", "gop", "mouse"])
        self.assertEqual(hasht.get_index("ehllo"), None)
        self.assertEqual(hasht.get_value("mouse"), [3,6])
        self.assertEqual(hasht.get_value(""), None)
        self.assertEqual(hasht.get_num_items(), 4)
        self.assertEqual(hasht.get_table_size(), 15)
        self.assertEqual(hasht.return_all(), [("hello", [6]), ("olleh", [6, 1234]), ("gop", [1]), ("mouse", [3, 6])])





if __name__ == '__main__':
   unittest.main()
