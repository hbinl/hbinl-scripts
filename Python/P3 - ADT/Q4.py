__author__ = 'HaoBin'

from Q8_1 import List
import queue

class Tree():
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

        if root is not None:
            if left is None:
                self.left = Tree()
            if right is None:
                self.right = Tree()


    def empty(self):
        if self.root is None:
            return True
        else:
            return False

    def leaf(self):
        if self.left is None and self.right is None:
            return True
        else:
            return False

    def fork(self):
        pass

    def get_left(self):
        if self.left is None:
            return None
        else:
            return self.left

    def get_right(self):
        if self.right is None:
            return None
        else:
            return self.right

    def contents(self):
        if self.root is None:
            return None
        else:
            return self.root

    def height(self):
        if self.empty() is True:
            return 0
        else:
            return 1 + max(self.left.height(), self.right.height())


    def weight(self):
        if self.empty() is True:
            return 0
        else:
            return 1 + self.left.weight() + self.right.weight()


    def breadth_first_draw(self):
        d = []
        q = queue.Queue()
        q.put(self)
        while q.empty() is False:
            v = q.get()
            if v.contents() is not None:
                print(v.contents(), end=" ")
            if v.leaf() is False:
                if v.get_left() is not None:
                    q.put(v.get_left())
                if v.get_right() is not None:
                    q.put(v.get_right())


    def flatten_infix(self):
        if self.empty() is True:
            return List()
        else:
            return self.left.flatten_infix().append(List(self.root, self.right.flatten_infix()))

    def flatten_prefix(self):
        if self.empty() is True:
            return List()
        else:
            return List(self.root, self.left.flatten_prefix().append(self.right.flatten_prefix()))

    def flatten_postfix(self):
        if self.empty() is True:
            return List()
        else:
            return self.left.flatten_postfix().append(self.right.flatten_postfix().append(List(self.root)))

    def fast_flatten_infix(self, l = None):
        if l is None:
            l = List()
        if self.empty() is True:
            return l
        else:
            return self.left.fast_flatten_infix(List(self.root, self.right.fast_flatten_infix(l)))


if __name__ == "__main__":
    tree = Tree(3, Tree(4, Tree(5)), Tree(8, Tree(7, Tree(9, Tree(4, Tree(11)), Tree(2)))))
    #print(tree.contents())
    print("Height: " + str(tree.height()))
    print("Weight: " + str(tree.weight()))

    print("Breadth first search:")
    tree.breadth_first_draw()

    x = tree.flatten_infix()
    print("\nInfix Flatten: ")
    for i in range(len(x)):
        print(x[i], end=" ")

    x = tree.flatten_prefix()
    print("\nPrefix Flatten: ")
    for i in range(len(x)):
        print(x[i], end=" ")

    x = tree.flatten_postfix()
    print("\nPostfix Flatten: ")
    for i in range(len(x)):
        print(x[i], end=" ")

    x = tree.fast_flatten_infix()
    print("\nFast Infix Flatten: ")
    for i in range(len(x)):
        print(x[i], end=" ")