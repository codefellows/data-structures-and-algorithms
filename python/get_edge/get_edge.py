# from graph.graph import Graph, Vertex, Edge

def get_edge(graph, names):
    actual_nodes = graph.get_nodes()
    print(actual_nodes)
    weight = 0
    can_travel = False
    for name in names:
        for nodes in actual_nodes:
            print('nodes[0]', nodes[1][1])
            if name in nodes[0]:
                for node in nodes:
                    for each in node:
                        print('each is:', each)
                        # weight += each[1]
                    print('node is', node[0])
                    # weight += node
                # weight += nodes[1][1]
                can_travel = True
    return (can_travel, weight)