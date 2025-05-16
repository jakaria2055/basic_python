# import matplotlib.pyplot as plt

# # গ্রাফ ডেটা
# graph = {
#     "A": ["D"],
#     "B": ["E", "D"],
#     "C": ["D", "E", "F"],
#     "D": ["A", "B", "C", "E"],
#     "E": ["C", "B", "D", "E", "F", "H"],
#     "F": ["C", "E", "H"],
#     "G": ["H"],
#     "H": ["E", "F", "G"]
# }

# # Color assignment (same as greedy logic)
# color = {}
# for current_node in graph.keys():
#     if current_node not in color.keys():
#         adj_color = []
#         for adj_node in graph[current_node]:
#             if adj_node in color.keys():
#                 adj_color.append(color[adj_node])
#     for selected_color in range(len(graph)):
#         if selected_color not in adj_color:
#             color[current_node] = selected_color
#             break
# for node in color:
#     color[node] += 1

# # Color map
# color_map = {
#     1: "red",
#     2: "green",
#     3: "blue",
#     4: "orange",
#     5: "purple",
#     6: "yellow"
# }

# # Node positions (manually placed for plotting)
# positions = {
#     "A": (1, 3),
#     "B": (0, 2),
#     "C": (2, 2),
#     "D": (1, 2),
#     "E": (1, 1),
#     "F": (2, 1),
#     "G": (0, 0),
#     "H": (1, 0)
# }

# # Plotting
# fig, ax = plt.subplots()
# for node, (x, y) in positions.items():
#     circle = plt.Circle((x, y), 0.2, color=color_map[color[node]])
#     ax.add_patch(circle)
#     plt.text(x, y, node, fontsize=12, ha='center', va='center', color='white')

# # Draw edges manually
# for node in graph:
#     x1, y1 = positions[node]
#     for adj in graph[node]:
#         x2, y2 = positions[adj]
#         plt.plot([x1, x2], [y1, y2], 'gray')

# ax.set_aspect('equal')
# plt.xlim(-1, 3)
# plt.ylim(-1, 4)
# plt.axis('off')
# plt.title("Graph Coloring Visualization (without networkx)")
# plt.show()

#-----------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt

# গ্রাফ ডেটা
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

# Color assignment (same as greedy logic)
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
for node in color:
    color[node] += 1

# Color map
color_map = {
    1: "red",
    2: "green",
    3: "blue",
    4: "orange",
    5: "purple",
    6: "yellow"
}

# Node positions (manually placed for plotting)
positions = {
    "A": (1, 3),
    "B": (0, 2),
    "C": (2, 2),
    "D": (1, 2),
    "E": (1, 1),
    "F": (2, 1),
    "G": (0, 0),
    "H": (1, 0)
}

# Plotting
fig, ax = plt.subplots()
for node, (x, y) in positions.items():
    circle = plt.Circle((x, y), 0.2, color=color_map[color[node]])
    ax.add_patch(circle)
    plt.text(x, y, node, fontsize=12, ha='center', va='center', color='white')

# Draw edges manually
drawn_edges = set()
for node in graph:
    x1, y1 = positions[node]
    for adj in graph[node]:
        if (adj, node) not in drawn_edges:
            x2, y2 = positions[adj]
            plt.plot([x1, x2], [y1, y2], 'gray')
            drawn_edges.add((node, adj))

ax.set_aspect('equal')
plt.xlim(-1, 3)
plt.ylim(-1, 4)
plt.axis('off')
plt.title("Graph Coloring Visualization (without networkx)")
plt.show()
