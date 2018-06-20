import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
print(graph_data.vertices)

N = 9
node_indices = list(range(N))

# debug_pallete = Spectral8
# debug_pallete.append('#ff0000')
# debug_pallete.append('#0000ff')

color_list = []
for vertex in graph_data.vertices:
    color_list.append(vertex.color)

plot = figure(title='Graph Layout Demonstration', x_range=(-500,500), y_range=(-500,500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
#changed debug_palette to color_list
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=20, width=40, fill_color='color')

### this is drawing the edges from start to end

graph.edge_renderer.data_source.data = dict(
    start=[0]*N, #this is why all the edges start from the first vertex
                #and is a list of some kind that has to do with starting points
    end=node_indices) #this is a list of some kind that has to do with ending points

### start of layout code
### This is setting the positions of the vertices
# circ = [i*2*math.pi/8 for i in node_indices]
# x = [math.cos(i) for i in circ] or [... for v in graph.vertices]
# y = [math.sin(i) for i in circ]
x = [v.pos['x'] for v in graph_data.vertices]
y = [v.pos['y'] for v in graph_data.vertices]

print('x is ',x)
print('y is ',y)

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)