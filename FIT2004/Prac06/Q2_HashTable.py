__author__ = 'HaoBin'

class HashTable():
    def __init__(self, size=11):
        # 11 because it's a small enough prime
        # just initialising...
        self.count = 0
        self.tablesize = size
        self.array = [None] * size

    def __len__(self):
        return self.count

    def load(self):
        return self.count / self.tablesize

    def table_size(self):
        return self.tablesize

    def lookup(self, key):
        # lookup using quadratic probing
        # O(n) worst case complexity
        h = h_original = self.hash(key)
        for i in range(self.tablesize):
            if self.array[h] is None:
                return False
            elif self.array[h][0] == key:
                return True
            else:
                h = (h_original + ((i+1) ** 2)) % self.tablesize
        return False

    def lookup_freq(self, key):
        # lookup frequency of a key using quadratic probing
        # O(n) worst case complexity
        h = h_original = self.hash(key)
        for i in range(self.tablesize):
            if self.array[h] is None:
                return 0
            elif self.array[h][0] == key:
                return self.array[h][1]
            else:
                h = (h_original + ((i+1) ** 2)) % self.tablesize
        return 0

    def insert(self, key):
        # Worst case O(n)
        # Best case O(1)
        self.check_load()
        h = h_original = self.hash(key)

        for i in range(self.tablesize):
            if self.array[h] is None:
                self.array[h] = [key, 1]
                self.count += 1
                return h
            elif self.array[h][0] == key:
                f = self.array[h][1] + 1
                self.array[h] = [key, f]
                return h
            else:
                h = (h_original + ((i+1) ** 2)) % self.tablesize
        raise KeyError

    def check_load(self):
        if self.load() > 0.5:
            self.resize()

    def delete(self, key):
        # Worst case, O(n)
        # Best case: O(1)
        h = h_original = self.hash(key)

        idx = -1
        k = 0
        # probe for the item to be deleted, and get its index
        for i in range(self.tablesize):
            if self.array[h] is None:
                break
            elif self.array[h][0] == key:
                k = i
                idx = h
                break
            else:
                h = (h_original + ((i+1) ** 2)) % self.tablesize

        # delete the item, then shift appropriate objects in front quadratically
        if idx != -1:
            self.array[idx] = None
            self.count -= 1
            h = (h_original + ((k+1) ** 2)) % self.tablesize
            while self.array[h] is not None and self.hash(self.array[h][0]) == h_original:
                x = self.array[h]
                new_h = self.insert(self.array[h][0])
                self.count -= 1
                self.array[new_h][1] = x[1]
                self.array[h] = None
                k += 1
                h = (h_original + ((k+1) ** 2)) % self.tablesize
            return True
        else:
            return False

    def resize(self, factor=2):
        # rehash everything!!11@!!11@!!
        # complexity O(n)
        self.tablesize = self.tablesize * factor
        tmp = self.array
        tmp_count = 0
        self.array = [None] * self.tablesize
        for x in tmp:
            if x is not None:
                h = self.insert(x[0])
                self.array[h][1] = x[1]
                tmp_count += 1
        self.count = tmp_count

    def hash(self, word):
        value = 0
        a = 31415
        b = 27183
        for i in range(len(word)):
            value = (ord(word[i]) + a*value) % self.tablesize
            a = a * b % (self.tablesize - 1)
        return value

    def toStr(self):
        print(self.array)

    def arraylist(self):
        # return the list of all elements in the hash table
        lst = []
        for i in range(len(self.array)):
            if self.array[i] is not None:
                lst.append(self.array[i])
        return lst

################ MISCELLANEOUS UNUSED ABANDONED FUNCTIONS

def flatten(bt):
    # Unused
    # Flatten a nested list
    result = []
    for i in bt:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in flatten(i):
                result.append(j)
        else:
            result.append(i)
    return result

def convert_btree(i, j, r, n):
    # UNUSED
    # recursively generates a pre-ordered binary tree from r
    tree = []
    #k = trimatrix_translate(i, j, n)
    if i == j:
        if r[k] == 0:
            return [None]
        else:
            return [r[k]]
    else:
        tree.append(r[k])
        tree += convert_btree(i, r[k]-1, r, n)
        tree += convert_btree(r[k], j, r, n)
        return tree

################ MISCELLANEOUS UNUSED ABANDONED FUNCTIONS


def meta(x):
    print("Table Size: " + str(x.table_size()) + " Count: " + str(len(x)) + " Load: " + str(x.load()))
    x.toStr()
    print()

if __name__ == "__main__":
    x = HashTable()
    meta(x)
    print(x.insert("bc"))
    meta(x)
    print(x.insert("bc"))
    meta(x)
    print(x.insert("cd"))
    print(meta(x))
    print(x.lookup("bc"))
    print(x.lookup_freq("bc"))
    print(x.lookup("cd"))
    print(x.lookup_freq("cd"))

    print(x.insert("dg"))
    meta(x)

    print(x.insert("cbb"))
    meta(x)
    print(x.insert("ebad"))
    meta(x)
    print(x.insert("xd"))
    meta(x)
    print(x.insert("ded")) #<
    meta(x)
    print(x.insert("vds"))
    meta(x)
    print(x.insert("abb"))
    meta(x)
    print(x.insert("abad"))
    meta(x)
    print(x.insert("abad"))
    meta(x)
    print(x.insert("abad"))
    meta(x)

    print(x.delete("cd"))
    meta(x)

    print(x.hash("abb"))
    print(x.hash("abad"))
    print(x.hash("bc"))

