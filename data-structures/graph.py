class Vertex:
    def __init__(self, id):
        self.id = id
        self.neighbors = []

    def addNeighbors(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
    
class Graph:
    def __init__(self):
        self.vertices = {}
    
    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.id not in self.vertices:
            self.vertices[vertex.id] = vertex
            return True
        else:
            return False

    def addEdge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].addNeighbors(v2)
            self.vertices[v2].addNeighbors(v1)
            return True
        else:
            return False


    def get_vertices(self):
        return self.vertices.keys()


    def __iter__(self):
        return iter(self.vertices.values())


graph = Graph()
for i in range(4):
    graph.addVertex(Vertex(i))

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 3)
