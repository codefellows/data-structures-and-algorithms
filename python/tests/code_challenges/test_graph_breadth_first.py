import pytest
from data_structures.graph import Graph


def test_exists():
    assert Graph

@pytest.mark.skip("TODO")
def test_bfs(graph):
    pass



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
