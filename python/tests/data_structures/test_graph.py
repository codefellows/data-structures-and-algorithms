import pytest
from data_structures.graph import Graph, Vertex


def test_exists():
    assert Graph


@pytest.mark.skip("TODO")
def test_add_node():

    graph = Graph()

    expected = "spam"  # a vertex's value that comes back

    actual = graph.add_node("spam").value

    assert actual == expected


@pytest.mark.skip("TODO")
def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


@pytest.mark.skip("TODO")
def test_size():

    graph = Graph()

    graph.add_node("spam")

    expected = 1

    actual = graph.size()

    assert actual == expected


@pytest.mark.skip("TODO")
def test_add_edge():
    g = Graph()
    apple = g.add_node("apple")
    banana = g.add_node("banana")
    g.add_edge(apple, banana, 5)
    neighbors = g.get_neighbors(apple)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "banana"
    assert neighbors[0].weight == 5


@pytest.mark.skip("TODO")
def test_bouquet():
    g = Graph()
    apple = g.add_node("apple")
    g.add_edge(apple, apple, 10)
    neighbors = g.get_neighbors(apple)
    assert len(neighbors) == 1
    assert neighbors[0].vertex.value == "apple"
    assert neighbors[0].weight == 10


@pytest.mark.skip("TODO")
def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex("start")

    end = graph.add_node("end")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


@pytest.mark.skip("TODO")
def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex("end")

    start = graph.add_node("start")

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


@pytest.mark.skip("TODO")
def test_get_nodes():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    loner = Vertex("loner")

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


@pytest.mark.skip("TODO")
def test_get_neighbors():

    graph = Graph()

    banana = graph.add_node("banana")

    apple = graph.add_node("apple")

    graph.add_edge(apple, banana, 44)

    neighbors = graph.get_neighbors(apple)

    assert len(neighbors) == 1

    neighbor_edge = neighbors[0]

    assert neighbor_edge.vertex.value == "banana"

    assert neighbor_edge.weight == 44
