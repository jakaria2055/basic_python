graph = {
    "A": ["D"],
    "B": ["E", "D"],
    "C": ["D", "E", "F"],
    "D": ["A", "B", "C", "E"],
    "E": ["C", "B", "D", "E", "F", "H"],
    "F": ["C", "E", "H"],
    "G": ["H"],
    "H": ["E", "F", "G"]
}

color = {}

for current_node in graph.keys():
    if current_node not in color.keys():
        adj_color = []
        for adj_node in graph[current_node]:
            if adj_node in color.keys():
                adj_color.append(color[adj_node])
    for selected_color in range(len(graph)):
        if selected_color not in adj_color:
            color[current_node] = selected_color
            break
for node in color.keys():
    color[node] = color[node] + 1
print(color)