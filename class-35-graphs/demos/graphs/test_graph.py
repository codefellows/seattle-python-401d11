from .graph import Graph

def test_class():
    assert Graph

def test_instance():
    assert Graph()

def test_add_vertex_once():
    g = Graph()
    vertex = g.add_vertex('apple')
    assert vertex.value is 'apple'
    assert 'apple' in g._table

def test_add_vertex_twice():
    g = Graph()
    g.add_vertex('apple')
    g.add_vertex('banana')
    assert 'apple' in g._table
    assert 'banana' in g._table


def test_add_edge():
    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    g.add_edge(apple, banana, 4)

    assert g._table['apple'] == ???
    assert g._table['banana'] == ???

def test_get_vertices():

    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    vertices = g.get_vertices()

    assert vertices == ???

def test_get_neighbors():

    g = Graph()
    apple = g.add_vertex('apple')
    banana = g.add_vertex('banana')

    neighbors = g.get_neighbor(apple)

    assert neighbors == ??? # check for weight!

def test_size():
    pass








