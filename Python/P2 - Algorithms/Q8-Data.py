"""
@purpose Recursively defined ADT for List
@author Loh Hao Bin

"""

class List():
    def __init__(self,h=[],t=[]):

        if h == "nil" or h == []:
            # if constructing a nil object
            self.data = ["nil"]
            self._head = "nil"
            self._tail = "nil"
        else:
            # construct an ordinary recursive list
            self.data = self.cons(h,t)
            self._head = self.data[0]
            self._tail = self.data[1]

    def cons(self,h=[],t=[]):
        list = [h]
        if len(t) == 0:
            # if tail is nil or doesn't have data, create nil List object
            list.append(List("nil"))
        else:
            # append tail
            list.append(List(t[0],t[1:len(t)]))

        return list

    def view(self, index):
        # Returns the item in the specified index
        # a recursive function for viewing the data stored in each List object
        if index == 0:
            return self._head
        else:
            return self._tail.view(index-1)

    def __getitem__(self,index):
        # overloading [n] operator for construction purposes
        if index == 0:
            return self.head()
        else:
            return self.tail()

    def null(self):
        # returns if current list is nil
        return self._head == "nil"

    def __len__(self):
        # overloading len operator to calculate length of list recursively
        if self.null() == True:
            return 0
        else:
            return 1 + len(self._tail)

    def head(self):
        # returns the head of the list
        if self._head == "nil":
            raise ValueError
        else:
            return self._head

    def tail(self):
        # returns the tail of the list
        if self._tail == "nil":
            raise ValueError
        else:
            return self._tail

    def append(self,L2):
        # append L1 with L2
        # if L1 is null, list = L2
        if self.null() == True:
            self.data = L2
            self._head = L2.head()
            self._tail = L2.tail()

        elif self.null() == False and L2.null() == False:
            self.data = self.cons(self._head, self._tail.append(L2))

        return self

    def reverse(self):
        #reverse the list items
        self.data = self.reverse_rec().data
        self._head = self.data[0]
        self._tail = self.data[1]


    def reverse_rec(self):
        if self.null() == True:
            pass
        else:
            self = self._tail.reverse_rec().append(List(self._head))

        return self


    def merge(self,L2):
        # Merge-sort L1 and L2, combining both list into one sorted list
        if self.null() == True and L2.null() == True:
            return self
        elif self.null() == True and L2.null() == False:
            return L2
        elif self.null() == False and L2.null() == True:
            return self
        else:
            if self._head < L2.head():
                self.data = self.cons(self._head, self._tail.merge(L2))
                self._head = self.data[0]
                self._tail = self.data[1]
            else:
                self.data = self.cons(L2.head(), self.merge(L2.tail()))
                self._head = self.data[0]
                self._tail = self.data[1]
            return self


if __name__ == "__main__":
    x = List(7,[9,11,13])
    print(x.view(3))

    x2 = List(72, x)

    #x.append(x2)
    #print(len(x))

    #x.merge(x2)
    print(len(x2))

    for i in range(len(x2)):
        print(x2.view(i), end=" ")

