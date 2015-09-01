__author__ = 'HaoBin'


class MinHeapPQ():
    def __init__(self):
        self.array = []
        self.count = 0
        self.keyIndexMap = {}

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
            self.array[self.count-1][0] = float("inf")
            self.keyIndexMap[self.array[0][1]] = 0
            self.downHeap(0)
            del self.keyIndexMap[item[1]]
            self.count -= 1

            if self.empty():
                self.reset()

            return item
        else:
            return None

    def reset(self):
        # resets the priority queue
        self.count = 0
        self.array = []

    def insert(self, key, data="-"):
        self.array.append([key, data])
        self.count += 1
        k = self.count-1
        self.keyIndexMap[data] = self.upHeap(k)

    def parent(self,i):
        if i == 0:
            return 0
        elif i % 2 == 0:
            return (i-2) // 2
        elif i % 2 == 1:
            return (i-1) // 2


    def upHeap(self,i):
        parent = self.parent(i)
        while self.array[parent][0] > self.array[i][0] and i > 0:
            self.array[i], self.array[parent] = self.array[parent], self.array[i]
            self.keyIndexMap[self.array[i][1]] = i
            self.keyIndexMap[self.array[parent][1]] = parent
            i = parent
            parent = self.parent(i)
        return i


    def downHeap(self,i):
        child= (2*i) + 1
        n = len(self)-1
        while child <= n:
            if child < n:
                if self.array[child][0] > self.array[child+1][0]:
                    child += 1
            if self.array[i][0] > self.array[child][0]:
                self.array[i], self.array[child] = self.array[child], self.array[i]
                self.keyIndexMap[self.array[i][1]] = i
                self.keyIndexMap[self.array[child][1]] = child
                i = child
                child = (2*i) + 1
            else:
                break

        return i


    def decrease_key(self, value, priority_key):
        k = self.keyIndexMap[value]
        if self.array[k][1] == value:
            self.array[k][0] = priority_key
            self.upHeap(k)


if __name__ == "__main__":
    x = MinHeapPQ()
    # x.insert(0)
    # x.insert(1)
    # x.insert(3)
    # print(x.array)
    # x.insert(4)
    # x.insert(7)
    # x.insert(329)
    # x.insert(3)
    # x.insert(2)
    # x.insert(6)
    # x.insert(-6)
    # x.insert(9)
    # x.insert(3)
    # x.insert(3298471)
    # x.insert(5)
    # x.insert(3)
    # x.insert(-4)
    #
    # # print(x.array)
    # #print(x.pop())
    # #
    # print(len(x))
    # #x.insert(8)
    # print(x.array)
    # for i in range(len(x)):
    #     print(x.pop())
    inf = float("inf")


    x.insert(inf, 5)
    print(x.array)
    x.insert(4, 25)
    print(x.array)
    x.insert(1, 9)
    print(x.array)
    x.insert(inf, 63)
    print(x.array)
    x.insert(6,1)
    print(x.array)
    print(x.keyIndexMap)
    for i in range(len(x)):
        print(x.pop())
        print(x.array, x.keyIndexMap)

    x.insert(inf, 5)
    print(x.array)
    x.insert(4, 25)
    print(x.array)
    x.insert(1, 9)
    print(x.array)
    x.insert(inf, 63)
    print(x.array)
    x.insert(6,1)
    print(x.array)
    x.decrease_key(1, 0)
    x.decrease_key(5, 999)
    x.decrease_key(63, 12)

    print()
    for i in range(len(x)):
        print(x.pop())

