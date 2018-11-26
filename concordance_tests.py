import unittest
import filecmp
from concordance import *

class TestList(unittest.TestCase):

   def test_01(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file1.txt")
       conc.write_concordance("file1_con.txt")
       self.assertTrue(filecmp.cmp("file1_con.txt", "file1_sol.txt"))

   def test_02(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("file2.txt")
       conc.write_concordance("file2_con.txt")
       self.assertTrue(filecmp.cmp("file2_con.txt", "file2_sol.txt"))

   def test_03(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("declaration.txt")
       conc.write_concordance("declaration_con.txt")
       self.assertTrue(filecmp.cmp("declaration_con.txt", "declaration_sol.txt"))

   def test_04(self):
       conc = Concordance()
       self.assertRaises(FileNotFoundError, conc.load_stop_table, "stop_words13.txt")
       self.assertRaises(FileNotFoundError, conc.load_concordance_table, "stop_words13.txt")

   def test_05(self):
       conc = Concordance()
       conc.load_stop_table("empty.txt")
       conc.load_concordance_table("empty.txt")
       conc.write_concordance("empty_con.txt")
       self.assertTrue(filecmp.cmp("empty_con.txt", "empty.txt"))

   def test_06(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("repeat.txt")
       conc.write_concordance("repeat_con.txt")
       self.assertTrue(filecmp.cmp("repeat_con.txt", "repeat_sol.txt"))

   def test_07(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("random.txt")
       conc.write_concordance("random_con.txt")
       self.assertTrue(filecmp.cmp("random_con.txt", "random_sol.txt"))

   def test_08(self):
       conc = Concordance()
       conc.load_stop_table("stop_words.txt")
       conc.load_concordance_table("wrap.txt")
       conc.write_concordance("wrap_con.txt")
       self.assertTrue(filecmp.cmp("wrap_con.txt", "wrap_sol.txt"))


if __name__ == '__main__':
   unittest.main()
