print("Antonov Nikita ISIP19-5")
graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'C'],
         'C': ['A', 'B'],
         'D': ['B']}


def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(set(graph[vertex]) - set(visited))
    return visited

print(dfs(graph, 'C'))