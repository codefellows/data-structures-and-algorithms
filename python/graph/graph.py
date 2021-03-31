class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):
        v = Vertex(value)
        self._adjacency_list[v] = []
        return v

    def add_edge(self, start_vert, end_vert, weight=1):
        # make sure both verts are already in the list
        if start_vert not in self._adjacency_list:
            raise KeyError('Start Vert not in graph!')
        if end_vert not in self._adjacency_list:
            raise KeyError('End Vert not in graph!')
        # store the edge then append it to adj_list at the start vert location.
        e = Edge(end_vert, weight)
        adj = self._adjacency_list[start_vert] 
        adj.append(e)

    def get_nodes(self):
        if len(self._adjacency_list) > 0:
            node = []
            for each in self._adjacency_list:
                neighbor = self.get_neighbor(each)
                to_append = [each.value, neighbor]
                node.append(to_append)
            return node


    def get_neighbor(self, value):
        home = self._adjacency_list[value]
        neighbor = []
        if len(home) > 0:
            for neighbors in home:
                e_neighbor = neighbors.vertex.value
                neighbor_weight = neighbors.weight
                both = e_neighbor, neighbor_weight
                neighbor.append(both)
        return neighbor
            

    def size(self):
        count = 0
        for each in self._adjacency_list:
            count += 1
        if count == 0:
            return 'Null'
        return count


# can replace 'Vertex' with 'Node'
class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight