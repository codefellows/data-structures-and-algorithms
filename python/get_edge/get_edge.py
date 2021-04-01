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

################################################################################

# def get_edge(graph, names):
#     actual_nodes = graph.get_nodes()
#     print(actual_nodes)
#     weight = 0
#     can_travel = False
#     for name in names:
#         for nodes in actual_nodes:
#             print('nodes[0]', nodes[1][1])
#             if name in nodes[0]:
#                 for node in nodes:
#                     for each in node:
#                         print('each is:', each)
#                         # weight += each[1]
#                     print('node is', node[0])
#                     # weight += node
#                 # weight += nodes[1][1]
#                 can_travel = True
#     return (can_travel, weight)

def get_edge2(graph, names):
    weight = 0
    can_travel = False
    name_list = []
    already_counted = []
    g_list = []
    edges = []
    for name in names:
        name_list.append(name.value)
        g_list = graph._adjacency_list[name]
        for each in g_list:
            both = [each.vertex.value, each.weight]
            edges.append(both)

    for each_name in name_list:
        for edge in edges:
            if each_name == edge[0]:
                if each_name not in already_counted:
                    weight += edge[1]
                    already_counted.append(each_name)
                    
    if weight > 0:
        can_travel = True
    return can_travel, weight

if __name__ == "__main__":
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    g.add_edge(a, b, 1)
    g.add_edge(a, c, 1)
    g.add_edge(c, b, 2)
    g.add_edge(c, a, 2)
    g.add_edge(a, d, 19)
    names = [a, c]
    edges = get_edge2(g, names)
    print(edges)
    
    
        