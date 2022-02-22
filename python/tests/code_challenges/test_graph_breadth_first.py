import pytest
from data_structures.graph import Graph


def test_exists():
    assert Graph

@pytest.mark.skip("TODO")
def test_bfs(graph):
    actual = graph.breadth_first(graph.get_nodes[0])
    expected = ["a","b","c","d","e","f","g","h","i","j"]
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
    i = letters.add_node("i")
    j = letters.add_node("j")

    letters.add_edge(a, b)
    letters.add_edge(a, c)
    letters.add_edge(a, e)

    letters.add_edge(b, a)
    letters.add_edge(b, d)

    letters.add_edge(c, a)
    letters.add_edge(c, f)

    letters.add_edge(d, b)
    letters.add_edge(d, e)


    letters.add_edge(e, a)
    letters.add_edge(e, d)
    letters.add_edge(e, f)
    letters.add_edge(e, g)

    letters.add_edge(f, c)
    letters.add_edge(f, g)
    letters.add_edge(f, h)

    letters.add_edge(g, e)
    letters.add_edge(g, h)

    letters.add_edge(h, f)
    letters.add_edge(h, g)
    letters.add_edge(h, j)

    letters.add_edge(i, f)
    letters.add_edge(i, j)

    letters.add_edge(j, h)
    letters.add_edge(j, i)

    return letters
