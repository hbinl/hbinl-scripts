__author__ = 'HaoBin'

class XSet():
    def __init__(self):
        self.parent = {}
        self.rank = {}


    def makeSet(self,node):
        self.parent[node] = node
        self.rank[node] = 0


    def findSet(self,node):

        if self.parent[node] != node:
            self.parent[node] = self.findSet(self.parent[node])
        return self.parent[node]

    def union(self,x,y):
        x_root = self.findSet(x)
        y_root = self.findSet(y)
        if x_root == y_root:
            return

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def getSets(self):
        for item in self.parent.items():
            self.findSet(item[0])


        set_map = {}
        for item in self.parent.items():
            try:
                set_map[item[1]] = set_map[item[1]] + [item[0]]
            except KeyError:
                set_map[item[1]] = [item[0]]

        return list(set_map.items())

    def getPartition(self, node):
        root = self.findSet(node)
        part = []
        for item in self.parent.items():
            if item[1] == root:
                part.append(item[0])
            else:
                x = self.findSet(item[0])
                if x == root:
                    part.append(item[0])
        return part



