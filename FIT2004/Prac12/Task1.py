__author__ = 'HaoBin'

import cProfile
from XGraph2 import XGraph
from XMinHeap import MinHeapPQ
from XSet import XSet


#################################################
# TASK 1 burrow
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


########################################################
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

    while pq.empty() is False:
        x = pq.pop()[1].split(":")
        if s.findSet(x[0]) != s.findSet(x[1]):
            s.union(x[0],x[1])
            mst.append(x)
    sets = s.getSets()

    return len(sets), sets, mst, s

############################################################
# TASK 3

def floyd_warshall(g):
    n = len(g)
    v = g.getVerticesList()
    dist = [[None for i in range(n)] for j in range(n)]
    #print(dist)
    print("Initialising Floyd-Warshall...", end="\r")
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            else:
                edge = g.getEdge(v[i],v[j])
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
                        dist[j][i] = dist[i][j]
        print("Calculating distances... " + v[k] + " " + str(k) + "/" + str(n), end="\r")
    print("Floyd-Warshall done.", end="\r")

    # for x in dist:
    #     print(x)

    return dist



def diameter_warshall(g, warshall_dist):
    max = (None, -1)
    n = len(g)
    ves = g.getVerticesList()
    for v in range(n):
        for e in range(n):
            test = warshall_dist[v][e]
            if test != float("inf") and test > max[1]:
                edge = [ves[v],ves[e]]
                max = (edge, test)
    return max


#### MAIN ############################################

def t3_main(g, s):
    dist = floyd_warshall(g)
    maxima = diameter_warshall(g, dist)
    print("Partition with largest diameter:", s.findSet(maxima[0][0]))
    print("Longest path: ", maxima)

def t2_main(g):
    num_cc, partitions, mst, set = kruskal(g)
    print("Number of Connected Components:",num_cc)
    print("Partitions:")
    for x in partitions:
        print(x[0])
    opt = str(input("Get partition? y/n: "))
    if opt == "Y":
        param = str(input("part: "))
        for item in partitions:
            if item[0] == param:
                print(item[1])
                break
    return partitions, set

def t1_main(g):
    while True:
        u = str(input("Origin (type exit to stop): "))
        if u == "exit":
            break
        v = str(input("Target: "))
        dist, path = dijkstra(g,u,v)
        print(dist, path_visualiser(path,u,v))
        print()


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

    #g.toStrConnection()
    partitions = []
    set_s = None

    while True:
        print("\nTask 1, enter:")
        print("1 - Shortest distance between words")
        print("2 - Number of Connected Components and Partitions")
        print("3 - Partition with the largest diameter")
        print("0 - Exit")
        param = int(input("Select task: "))

        if param == 1:
            try:
                t1_main(g)
            except KeyError:
                print("Not exist or not connected")
        elif param == 2:
            partitions, set_s = t2_main(g)
        elif param == 3:
            if partitions == [] or set_s is None:
                partitions, set_s = t2_main(g)
            t3_main(g, set_s)
        else:
            print("Invalid input")


if __name__ == "__main__":
    #cProfile.run("main()")
    main()