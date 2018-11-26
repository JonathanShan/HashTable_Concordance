import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_num_items(), 0)

    def test_01c(self):
        ht = HashTable(7)
        self.assertAlmostEqual(ht.get_load_factor(), 0)

    def test_01d(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_all_keys(), [])

    def test_01e(self):
        ht = HashTable(7)
        self.assertEqual(ht.in_table("cat"), False)

    def test_01f(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_value("cat"), None)

    def test_01g(self):
        ht = HashTable(7)
        self.assertEqual(ht.get_index("cat"), None)

    def test_01h(self):
        ht = HashTable(7)
        self.assertEqual(ht.horner_hash("cat"), 3)

    def test_02a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_02b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_02c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_02d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_02e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_02f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), [5])

    def test_02g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_03(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        ht.insert("cat", 17)
        self.assertEqual(ht.get_value("cat"), [5, 17])

    def test_04(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

        ht.insert("dog", 8)
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_index("dog"), 6)
        self.assertAlmostEqual(ht.get_load_factor(), 2 / 7)

        ht.insert("mouse", 10)
        self.assertEqual(ht.get_num_items(), 3)
        self.assertEqual(ht.get_index("mouse"), 4)
        self.assertAlmostEqual(ht.get_load_factor(), 3 / 7)

        ht.insert("elephant", 12) # hash table should be resized
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertAlmostEqual(ht.get_load_factor(), 4 / 15)
        self.assertEqual(ht.get_index("cat"), 12)
        self.assertEqual(ht.get_index("dog"), 14)
        self.assertEqual(ht.get_index("mouse"), 13)
        self.assertEqual(ht.get_index("elephant"), 9)
        keys = ht.get_all_keys()
        keys.sort()
        self.assertEqual(keys, ["cat", "dog", "elephant", "mouse"])

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
        self.assertEqual(hasht.get_table_size(), 15)
        hasht.insert("wajognik")
        self.assertEqual(hasht.get_index("wajognik"), 3)
        hasht.insert("wajognikne")
        self.assertEqual(hasht.get_index("wajognikne"), 4)
        hasht.insert("wajognikneeeeeeeeeeeeeeee")
        self.assertEqual(hasht.get_index("wajognikneeeeeeeeeeeeeeee"), 12)

    def test_06(self):
        hasht = HashTable(191)
        hasht.insert("whatever", 1)
        hasht.insert("whatevery", 2)
        hasht.insert("whateveryy", 3)
        hasht.insert("whateveryyy", 4)
        hasht.insert("whateveryyyy", 5)
        hasht.insert("whateveryyyyy", 6)
        hasht.insert("whateveryyyyyy", 7)
        hasht.insert("whateveryyyyyyy", 8)
        hasht.insert("whateveryyyyyyyy", 9)
        hasht.insert("whateveryyyyyyyyy", 10)
        hasht.insert("whateveryyyyyyyyyy", 11)
        hasht.insert("whateveryyyyyyyyyyy", 12)
        hasht.insert("whateveryyyyyyyyyyyy", 13)
        hasht.insert("whateveryyyyyyyyyyyyy", 14)
        hasht.insert("whateveryyyyyyyyyyyyyy", 15)
        hasht.insert("whateveryyyyyyyyyyyyyyy", 16)
        self.assertEqual(hasht.get_index("whatever"), 28)
        self.assertEqual(hasht.get_index("whatevery"), 29)
        self.assertEqual(hasht.get_index("whateveryy"), 32)
        self.assertEqual(hasht.get_index("whateveryyy"), 37)
        self.assertEqual(hasht.get_index("whateveryyyy"), 44)
        self.assertEqual(hasht.get_index("whateveryyyyy"), 53)
        self.assertEqual(hasht.get_index("whateveryyyyyy"), 64)
        self.assertEqual(hasht.get_index("whateveryyyyyyy"), 77)
        self.assertEqual(hasht.get_index("whateveryyyyyyyy"), 92)
        self.assertEqual(hasht.get_index("whateveryyyyyyyyy"), 109)
        self.assertEqual(hasht.get_index("whateveryyyyyyyyyy"), 128)
        self.assertEqual(hasht.get_index("whateveryyyyyyyyyyy"), 149)
        self.assertEqual(hasht.get_index("whateveryyyyyyyyyyyy"), 172)
        self.assertEqual(hasht.get_index("whateveryyyyyyyyyyyyy"), 6)
        self.assertEqual(hasht.get_index("whateveryyyyyyyyyyyyyy"), 33)
        self.assertEqual(hasht.get_index("whateveryyyyyyyyyyyyyyy"), 62)

    def test_07(self):
        hasht = HashTable(7)
        hasht.insert("eightletter", 3)
        self.assertEqual(hasht.get_index("eightletter"),3)
        hasht.insert("eightletterfer", 3)
        self.assertEqual(hasht.get_index("eightletterfer"), 4)
        hasht.insert("eightletteradaw", 1)
        self.assertEqual(hasht.get_index("eightletteradaw"), 0)
        hasht.insert("eightletterdf", 5)
        self.assertEqual(hasht.get_index("eightletteradaw"), 14)
        self.assertEqual(hasht.get_index("eightletter"), 0)
        self.assertEqual(hasht.get_index("eightletterfer"), 3)
        self.assertEqual(hasht.get_index("eightletterdf"), 8)

        

if __name__ == '__main__':
   unittest.main()
