from graph.graph import Graph, Vertex, Edge

def depth_first(adj_list):
    visited = []
    stack = []
    
    keys = adj_list.keys()
    dict_keys = []
    for key in keys:
        dict_keys.append(key)
    # print('keys', adj_list[dict_keys[0]])
    visited.append(dict_keys[0].value)
    for values in adj_list[dict_keys[0]]:
        stack.append(values)
    # print('stack is ', stack)

    while (len(stack)):
        s = stack.pop(0)
        # print('s value:', s.vertex.value)

        if s.vertex.value not in visited:
            visited.append(s.vertex.value)
        
        for node in stack:
            # print("node", node)
            if node.vertex.value not in visited:
                visited.append(node.vertex.value)
        # print(visited)

    return visited