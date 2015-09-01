__author__ = 'HaoBin'

from XGraph2 import *
import copy, cProfile

def generate(m,n):
    # recursively generates a list of values according to m, n parameter
    # where m is the size of the alphabet set
    # and n is the length of each string
    # Complexity: O(M^N)
    dict = []
    for i in range(m):
        dict.append(chr(65+i))

    total_set = generate_recursive(n, dict,[],"")
    return total_set

def generate_recursive(n, dict, total, current):
    if len(current) == n:
        total.append(current)
    else:
        for c in dict:
            current += c
            total = generate_recursive(n, dict, total, current)
            current = current[0:len(current)-1]
    return total

def check_graph(graph):
    # does a simple graph check to determine if Euler Circuit exist
    # works for Task 1 only I suppose
    # condition: All vertices has equal in and out degree
    # Complexity: worst case O(|V|^2)
    vs = graph.getVerticesList()
    cycle = True
    for v in vs:
        if graph.getInDegree(v) != graph.getDegree(v):
            cycle = False
            break
    return cycle

def e_graph_build(graph):
    # Complexity: O(|E| * |V| * Worst length of outgoing)
    e_path_exists = check_graph(graph)
    print("Checking graph... E-path exists?", e_path_exists)
    e_graph = []
    if e_path_exists:
        vs = graph.getVerticesList()
        # get arbitrary vertex to start, but we simply choose the first in vertex list
        u = vs[0]
        e_graph.append(u)
        while graph.getEdgeCount() > 0:
            # O(|E|)
            if graph.getDegree(u) == 0 and graph.getEdgeCount() > 0:
                print("No E-path found!")
                break
            elif graph.getDegree(u) == 0 and graph.getEdgeCount() == 0:
                print("E-path found!")
                break
            elif graph.getDegree(u) == 1:
                v = graph.getConnections(u)[0][0]
                e_graph.append(v)
                graph.deleteEdge(u,v)
                u = v
            elif graph.getDegree(u) >= 2:

                # go through self loops
                for connection in graph.getConnections(u):
                    if connection[0] == u:
                        graph.deleteEdge(u,connection[0])
                        e_graph.append(connection[0])
                u_outgoing = graph.getConnections(u)
                continuex = True

                i = 0
                while continuex and i < len(u_outgoing):
                    # O( Number of outdegree)
                    v = u_outgoing[i][0]

                    ori_edge_cost, ori_edge_direct = graph.getEdge(u, v).getCost(), graph.getEdge(u, v).isDirected()

                    # tries to traverse/delete the edge, and check for validity
                    # ** does DFS to check if the edge is a bridge
                    # DFS is O(|V|)
                    init_c = dfs(copy.deepcopy(graph),u)
                    graph.deleteEdge(u, v)
                    continuex = False
                    after_c = dfs(copy.deepcopy(graph),v)


                    # getInDegree is O(|V|)
                    if graph.getInDegree(v) == 0 and graph.getDegree(v) == 0:
                        graph.addEdge(u, v, ori_edge_cost, ori_edge_direct)
                        continuex = True

                    else:
                        if init_c > after_c:
                            # Bridge detected
                            graph.addEdge(u, v, ori_edge_cost, ori_edge_direct)
                            continuex = True
                        else:

                            e_graph.append(v)
                            u = v
                            u_outgoing = graph.getConnections(u)
                    i += 1
            print(len(e_graph),end="\r")
        return e_graph
    else:
        return []

def dfs(graph, u):
    # performs a depth first search and return the number of nodes traversable
    # * count reachable node from u *
    # Complexity: O(|V|) worst case, traverse all nodes reachable
    count = 0
    connections = graph.getConnections(u)
    graph.deleteVertex(u)
    count += dfs_helper(graph, connections,u) + 1
    return count

def dfs_helper(graph, connections, u):
    # helper recursive part for dfs()
    count = 0

    for v in connections:
        if v[0] != u and graph[v[0]] is not None:
            v_connection = graph.getConnections(v[0])
            graph.deleteVertex(v[0])
            count += dfs_helper(graph,v_connection,v[0]) + 1
    return count


def rbk(pat,txt):
    n = len(txt)
    m = len(pat)
    h_pat = rolling_hash(pat)
    h_txt = rolling_hash(txt[0:m])

    for i in range(n-m+1):
        if h_pat == h_txt:

            for j in range(m):
                match = True
                if txt[i+j] != pat[j]:
                    match = False
                if match is True:
                    return i
        h_txt = update_rolling_hash(h_txt, txt[i:i+m+1])
    return -1

def rolling_hash(string,d=131):
    q = 32452843
    hash = ord(string[0]) * d + ord(string[1])
    for i in range(2,len(string)):
        hash = hash * d + ord(string[i])
    return hash % q

def update_rolling_hash(hash,txt,d=131):
    q = 32452843
    h = (hash - (ord(txt[0]) * (d**(len(txt)-2))) ) * d + ord(txt[len(txt)-1])
    return h % q


def d_edges_build(graph,n):
    # Complexity: O(|V|^2)
    # build the D-graph and edges
    vertices = graph.getVertices()
    for vertex in vertices:
        for target in vertices:
            vid = vertex[1].getID()
            tid = target[1].getID()
            # PENDING COMPLETION: STRING MATCHING #
            if rbk(vid[1:n], tid) == 0:
            #if vid[1:n] == tid[0:n-1]:
                graph.addEdge(vid,tid,0,True)
    return graph


def d_edges_build_2(graph,n):
    # Complexity: O(|V| * c)
    hash_head = XHashTable()
    hash_tail = XHashTable()

    vertices = graph.getVerticesList()

    for v in vertices:
        h = hash_head[v[0:n-1]]
        t = hash_tail[v[1:n]]
        if h is None:
            hash_head[v[0:n-1]] = [v]
        if t is None:
            hash_tail[v[1:n]] = [v]
        if h is not None:
            hash_head[v[0:n-1]] = h + [v]
        if t is not None:
            hash_tail[v[1:n]] = t + [v]

    for v in vertices:
        h_v = hash_head[v[1:n]]
        for h in h_v:
            if graph.getEdge(v,h) is None:
                graph.addEdge(v,h,0,True)
        t_v = hash_tail[v[0:n-1]]
        for t in t_v:
            if graph.getEdge(t,v) is None:
                graph.addEdge(t,v,0,True)

    return graph


def print_extend(graph):
    # Complexity O(|E|)
    # prints out the final E-path
    if len(graph) > 0:
        n = len(graph[0])
        print(graph[0], end="")
        i = 1
        while i < len(graph):
            print(graph[i][n-1:], end="")
            i += 1
        print()

def main():
    # initialise the string set using m & n
    m = 3
    n = 2
    total_set = generate(m,n)

    # starts to build D-graph and edges
    d_graph = XGraph()
    for s in total_set:
        d_graph.addVertex(s)
    #graph = d_edges_build(d_graph,n)
    graph = d_edges_build_2(d_graph,n)
    graph.toStrConnection()
    print("Edge Count:", graph.getEdgeCount())

    # build the E-graph
    e_graph = e_graph_build(graph)
    print("E",e_graph)
    print("E-path length:",len(e_graph)-1)
    print_extend(e_graph)
    print()

if __name__ == "__main__":
    cProfile.run('main()')
    #print(rbk("AA","AAB"))