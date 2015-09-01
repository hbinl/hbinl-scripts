__author__ = 'HaoBin'

from L2013LL import *


def xselect():
    x = 10000000
    for i in range(1,10000*10000):
        x = x*i
        print(i)
    t=0
    for i in range(x):
        t += 1
    print(t)

def select(a_list, f):
    if len(a_list) != 0:
        x = a_list[0]
        for i in range(len(a_list)-1):
            y = a_list[i+1]
            x = f(x,y)
        print(x)
    else:
        raise IndexError

def below_average(a_queue):
    tmp_queue = Queue()
    sum = 0
    count = 0
    while a_queue.is_empty() == False:
        x = a_queue.serve()
        tmp_queue.append(x)
        sum += x
        count += 1

    if count > 0:
        average = sum / count

    while tmp_queue.is_empty() == False:
        x = tmp_queue.serve()
        if x < average:
            a_queue.append(x)

    return a_queue


def swap_adjacent_items(self):
        self.swap_adj(self.head)


def swap_adj(self, current):
            if current.next is None:
                return

            else:
                a = current.item
                current.item = current.next.item
                current.next.item = a
                if current.next.next is not None:
                    self.swap_adj(current.next.next)

class PowerIterator:
    def __init__(self, base):
        self.base = base
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current = self.current * self.base
        return self.current

def collect_parents(self):
    if self.root is not None:
        parents = collect_parents_aux(self.root)
        return parents
    else:
        return []

def collect_parents_aux(self, current):
    list = []
    if current.left is not None or current.right is not None:

        if current.left is not None:
            b = collect_parents_aux(self, current.left)
            list = list + b

        list.append(current.item)

        if current.right is not None:
            b = collect_parents_aux(self, current.right)
            list = list + b

    return list


def factorial_rec(n, d):
    if n == 0:
        return (1, d)
    else:
        x = factorial_rec(n-1, d+1)
        return (n*x[0], x[1])



if __name__ == "__main__":
    #select([], max)
    print(factorial_rec(5,1))