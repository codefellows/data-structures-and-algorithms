from graph.graph import Vertex, Graph, Edge
from get_edge.get_edge import get_edge2

# def test_get_edge():
#     g = Graph()
#     a = g.add_node('a')
#     b = g.add_node('b')
#     c = g.add_node('c')
#     d = g.add_node('d')
#     g.add_edge(a, b)
#     g.add_edge(a, c)
#     g.add_edge(a, d)
#     names = ['a', 'c', 'b']
#     edges = get_edge(g, names)
#     actual = True, 3 
#     assert actual == edges

def test_get_edge_2():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b, 1)
    g.add_edge(a, c, 1)
    g.add_edge(c, b, 2)
    g.add_edge(c, a, 2)
    g.add_edge(a, d, 19)
    names = [a, c]
    edges = get_edge2(g, names)
    actual = (True, 3)
    assert actual == edges

def test_get_edge_2_more():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b, 1)
    g.add_edge(a, c, 1)
    g.add_edge(a, d, 1)
    g.add_edge(c, a, 2)
    g.add_edge(c, b, 2)
    g.add_edge(d, c, 19)
    g.add_edge(d, a, 19)
    names = [a, c, d]
    edges = get_edge2(g, names)
    actual = (True, 22)

def test_get_edge_2_cant_travel():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b, 1)
    # g.add_edge(a, c, 1)
    g.add_edge(a, d, 1)
    # g.add_edge(c, a, 2)
    g.add_edge(c, b, 2)
    # g.add_edge(c, d, 19)
    g.add_edge(d, b, 10)
    names = [a, c, d]
    edges = get_edge2(g, names)
    actual = (False, 0)