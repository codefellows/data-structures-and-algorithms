import pytest
from data_structures.graph import Graph, Vertex


@pytest.mark.skip("TODO")
def test_full(graph_and_root):
    graph, root = graph_and_root
    actual = graph.depth_first_search(root)

    expected = ["a", "b", "c", "g", "d", "e", "h", "f"]
    assert actual == expected


@pytest.mark.skip("TODO")
def test_empty():
    graph = Graph()
    node = Vertex("some other node")
    actual = graph.depth_first_search(node)
    expected = []
    assert actual == expected


@pytest.mark.skip("TODO")
def test_island_empty():
    graph = Graph()
    lonely = graph.add_node("lonely")
    actual = graph.depth_first_search(lonely)
    expected = ["lonely"]
    assert actual == expected


@pytest.mark.skip("TODO")
def test_island_crowded(graph):
    lonely = graph.add_node("lonely")
    actual = graph.depth_first_search(lonely)
    expected = ["lonely"]
    assert actual == expected


@pytest.mark.skip("TODO")
def test_mates_crowded(graph):
    lady = graph.add_node("lady")
    the_tramp = graph.add_node("the tramp")
    graph.add_edge(lady, the_tramp, 10)
    graph.add_edge(the_tramp, lady, 10)
    actual = graph.depth_first_search(lady)
    expected = ["lady", "the tramp"]
    assert actual == expected


@pytest.fixture
def graph():

    letters = Graph()

    a = letters.add_node("a")
    b = letters.add_node("b")
    c = letters.add_node("c")
    d = letters.add_node("d")
    e = letters.add_node("e")
    f = letters.add_node("f")
    g = letters.add_node("g")
    h = letters.add_node("h")

    letters.add_edge(a, b)
    letters.add_edge(b, c)
    letters.add_edge(c, g)
    letters.add_edge(a, d)

    letters.add_edge(d, e)
    letters.add_edge(d, h)
    letters.add_edge(d, f)

    letters.add_edge(h, f)

    return letters


@pytest.fixture
def graph_and_root(graph):
    return graph, graph.get_nodes()[0]
