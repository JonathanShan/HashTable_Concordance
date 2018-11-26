from hash_quad import *
import string

class Concordance:

    def __init__(self):
        self.stop_table = None          # hash table for stop words
        self.concordance_table = None   # hash table for concordance

    def is_num(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def load_stop_table(self, filename):
        """ Read stop words from input file (filename) and insert each word as a key into the stop words hash table.
        Starting size of hash table should be 191: self.stop_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.stop_table = HashTable(191)
        file = open(filename, 'r')
        for line in file:
            for word in line.split():
                self.stop_table.insert(word)
        file.close()

    def load_concordance_table(self, filename):
        """ Read words from input text file (filename) and insert them into the concordance hash table, 
        after processing for punctuation, numbers and filtering out words that are in the stop words hash table.
        Do not include duplicate line numbers (word appearing on same line more than once, just one entry for that line)
        Starting size of hash table should be 191: self.concordance_table = HashTable(191)
        If file does not exist, raise FileNotFoundError"""
        self.concordance_table = HashTable(191)
        file = open(filename, 'r')
        linenum = 0
        for line in file:
            for punc in string.punctuation:
                if punc == '-':
                    line = line.replace(punc, " ")
                line = line.replace(punc, "")
            linenum += 1
            words_seen = []
            for word in line.split():
                word = word.lower()
                if word not in words_seen and word not in self.stop_table.get_all_keys():
                    if not self.is_num(word):
                        self.concordance_table.insert(word, linenum)
                        words_seen.append(word)
        file.close()

    def write_concordance(self, filename):
        """ Write the concordance entries to the output file(filename)
        See sample output files for format."""
        file = open(filename, 'w')
        keylist = self.concordance_table.return_all()
        keylist.sort()
        for key in keylist:
            returnstring = ''
            for item in key[1]:
                returnstring = returnstring + " " + str(item)
            if key != keylist[0]:
                file.write("\n")
            file.write(key[0] + ":" + returnstring)
        file.close()
