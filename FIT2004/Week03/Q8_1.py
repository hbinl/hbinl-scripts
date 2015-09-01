"""
@purpose Recursively defined ADT for List
@author Loh Hao Bin

"""
class List():
    def __init__(self, new_head=None, new_tail=None):
        if new_head is not None and new_tail is None:
            new_tail = List()
        self._head = new_head
        self._tail = new_tail

    def head(self):
        # returns the head of the list
        return self._head

    def tail(self):
        # returns the tail of the list
        return self._tail

    def __getitem__(self,index):
        # overloading [n] operator for construction purposes
        if index == 0:
            return self.head()
        else:
            return self.tail().__getitem__(index-1)

    def null(self):
        # returns if current list is nil
        if self.head() is None and self.tail() is None:
            return True
        return False

    def __len__(self):
        # overloading len operator to calculate length of list recursively
        if self.head() is None:
            return 0
        else:
            return 1 + len(self.tail())

    def append(self,L2):
        # append L1 with L2
        # if L1 is null, list = L2
        if self.null():
            self._head = L2.head()
            self._tail = L2.tail()
        elif self.null() is False and L2.null() is False:
            self = List(self.head(), self.tail().append(L2))
        return self

    def reverse(self):
        #reverse the list items     L(22, (55, (3, None))  L(22, (3, None))
        rev = self.reverse_rec()
        self._head = rev.head()
        self._tail = rev.tail()
        return self

    def reverse_rec(self):
        if self.null():
            pass
        else:
            return self._tail.reverse_rec().append(List(self._head))
        return self

    def merge(self, L2):
        merged = self.merge_rec(L2)
        self._head = merged.head()
        self._tail = merged.tail()
        return merged

    def merge_rec(self,L2):
        # Merge-sort L1 and L2, combining both list into one sorted list
        if L2.null() is True:
             return self
        elif self.null() is True and L2.null() is False:
            return L2
        else:
            if self.head() < L2.head():
                return List(self.head(), self.tail().merge_rec(L2))
            else:
                return List(L2.head(), self.merge_rec(L2.tail()))


if __name__ == "__main__":
    x = List(0,List(8,List(17, List(24, List(47)))))
    # print(x.tail())
    # print(x[4])
    print(len(x))

    z = List(1,List(5,List(12, List(20, List(50, List(80))))))
    #x.append(z)
    x.merge(z)
    #x.reverse()
    for i in range(len(x)):
        print(x[i], end=" ")

    # v = List(22, List(55, List(5)))
    # print(v[0])
    # b = List(3, List(0))
    # v.append(b)
    # for i in range(len(v)):
    #     print(v[i], end=" ")
    #
    # v.reverse()
    #
    # for i in range(len(v)):
    #     print(v[i], end=" ")



