__author__ = 'HaoBin'

class Node():
    def __init__(self, data, left=None, right=None):
        self.node = data
        self.left = None
        self.right = None

class NodeHeap():
    def __init__(self,root):
        self.root = Node(root)

#####################################

class Heap():
    def __init__(self):
        self.array = []
        self.count = 0

    def __len__(self):
        return self.count

    def empty(self):
        return self.count == 0

    def peek(self):
        if self.empty() is False:
            return self.array[0]
        else:
            return None

    def pop(self):
        if self.empty() is False:
            item = self.array[0]
            self.array[0] = self.array[self.count-1]
            self.downHeap(0)
            self.count -= 1
            return item
        else:
            return None

    def insert(self, key):
        self.array.append(key)
        self.count += 1
        k = self.count-1
        self.upHeap(k)

    def parent(self,i):
        if i == 0:
            return 0
        elif i % 2 == 0:
            return (i-2) // 2
        elif i % 2 == 1:
            return (i-1) // 2


    def upHeap(self,i):
        parent = self.parent(i)
        while self.array[parent] < self.array[i] and i > 0:
            self.array[i], self.array[parent] = self.array[parent], self.array[i]
            i = parent
            parent = self.parent(i)

    def downHeap(self,i):
        child= (2*i) + 1
        n = len(self)-1
        while child <= n:
            if child < n:
                if self.array[child] < self.array[child+1]:
                    child += 1
            if self.array[i] < self.array[child]:
                self.array[i], self.array[child] = self.array[child], self.array[i]
                i = child
                child = (2*i) + 1
            else:
                break




if __name__ == "__main__":
    x = Heap()
    x.insert(0)
    x.insert(1)
    print(x.array)

    x.insert(2)
    x.insert(3)
    x.insert(4)
    x.insert(5)
    x.insert(6)
    x.insert(7)
    # print(x.array)
    print(x.pop())
    #
    print(len(x))
    #x.insert(8)
    print(x.array)