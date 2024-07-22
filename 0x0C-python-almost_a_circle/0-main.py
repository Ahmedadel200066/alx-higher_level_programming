import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import networkx as nx

# Initialize the directed graph
G = nx.DiGraph()

# Add nodes
nodes = [
    "Start", 
    "Define `collo`", 
    "Zip `collo` and `args`", 
    "For each `(attrr, valuee)` in `zip(collo, args)`", 
    "Set attribute `attrr` to `valuee`", 
    "For each `(atr, value)` in `kwargs.items()`", 
    "Set attribute `atr` to `value`", 
    "End"
]
for node in nodes:
    G.add_node(node)

# Add edges
edges = [
    ("Start", "Define `collo`"), 
    ("Define `collo`", "Zip `collo` and `args`"), 
    ("Zip `collo` and `args`", "For each `(attrr, valuee)` in `zip(collo, args)`"), 
    ("For each `(attrr, valuee)` in `zip(collo, args)`", "Set attribute `attrr` to `valuee`"), 
    ("Set attribute `attrr` to `valuee`", "For each `(atr, value)` in `kwargs.items()`"), 
    ("For each `(atr, value)` in `kwargs.items()`", "Set attribute `atr` to `value`"), 
    ("Set attribute `atr` to `value`", "End")
]
for edge in edges:
    G.add_edge(*edge)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=10, font_weight="bold", arrows=True, arrowstyle="->", arrowsize=10)
plt.title("Flowchart for the `update` Method")
plt.show()