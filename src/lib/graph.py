import queue

class EdgeNode(object):

    def __init__(self, end_node = None, weight = None, next = None):
        self.end_node = end_node if end_node is not None else None
        self.weight = weight if end_node is not None else None
        self.next = next if end_node is not None else None

class Graph(object):

    def __init__(self, directed = False):
        self.edges = {}
        self.degree = {}
        self.num_vertices = 0
        self.num_edges = 0
        self.directed = directed

    def insert_edge(self, start_node, end_node, weight, directed):
        if start_node not in self.edges.keys():
            self.edges[start_node] = None
            self.degree[start_node] = 0
            self.num_vertices += 1
        edgenode = EdgeNode(end_node, weight, self.edges[start_node])
        self.edges[start_node] = edgenode
        self.degree[start_node] += 1

        if not directed:
            self.insert_edge(end_node, start_node, weight, True)
        else:
            self.num_edges += 1

    def print(self):
        for vertex, edge in self.edges.items():
            output = vertex + ":"
            while (edge is not None):
                output += " " + edge.end_node
                edge = edge.next
            print(output)

    def bfs(self, initial, preprocess_vertex=None, postprocess_vertex=None, process_edge=None):
        processed = {}
        discovered = {}
        parent = {}
        for vertex in self.edges.keys():
            processed[vertex] = discovered[vertex] = False
            parent[vertex] = None

        q = queue.Queue()
        q.put(initial)
        discovered[initial] = True
        while (not q.empty()):
            vertex = q.get()
            preprocess_vertex(vertex)
            processed[vertex] = True
            edge = self.edges[vertex]
            while (edge is not None):
                end_node = edge.end_node
                if ( (not processed[end_node]) or self.directed):
                    process_edge(vertex, end_node)
                if not discovered[end_node]:
                    q.put(end_node)
                    discovered[end_node] = True
                    parent[end_node] = vertex
                edge = edge.next
            postprocess_vertex(vertex)
        return parent

    def find_path(self, start, end, parents, path=[]):
        if ((start == end) or (end is None)):
            path.append(start)
        else:
            self.find_path(start, parents[end], parents, path)
            path.append(end)
        return path


class DFS(object):

    def __init__(self, graph, preprocess_vertex=None, postprocess_vertex=None, process_edge=None):
        self.graph = graph
        self.reset(preprocess_vertex, postprocess_vertex, process_edge)

    def reset(self, preprocess_vertex, postprocess_vertex, process_edge):
        self.processed = {}
        self.discovered = {}
        self.parent = {}
        self.entry_time = {}
        self.exit_time = {}
        self.time = 0
        self.preprocess_vertex = preprocess_vertex
        self.postprocess_vertex = postprocess_vertex
        self.process_edge = process_edge
        for vertex in self.graph.edges.keys():
            self.processed[vertex] = False
            self.discovered[vertex] = False
            self.parent[vertex] = None

    def dfs(self, vertex):
        self.discovered[vertex] = True
        self.time += 1
        self.entry_time[vertex] = self.time
        self.preprocess_vertex(vertex)
        edge = self.graph.edges[vertex]
        while (edge != None):
            end_node = edge.end_node
            if not self.discovered[end_node]:
                self.parent[end_node] = vertex
                self.process_edge(vertex, end_node)
                self.dfs(end_node)
            elif ( (not self.processed[end_node]) or self.graph.directed):
                self.process_edge(vertex, end_node)
                edge = edge.next
            self.postprocess_vertex(vertex)
            self.time += 1
            self.exit_time[vertex] = self.time



test = Graph()

body = [('neck', 'head'),
 ('torso', 'neck'),
 ('torso', 'left_arm'),
 ('left_arm', 'left_wrist'),
 ('left_wrist', 'left_hand'),
 ('left_hand', 'left_finger'),
 ('torso', 'right_arm'),
 ('right_arm', 'right_wrist'),
 ('right_wrist', 'right_hand'),
 ('right_hand', 'right_finger'),
 ('torso', 'right_leg'),
 ('right_leg', 'right_foot'),
 ('right_foot', 'right_tentacle'),
 ('right_tentacle', 'head'),
 ('torso', 'left_leg'),
 ('left_leg', 'left_foot'),
 ]

for edge in body:
    test.insert_edge(edge[0], edge[1], 0, False)

test.print()
        
def preprocess(x):
    print("Preprocessing Vertex:" + str(x))

def postprocess(x):
    print("Postprocessing Vertex:" + str(x))

def process_edge(x, y):
    print("Processing Edge between:" + str(x) + " and " + str(y))

parent = test.bfs('torso', preprocess, postprocess, process_edge)
path = test.find_path('torso', 'right_tentacle', parent)
print(path)

print("DFS")
dfs = DFS(test, preprocess, postprocess, process_edge)
dfs.dfs('head')
