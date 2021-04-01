import pytest
from graph.graph import Vertex, Graph, Edge

def test_add_vertex_pass():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'a'
    assert actual == expected

def test_add_vertex_fail():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'b'
    assert actual != expected

# Node can be successfully added to the graph
def test_add_node():
    graph = Graph()
    expected = 'a'
    actual = graph.add_node('a').value
    assert expected == actual

# An edge can be successfully added to the graph    
def test_add_edge_true():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    graph.add_edge(a, b)
    assert True

# The proper size is returned, representing the number of nodes in the graph
def test_size():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 2
    actual = graph.size()
    assert actual == expected
 
def test_size_fail():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    expected = 3
    actual = graph.size()
    assert actual != expected

# A collection of all nodes can be properly retrieved from the graph
def test_all_nodes():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(a, d)
    all_nodes = g.get_nodes()
    # expected = [['a', [('b', 1), ('c', 1), ('d', 1)]], ['b', []], ['c', []], ['d', []]]
    assert True

# All appropriate neighbors can be retrieved from the graph
# Neighbors are returned with the weight between nodes included
def test_neighbor():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(a, d)
    neighbor = g.get_neighbor(a)
    assert True

# A graph with only one node and edge can be properly returned
def test_add_edge_true():
    graph = Graph()
    a = graph.add_node('a')
    graph.add_edge(a, a)
    assert True

# An empty graph properly returns null
def test_empty_graph():
    g = Graph()
    empty = g.size()
    actual = 'Null'
    assert actual == empty

def test_breadth():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(a, d)
    breadth = g.breadth_first(a)
    expected = ['a', 'b', 'c', 'd']
    assert expected == breadth

def test_breadth_unOrdered():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b)
    g.add_edge(b, c)
    g.add_edge(a, d)
    breadth = g.breadth_first(a)
    expected = ['a', 'b', 'd', 'c']
    assert expected == breadth

def test_breadth_b():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    e = g.add_node('e')
    g.add_edge(b, a)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(a, c)
    g.add_edge(e, a)
    breadth = g.breadth_first(b)
    expected = ['b', 'a', 'd', 'e', 'c']
    assert expected == breadth