def read_graph_from_file(filename):
    graph = {}
    with open(filename, 'r') as file:
        for line in file:
            if ':' in line:
                node, neighbors = line.strip().split(':')
                graph[node.strip()] = [n.strip() for n in neighbors.strip().split()]
    return graph

def graph_coloring(graph):
    color = {}
    for node in graph:
        used_colors = set()
        for neighbor in graph[node]:
            if neighbor in color:
                used_colors.add(color[neighbor])
        for clr in range(len(graph)):
            if clr not in used_colors:
                color[node] = clr
                break
    return color

def display_colors(coloring):
    print("\nGraph Coloring Result:")
    for node in sorted(coloring):
        print(f"{node}: Color {coloring[node] + 1}")

# ======== Main Execution ========
filename = input("Enter the graph file path (e.g., graph.txt): ")

try:
    graph = read_graph_from_file(filename)
    coloring = graph_coloring(graph)
    display_colors(coloring)
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except Exception as e:
    print("An error occurred:", e)