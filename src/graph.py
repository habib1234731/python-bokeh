import random

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
        debug_vertex_2.edges.append(debug_edge_1)

        debug_edge_2 = Edge(debug_vertex_2)
        debug_vertex_3.edges.append(debug_edge_2)

        debug_edge_3 = Edge(debug_vertex_3)
        debug_vertex_4.edges.append(debug_edge_3)

        self.vertices.extend([debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4])

    def randomize(self,width, height, px_box, probability):
        def connect_vertices(v0, v1):
            v0.edges.append(Edge(v1))
            v1.edges.append(Edge(v0))

        count = 0
        
        # Build a grid of vertices

        grid = []
        for y in range(height):
            row = []
            for x in range(width):
                vert = Vertex('t + {count+1}')
                count += 1
                row.append(vert)
            grid.append(row)
        
        #Go through the grid randomly hooking up edges
        for y in range(height):
            for x in range(width):
                #connect down
                if (y < height - 1):
                    if (random.random() < probability):
                        connect_vertices(grid[y][x], grid[y+1][x])
                if (x < width - 1):
                    if (random.random() < probability):
                        connect_vertices(grid[y][x], grid[y][x+1])
        box_buffer = 0.8
        box_inner = px_box * box_buffer
        box_inner_offset = (px_box - box_inner) / 2

        for y in range(height):
            for x in range(width):
                grid[y][x].pos = {
                'x': (x * px_box + box_inner_offset + random.random() * box_inner),
                'y': (y * px_box + box_inner_offset + random.random() * box_inner)
                }
        
        # Finally, add everything in our grid to the vertexes in this Graph
        for y in range(height):
            for x in range(width):
                self.vertices.append(grid[y][x])

    def get_values(self):
        return [v.value for v in self.vertices]
    def bfs(self, start):
        print('called BFS')
        random_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        queue = []
        found = []

        queue.append(start)
        found.append(start)

        start.color = random_color

        while (len(queue) > 0):
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
            queue.pop(0) #TODO: Look into collections.dequeue
        print('found', found, ' completed and exiting from BFS')
        