class minHeap:
    def __init__(self):
        self.count = 0
        self.array = [None]

    def __len__(self):
        return self.count

    def add(self, item):
        if self.count + 1 < len(self.array):
            self.array[self.count+1] = item
        else:
            self.array.append(item)

        self.count += 1
        self.rise(self.count)

    def swap(self, x, y):
        tmp = self.array[x]
        self.array[x] = self.array[y]
        self.array[y] = tmp

    def rise(self, k):
        while k > 1 and self.array[k] < self.array[k//2]:
            self.swap(k, k//2)
            k = k // 2

    def sink(self, k):
        while 2*k < self.count:
            child = self.smallest_child(k)
            if self.array[k] <= self.array[child]:
                break
            self.swap(child, k)
            k = child

    def smallest_child(self, k):
        if 2*k == self.count or self.array[2*k] < self.array[2*k+1]:
            return 2*k
        else:
            return 2*k + 1

    def serve(self):
        item = self.array[1]
        self.swap(1, self.count)
        self.count -= 1
        self.sink(1)
        return item