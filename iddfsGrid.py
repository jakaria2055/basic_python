import matplotlib.pyplot as plt

class IterativeDeepening:
    def __init__(self):
        self.goal_found = False
        self.max_depth = 0
        self.path = []

    def iterative_deepening(self, adj_matrix, source, goal):
        self.num_nodes = len(adj_matrix)
        while not self.goal_found:
            visited = [False] * self.num_nodes
            self.path = []
            print(f"Trying depth: {self.max_depth}")
            self.dls(adj_matrix, source, goal, 0, visited)
            if self.goal_found:
                print("Goal found!")
                print("Path:", self.path)
                return
            self.max_depth += 1

    def dls(self, adj_matrix, current, goal, depth, visited):
        visited[current] = True
        self.path.append(current)

        if current == goal:
            self.goal_found = True
            return

        if depth == self.max_depth:
            self.path.pop()
            return

        for neighbor in range(len(adj_matrix[current])):
            if adj_matrix[current][neighbor] == 1 and not visited[neighbor]:
                self.dls(adj_matrix, neighbor, goal, depth + 1, visited)
                if self.goal_found:
                    return

        self.path.pop()

# ====== Visualization Function ======
def draw_path(path):
    x = list(range(len(path)))
    y = [1]*len(path)
    labels = [str(node) for node in path]

    plt.plot(x, y, 'bo-')
    for i, label in enumerate(labels):
        plt.text(x[i], y[i]+0.05, label, ha='center', fontsize=12)

    plt.ylim(0.9, 1.2)
    plt.xticks([])
    plt.yticks([])
    plt.title("IDS Path Visualization (without networkx)")
    plt.show()

# ====== Example Usage ======
adjacency_matrix = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0]
]

try:
    goal = int(input("Enter goal node (0–5): "))
    if goal < 0 or goal > 5:
        raise ValueError

    ids = IterativeDeepening()
    ids.iterative_deepening(adjacency_matrix, 0, goal)

    if ids.goal_found:
        draw_path(ids.path)

except ValueError:
    print("Invalid input! Please enter a number between 0 and 5.")
