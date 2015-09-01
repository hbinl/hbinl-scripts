__author__ = 'HaoBin'

from XGraph2 import *
import copy, cProfile


def check_graph(graph):
    # this method checks the graph for Eulerian Trail validity
    # which is: max 1 vertex with inD-outD=1 and max 1 vertex with outD-inD=1,
    # and all other vertices must have equal inD and outD
    # O(|V|^2) complexity

    vs = graph.getVerticesList()

    # initialising validity
    valid = True
    in_out_delta = 0
    out_in_delta = 0

    for v in vs:
        in_d = graph.getInDegree(v)
        out_d = graph.getDegree(v)
        if in_d != out_d:
            valid = False
            if in_d - out_d == 1:
                in_out_delta += 1
            if out_d - in_d == 1:
                out_in_delta += 1
            if in_out_delta <= 1 and out_in_delta <= 1:
                # if still within valid bounds, valid again
                valid = True

    if in_out_delta > 1 or out_in_delta > 1:
        valid = False
    return valid

def e_graph_build(graph):
    #e_path_exists = check_graph(graph)
    #print("Checking graph... E-path exists?", e_path_exists)
    e_graph = []
    e_path_exists = True
    if e_path_exists:
        vs = graph.getVerticesList()
        u = vs[0]
        # Start from the vertex with 0 in-degree
        for v in vs:
            if graph.getInDegree(v) == 0:
                u = v
        e_graph.append(u)

        while graph.getEdgeCount() > 0:
            # while there are still unvisited edges
            if graph.getDegree(u) == 0 and graph.getEdgeCount() > 0:
                print("No E-path found!")
                break
            elif graph.getDegree(u) == 0 and graph.getEdgeCount() == 0:
                print("E-path found!")
                break
            elif graph.getDegree(u) == 1:
                # left 1 out-degree
                v = graph.getConnections(u)[0][0]
                e_graph.append(v)
                graph.deleteEdge(u,v)
                u = v
            elif graph.getDegree(u) >= 2:
                #print("c4")
                # if the vertex u has 2 or more out-degree

                # go through self loops first
                for connection in graph.getConnections(u):
                    if connection[0] == u:
                        graph.deleteEdge(u,connection[0])
                        e_graph.append(connection[0])

                u_outgoing = graph.getConnections(u)
                #print(u_outgoing)
                continuex = True
                i = 0
                # check each outgoing paths
                while continuex and i < len(u_outgoing):
                    #print(i)
                    v = u_outgoing[i][0]
                    ori_edge_cost, ori_edge_direct = graph.getEdge(u, v).getCost(), graph.getEdge(u, v).isDirected()

                    # tries to traverse/delete the edge, and check for validity
                    # ** does DFS to check if the edge is a bridge
                    init_c = dfs(copy.deepcopy(graph),u)
                    graph.deleteEdge(u, v)
                    continuex = False
                    after_c = dfs(copy.deepcopy(graph),v)

                    # now check if doing this edge will leave it disconnected
                    if graph.getInDegree(v) == 0 and graph.getDegree(v) == 0:
                        graph.addEdge(u, v, ori_edge_cost, ori_edge_direct)
                        continuex = True
                    else:
                        if init_c > after_c:
                            # Bridge detected
                            graph.addEdge(u, v, ori_edge_cost, ori_edge_direct)
                            continuex = True
                        else:
                            # valid next-edge, proceed to next loop
                            e_graph.append(v)
                            u = v
                            u_outgoing = graph.getConnections(u)
                    i += 1
                    if i >= len(u_outgoing):
                        print("No E-path found! No valid next vertex found.")
                        return e_graph
            print(len(e_graph),end="\r")
        return e_graph
    else:
        return []




def dfs(graph, u):
    # O(|V|)
    # performs a depth first search and return the number of nodes traversable
    # * count reachable node from u *
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
    # Complexity: O(|V|)
    # build the D-graph and edges
    vertices = graph.getVertices()

    for vertex in vertices:
        for target in vertices:
            vid = vertex[1].getID()
            tid = target[1].getID()
            # PENDING COMPLETION: STRING MATCHING #
            if rbk(vid[1:n], tid) == 0:
            #if vid[1:n] == tid[0:n-2]:
                graph.addEdge(vid,tid,0,True)
    return graph

def d_edges_build_2(graph,n):
    hash_head = XHashTable()
    hash_tail = XHashTable()

    vertices = graph.getVerticesList()

    for v in vertices:
        h = hash_head[v[0:n-2]]
        t = hash_tail[v[1:n]]
        if h is None:
            hash_head[v[0:n-2]] = [v]
        if t is None:
            hash_tail[v[1:n]] = [v]
        if h is not None:
            hash_head[v[0:n-2]] = h + [v]
        if t is not None:
            hash_tail[v[1:n]] = t + [v]

    for v in vertices:
        h_v = hash_head[v[1:n]]
        if h_v is not None:
            for h in h_v:
                if graph.getEdge(v,h) is None:
                    graph.addEdge(v,h,0,True)
        t_v = hash_tail[v[0:n-1]]
        if t_v is not None:
            for t in t_v:
                if graph.getEdge(t,v) is None:
                    graph.addEdge(t,v,0,True)

    return graph

def print_extend(graph):
    # Complexity: O(|E|)
    # printing out the final E-path
    if len(graph) > 0:
        n = len(graph[0])
        print(graph[0], end="")
        i = 1
        while i < len(graph):
            print(graph[i][n-1:], end="")
            i += 1
        print()

def main():
    # Load the file
    total_set = []
    n = 0
    file = open("substrings.txt",'r')
    for line in file:
        total_set.append(line.strip())
        if n == 0:
            n = len(line)

    # initialise D-graph and build the edges
    d_graph = XGraph()
    for s in total_set:
        d_graph.addVertex(s)

    graph = d_edges_build_2(d_graph,n)
    print("Edge Count:", graph.getEdgeCount())

    # build the E-graph
    e_graph = e_graph_build(graph)
    print("E",e_graph)
    print("E-path length:",len(e_graph)-1)
    print_extend(e_graph)
    print()

if __name__ == "__main__":
    cProfile.run('main()')

