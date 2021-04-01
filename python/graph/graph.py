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
                e_neighbor = neighbors.vertex
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

# Extend your graph object with a breadth-first traversal method that accepts a starting node. 
# Without utilizing any of the built-in methods available to your language, return a collection of nodes in the order they were visited. Display the collection.
    def breadth_first(self, vertex):
        nodes = []
        queue = []
        visited = []

        queue.append(vertex)
        visited.append(vertex.value)

        while len(queue) > 0:
            front = queue.pop(0)
            neighbors = self.get_neighbor(front)
            nodes.append(front.value)

            for neighbor in neighbors:
                if neighbor[0].value not in visited:
                    visited.append(neighbor[0].value)
                    queue.append(neighbor[0])
        return nodes

# can replace 'Vertex' with 'Node'
class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

if __name__ == "__main__":
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b)
    g.add_edge(b, c)
    g.add_edge(a, d)
    print(g.breadth_first(a))
