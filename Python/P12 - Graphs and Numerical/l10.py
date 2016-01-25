__author__ = 'HaoBin'

from Prac12.XGraph2 import *
from Prac12.XMinHeap import *

def Kahn(g):
    ts = []
    p = MinHeapPQ()
    for v in g.getVerticesList():
        if g.getInDegree(v) == 0:
            p.insert(1, v)
    #print(p.array)
    while p.empty() is False:
        x = p.pop()[1]
        #print(p.array)


        ts.append(x)
        for y in g.getConnections(x):
            #print(x,y)
            g.deleteEdge(x,y[0])
            #print(y[0],g.getInDegree(y[0]))
            if g.getInDegree(y[0]) == 0:
                p.insert(1, y[0])
                #print(p.array)
    return ts




if __name__ == "__main__":
    g = XGraph()
    g.addVertex("7a")
    g.addVertex("5a")
    g.addVertex("3a")
    g.addVertex("11a")
    g.addVertex("8a")
    g.addVertex("2a")
    g.addVertex("9a")
    g.addVertex("10a")
    g.addEdge("7a","11a",0,True)
    g.addEdge("7a","8a",0,True)
    g.addEdge("5a","11a",0, True)
    g.addEdge("3a","8a",0,True)
    g.addEdge("3a","10a",0,True)
    g.addEdge("11a","2a",0,True)
    g.addEdge("11a","9a",0,True)
    g.addEdge("11a","10a",0,True)
    g.addEdge("8a","9a",0,True)
    print(Kahn(g))