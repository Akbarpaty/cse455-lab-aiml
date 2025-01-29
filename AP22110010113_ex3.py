graph = {
    'a': ['b', 'c', 'd'],
    'b': ['e'],
    'c': ['e', 'f'],
    'd': ['f'],
    'e': ['z'],
    'f': ['z'],
    'z': []
}

def dls(node, depth, max_depth, path):
    path.append(node)
    
    if depth < max_depth:
        for neighbor in graph.get(node, []):  
            if neighbor not in path:  
                dls(neighbor, depth + 1, max_depth, path)
    
    return path

start = 'a'
maxlimit = 2  

path = dls(start, 0, maxlimit, [])
print("Nodes visited in level order:", ' -> '.join(path))
