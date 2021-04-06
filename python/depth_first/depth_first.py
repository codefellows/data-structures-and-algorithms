from graph.graph import Graph, Vertex, Edge

def depth_first(adj_list):
    ####################################################
    ## Old logic
    # visited = []
    # stack = []
    
    # keys = adj_list.keys()
    # dict_keys = []
    # for key in keys:
    #     dict_keys.append(key)
    # # print('keys', adj_list[dict_keys[0]])
    # visited.append(dict_keys[0].value)
    # for each in dict_keys:
    #     for values in adj_list[dict_keys[each]]:
    #         stack.append(values)
    # # print('stack is ', stack)

    # while (len(stack)):
    #     s = stack.pop(0)
    #     # print('s value:', s.vertex.value)

    #     if s.vertex.value not in visited:
    #         visited.append(s.vertex.value)
        
    #     for node in stack:
    #         # print("node", node)
    #         if node.vertex.value not in visited:
    #             visited.append(node.vertex.value)
    #     # print(visited)

    # return visited
    ####################################################
    
    visited = []
    stack = []
    
    keys = adj_list.keys()
    dict_keys = []
    for key in keys:
        dict_keys.append(key)
    visited.append(dict_keys[0].value) # the first key/the root

    def traversal(a_list, key):
        print("visited is:", visited)
        if not a_list[key]:
            return

        for each_key in a_list[key]:
            if each_key.vertex.value not in visited:
                visited.append(each_key.vertex.value)
            traversal(a_list, each_key.vertex)
        return

    for each in dict_keys:
        if each.value not in visited:
            visited.append(each.value)
        for lists in adj_list[each]:
            if lists.vertex.value not in visited:
                visited.append(lists.vertex.value)
            print("lists are", lists.vertex.value)
            traversal(adj_list, lists.vertex)

    return visited

