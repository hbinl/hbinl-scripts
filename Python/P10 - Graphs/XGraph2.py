__author__ = 'HaoBin'

from XHashTable import XHashTable


class XGraph():
    def __init__(self):
        # directed = False if non-directed graph, and otherwise
        self.verticesCount = 0
        self.edgesCount = 0
        self.verticeList = XHashTable()
        self.edgesList = XHashTable()

    def __len__(self):
        return self.verticesCount

    def empty(self):
        return self.verticesCount == 0

    def getEdgeCount(self):
        return self.edgesCount

    def getVertices(self):
        return self.verticeList.arrayList()

    def getVerticesList(self):
        # Complexity: O(|V|)
        lst = []
        for v in self.verticeList.arrayList():
            lst.append(v[0])
        return lst

    def addVertex(self, id):
        self.verticesCount += 1
        self.verticeList.__setitem__(id, XVertice(id))
        return True

    def __getitem__(self, id):
        return self.verticeList[id]

    def __contains__(self, id):
        if self.verticeList[id] is not None:
            return True
        else:
            return False

    def deleteVertex(self, id):
        # Complexity: O(|V|)
        self.verticesCount -= 1
        if self.verticeList[id] is None:
            # print(self.getVerticesList())
            raise KeyError
        else:
            self.verticeList.delete(id)

            if self.edgesList[id] is not None:
                self.edgesCount -= len(self.edgesList[id])

            for v in self.getVertices():
                k = self.edgesList[v[0]]
                if k is not None:
                    k.delete(id)
            self.edgesList.delete(id)

    def addEdge(self, id1, id2, weight=0, directed=False):
        # Complexity: O(1)
        # id1 = origin vertex
        # id2 = target vertex
        # weight = cost of the edge
        # if directed edge, id1 would be the origin
        if id1 not in self:
            self.addVertex(id1)
        if id2 not in self:
            self.addVertex(id2)

        edge = XEdge(self[id1], self[id2], weight, directed)

        if self.edgesList[id1] is None:
            self.edgesList[id1] = XHashTable()

        self.edgesList[id1][id2] = edge

        if directed is False:
            if self.edgesList[id2] is None:
                self.edgesList[id2] = XHashTable()
            self.edgesList[id2][id1] = XEdge(self[id2], self[id1], weight, directed)

        self.edgesCount += 1
        return edge


    def deleteEdge(self, id1, id2):
        # id1 is origin in directed graph
        if id1 not in self or id2 not in self:
            raise KeyError
        else:
            edge = self.edgesList[id1][id2]
            if edge.isDirected() is False:
                self.edgesList[id2].delete(id1)
            self.edgesList[id1].delete(id2)
            self.edgesCount -= 1
            # return edge

    def getEdge(self, v1, v2):
        if v1 not in self:
            return None
        elif v2 not in self:
            return None
        else:
            if self.edgesList[v1] is not None:
                return self.edgesList[v1][v2]
            else:
                return None

    def getConnections(self, v):
        edge = self.edgesList[v]
        if edge is not None:
            return edge.arrayList()
        else:
            return []

    def getDegree(self, v):
        # Returns the degree of the vertex v
        # if directed, returns the out-degree
        return len(self.getConnections(v))

    def getInDegree(self, v_node):
        # Complexity: O(|V|)
        vs = self.getVerticesList()
        count = 0
        for v in vs:
            for c in self.getConnections(v):
                if c[0] == v_node:
                    count += 1
        return count

    def connectedTo(self, v1, v2):
        if self.edgesList[v1] is not None:
            node = self.edgesList[v1][v2]
        else:
            node = None

        if node is None:
            return False
        else:
            return True

    def getCostOfConnection(self, v1, v2):
        return self.edgesList[v1][v2].getCost()


    def toStrConnection(self):
        # Complexity: O(|E|) or O(|V|^2)
        for v in self.getVertices():
            for c in self.getConnections(v[0]):
                print(v[1].getID(), ">", c[1].getV2().getID())


class XEdge():
    def __init__(self, v1, v2, weight, directed=False):
        self.v1 = v1
        self.v2 = v2
        self.directed = directed
        self.cost = weight

    def isDirected(self):
        return self.directed

    def getCost(self):
        return self.cost

    def getV2(self):
        return self.v2

    def getV1(self):
        return self.v1

    def strConnection(self):
        return self.v1.getID() + " " + self.v2.getID()


class XVertice():
    def __init__(self, key):
        self.id = key

    def getID(self):
        return self.id
