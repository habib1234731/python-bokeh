class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, **pos):
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []
    
class Graph:
    def __init__(self):
        self.vertices = []
    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x = 40, y = 40)
        debug_vertex_2 = Vertex('t2', x = 140, y = 140)
        debug_vertex_3 = Vertex('t3', x = 300, y = 400)
        debug_vertex_4 = Vertex('t4', x = 50, y = 250)
        # print(debug_vertex_1.pos['x'])
        
        debug_edge_1 = Edge(debug_vertex_1)
        debug_vertex_1.edges.append(debug_edge_1)

        debug_edge_2 = Edge(debug_vertex_2)
        debug_vertex_3.edges.append(debug_edge_2)

        debug_edge_3 = Edge(debug_vertex_3)
        debug_vertex_4.edges.append(debug_edge_3)

        self.vertices.extend([debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4])
    def get_values(self):
        return [v.value for v in self.vertices]