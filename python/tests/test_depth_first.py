from graph.graph import Graph, Vertex, Edge
from depth_first.depth_first import depth_first

def test_depth_first():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(a, d)
    actual = depth_first(g._adjacency_list)
    expected = ["a", "b", "c", "d"]
    assert actual == expected

def test_depth_first_2():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')
    graph.add_edge(a, b)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(c, g)
    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(d, f)
    actual = depth_first(graph._adjacency_list)
    expected = ["a", "b", "c", "g", "d", "e", "h", "f"]
    assert actual == expected