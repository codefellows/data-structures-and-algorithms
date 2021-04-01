from graph.graph import Vertex, Graph, Edge
from get_edge.get_edge import get_edge

def test_get_edge():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(a, d)
    names = ['a', 'c', 'b']
    edges = get_edge(g, names)
    actual = True, 3 
    assert actual == edges

def test_get_edge_2():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b, 4)
    g.add_edge(a, c, 23)
    g.add_edge(a, d, 19)
    names = ['a', 'c', 'b']
    edges = get_edge(g, names)
    actual = True, 27
    assert actual == edges
