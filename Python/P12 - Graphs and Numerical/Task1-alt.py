__author__ = 'HaoBin'

import cProfile
from XGraph2 import XGraph
from XMinHeap import MinHeapPQ
from XSet import XSet

# TASK 1
def dijkstra(g, u, t):
    dist = {}
    predecessor = {}
    removed = []
    remaining = MinHeapPQ()

    dist[u] = 0
    for v in g.getVerticesList():
        if v != u:
            dist[v] = float("inf")
            predecessor[v] = None
        remaining.insert(dist[v], v)

    while remaining.empty() is False:
        x = remaining.pop()
        removed.append(x)
        if dist[x[1]] == float("inf"):
            break
        for y in g.getConnections(x[1]):
            est = dist[x[1]] + g.getEdge(x[1],y[0]).getCost()
            if est < dist[y[0]]:
                dist[y[0]] = est
                predecessor[y[0]] = x
                remaining.decrease_key(y[0], est)

    return dist[t], predecessor


def path_visualiser(path, u, v):
    node = path[v]
    path_v = [v]
    if node is not None:
        while node[1] != u:
            path_v.append(node[1])
            node = path[node[1]]
    path_v.append(u)
    return path_v[::-1]

# TASK 2
def kruskal(g):
    mst = []
    s = XSet()
    for v in g.getVerticesList():
        s.makeSet(v)

    pq = MinHeapPQ()
    for e in g.getEdgesList():
        key = e[0] + ":" + e[1]
        pq.insert(g.getEdge(e[0],e[1]).getCost(),key)
    #print(pq.array)

    while pq.empty() is False:
        x = pq.pop()[1].split(":")
        if s.findSet(x[0]) != s.findSet(x[1]):
            s.union(x[0],x[1])
            mst.append(x)

    sets = s.getSets()
    #print(s.getPartition("A"))

    return len(sets), sets, mst, s

############################################################
# TASK 3

def floyd_warshall_partition(partition_v, g):
    n = len(partition_v)
    dist = [[None for i in range(n)] for j in range(n)]
    #print(dist)
    print("Initialising Floyd-Warshall...", end="\r")
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            else:
                edge = g.getEdge(partition_v[i],partition_v[j])
                if edge is not None:
                    dist[i][j] = edge.getCost()
                else:
                    dist[i][j] = float("inf")

    print("Calculating distances...", end="\r")
    for k in range(n):
        for i in range(n):
        	if k != i:
	            for j in range(i+1):
	                if dist[i][j] > dist[i][k] + dist[k][j]:
	                    dist[i][j] = dist[i][k] + dist[k][j]
        print("Calculating distances... " + partition_v[k] , end="\r")
    print("Floyd-Warshall done.", end="\r")

    return dist

def diameter_warshall(g, partition_v, warshall_dist):
    max = (None, -1)
    n = len(partition_v)
    for v in range(n):
        for e in range(n):
            test = warshall_dist[v][e]
            if test != float("inf") and test > max[1]:
                edge = [partition_v[v],partition_v[e]]
                max = (edge, test)
    #print(max)

    return max


#### MAIN ############################################

def t3_main(g, s):
    partitions = s.getSets()
    maxima = (None, -1)
    for p in partitions:
        print("Current:", p[0], " - Calculating diameters using Floyd-Warshall...")
        warshall_dist = floyd_warshall_partition(p[1],g)
        print("Computing diameter... ", end="")
        diameter = diameter_warshall(g, p[1], warshall_dist)
        print(diameter[1])
        if diameter[1] > maxima[1]:
            maxima = diameter

    print("Partition with largest diamter:", s.findSet(maxima[0][0]))


def t2_main(g):
    num_cc, partitions, mst, set = kruskal(g)
    print("Number of Connected Components:",num_cc)
    print("Partitions:")
    for x in partitions:
        print(x[0])
    #print(partitions)
    opt = str(input("Get partition? y/n: "))
    if opt == "Y":
        param = str(input("part: "))
        for item in partitions:
            if item[0] == param:
                print(item[1])
                break
    else:
        pass

    return partitions, set



def main():
    g = XGraph()
    print("Reading file...")
    file = open("words5letter.txt", 'r')
    for line in file:
        g.addVertex(line.rstrip())

    print("Building edges...")
    for v in g.getVerticesList():
        for u in g.getVerticesList():
            hd = 0
            for i in range(len(u)):
                if v[i] != u[i]:
                    hd += 1
                if hd > 1:
                    break
            if hd == 1 and g.connectedTo(v,u) is False:
                g.addEdge(v,u)

    g.toStrConnection()

    partitions = []

    while True:
        print("Task 1, enter:")
        print("1 - Shortest distance between words")
        print("2 - Number of Components and Partitions")
        print("3 - Partition with the largest diameter")
        param = int(input("Select task: "))

        if param == 1:
            u = str(input("Origin (type exit to stop): "))
            if v == "exit":
                break
            v = str(input("Target: "))
            dist, path = dijkstra(g,u,v)
            print(dist, path_visualiser(path,u,v))
            print()
        elif param == 2:
            partitions, set_s = t2_main(g)
        elif param == 3:
            if partitions != []:
                t3_main(g, set_s)
            else:
                print("Please run 2 before you run 3.")
        else:
            print("Invalid input")



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
    #cProfile.run("main()")
    #test()
    main()