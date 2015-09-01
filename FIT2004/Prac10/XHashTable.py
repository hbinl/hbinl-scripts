__author__ = 'HaoBin'

class XHashTable():
    def __init__(self, size=7):
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

    def __getitem__(self, key):
        # lookup using quadratic probing
        # O(n) worst case complexity
        h = h_original = self.hash(key)
        for i in range(self.tablesize):
            if self.array[h] is None:
                return None
            elif self.array[h][0] == key:
                return self.array[h][1]
            else:
                h = (h_original + ((i+1) ** 2)) % self.tablesize
        return None


    def __setitem__(self, key, data):
        # Worst case O(n)
        # Best case O(1)
        self.check_load()
        h = h_original = self.hash(key)
        #print(h)

        for i in range(self.tablesize):
            if self.array[h] is None:
                self.array[h] = (key, data)
                self.count += 1
                return h
            elif self.array[h][0] == key:
                #f = self.array[h][1] + 1
                self.array[h] = (key, data)
                return h
            else:
                h = (h_original + ((i+1) ** 2)) % self.tablesize
            #print(h)
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
        #print(h,k)

        # delete the item, then shift appropriate objects in front quadratically
        if idx != -1:
            self.array[idx] = None
            self.count -= 1
            j_idx = ((k+1) ** 2)
            h = (h_original + ((k+1) ** 2)) % self.tablesize
            self.resize(1)
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
                h = self.__setitem__(x[0],x[1])
                #self.array[h][1] = x[1]
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
        return self.array

    def arrayList(self):
        # return the list of all elements in the hash table
        lst = []
        for i in range(len(self.array)):
            if self.array[i] is not None:
                lst.append(self.array[i])
        return lst
