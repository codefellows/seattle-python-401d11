class Graph:
    
    def __init__(self):
        self._table = {}


    def add_vertex(self, value):

        vertex = Vertex(value)

        # add to "the graph" ????
        self._table[value] = []

        # return vertex

        return vertex

    
    def size(self):
        pass

class Vertex:
    """
    Thanks Chris
    """

    def __init__(self, value):
        self.value = value

    # do repr and string

    


    