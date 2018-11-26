class HashTable:

    def __init__(self, table_size):         # can add additional attributes
        self.table_size = table_size        # initial table size
        self.hash_table = [None]*table_size # hash table
        self.num_items = 0                  # empty hash table

    def insert(self, key, value = 0):
        """ Inserts an entry into the hash table (using Horner hash function to determine index, 
        and quadratic probing to resolve collisions).
        The key is a string (a word) to be entered, and value is the line number that the word appears on. 
        If the key is not already in the table, then the key is inserted, and the value is used as the first 
        line number in the list of line numbers. If the key is in the table, then the value is appended to that 
        key’s list of line numbers. If value is not used for a particular hash table (e.g. the stop words hash table),
        can use the default of 0 for value and just call the insert function with the key.
        If load factor is greater than 0.5 after an insertion, hash table size should be increased (doubled + 1)."""
        hashval = self.horner_hash(key)
        i = 0
        quad = 0
        if self.in_table(key):
            while self.hash_table[(hashval+quad)%self.table_size][0] != key:
                i += 1
                quad = i ** 2
            self.hash_table[(hashval+quad)%self.table_size][1].append(value)
        else:
            while self.hash_table[(hashval+quad)%self.table_size] != None:
                i += 1
                quad = i**2
            self.hash_table[(hashval+quad)%self.table_size] = (key, [value])
            self.num_items += 1
        #implement table doubling
        if self.get_load_factor() > 0.5:
            newSize = self.table_size * 2 + 1
            temphash = [None] * (newSize)
            self.table_size = newSize
            for k in self.hash_table:
                if k != None:
                    i = 0
                    quad = 0
                    hashval = self.horner_hash(k[0])
                    while temphash[(hashval+quad)%self.table_size] != None:
                        i += 1
                        quad = i**2
                    temphash[(hashval+quad)%self.table_size] = k
            self.hash_table = temphash

    def horner_hash(self, key):
        """ Compute and return an integer from 0 to the (size of the hash table) - 1
        Compute the hash value by using Horner’s rule, as described in project specification."""
        hashval = 0
        minimum = min(len(key), 8)
        for i in range(0, minimum):
            alpha = ord(key[i])
            hashval = (hashval*31 + alpha) % self.table_size
        return hashval

    def in_table(self, key):
        """ Returns True if key is in an entry of the hash table, False otherwise."""
        hashval = self.horner_hash(key)
        i = 0
        quad = 0
        stop = False
        while not stop: 
            if self.hash_table[(hashval+quad)%self.table_size] == None:
                stop = True
                return False
            elif self.hash_table[(hashval+quad)%self.table_size][0] == key:
                stop = True
                return True
            else:
                i += 1
                quad = i ** 2

    def get_index(self, key):
        """ Returns the index of the hash table entry containing the provided key. 
        If there is not an entry with the provided key, returns None."""
        hashval = self.horner_hash(key)
        if not self.in_table(key):
            return None
        i = 0
        quad = 0
        stop = False
        while not stop: 
            if self.hash_table[(hashval+quad)%self.table_size][0] == key:
                stop = True
                return (hashval+quad)%self.table_size
            else:
                i += 1
                quad = i ** 2

    def get_all_keys(self):
        """ Returns a Python list of all keys in the hash table."""
        returnlist = []
        for i in self.hash_table:
            if i != None:
                returnlist.append(i[0])
        #print(returnlist)
        return returnlist

    def get_value(self, key):
        """ Returns the value (list of line numbers) associated with the key. 
        If key is not in hash table, returns None."""
        if not self.in_table(key):
            return None
        #print(self.hash_table[self.get_index(key)][1])
        return self.hash_table[self.get_index(key)][1]

    def get_num_items(self):
        """ Returns the number of entries (words) in the table."""
        return self.num_items

    def get_table_size(self):
        """ Returns the size of the hash table."""
        return self.table_size

    def get_load_factor(self):
        """ Returns the load factor of the hash table (entries / table_size)."""
        return self.num_items/ self.table_size

    def return_all(self):
        returnlist = []
        for i in self.hash_table:
            if i != None:
                returnlist.append(i)
        return returnlist
