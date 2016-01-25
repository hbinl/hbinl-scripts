__author__ = 'HaoBin'

from Task1 import *

# TEST CASES
def test():
    g = XGraph()
    g.addVertex("s")
    g.addVertex("u")
    g.addVertex("t")
    g.addVertex("v")
    g.addVertex("w")

    g.addEdge("s","t",10,True)
    g.addEdge("s","u",5,True)
    g.addEdge("u","t",3,True)
    g.addEdge("u","w",2,True)
    g.addEdge("u","v",9,True)
    g.addEdge("t","u",2,True)
    g.addEdge("t","v",1,True)
    g.addEdge("w","s",7,True)
    g.addEdge("w","v",6,True)
    g.addEdge("v","w",4,True)

    h = XGraph()
    h.addVertex("S")
    h.addVertex("A")
    h.addVertex("B")
    h.addVertex("C")
    h.addVertex("D")
    h.addVertex("G")
    h.addEdge("S","A",1)
    h.addEdge("S","G",12)
    h.addEdge("A","B",3)
    h.addEdge("A","C",1)
    h.addEdge("B","D",3)
    h.addEdge("C","D",1)
    h.addEdge("C","G",2)
    h.addEdge("D","G",3)

    cost, path = dijkstra(g,"s","w")
    print(path)
    print(cost, path_visualiser(path, "s", "w"))



    cost, path = dijkstra(h,"G","S")
    print(path)
    print(cost, path_visualiser(path, "G", "S"))

    a = XGraph()
    a.addVertex("A")
    a.addVertex("D")
    a.addVertex("B")
    a.addVertex("E")
    a.addVertex("C")
    a.addVertex("F")
    a.addEdge("A","B",1)
    a.addEdge("A","D",4)
    a.addEdge("A","E",3)
    a.addEdge("D","B",4)
    a.addEdge("D","E",4)
    a.addEdge("B","E",2)
    a.addEdge("E","C",4)
    a.addEdge("E","F",7)
    a.addEdge("F","C",5)

    a = XGraph()
    a.addVertex("A")
    a.addVertex("D")
    a.addVertex("B")
    a.addVertex("E")
    a.addVertex("C")
    a.addVertex("F")
    a.addEdge("A","B",1)
    a.addEdge("B","E",2)

    a.addEdge("E","C",4)
    a.addEdge("C","F",5)

    num_cc, partitions, mst, set_s = kruskal(a)
    print(num_cc, partitions, mst)

    t3_main(a,set_s)

if __name__ == "__main__":
    test()
