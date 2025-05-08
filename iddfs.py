class IterativeDeepening:
    def __init__(self):
        self.stack = []
        self.goal_found = False
        self.depth = 0
        self.max_depth = 0

    def iterative_deepening(self, adjacency_matrix, destination):
        self.num_nodes = len(adjacency_matrix)
        while not self.goal_found:
            print(f"\nTrying Depth: {self.max_depth}")
            self.depth_limited_search(adjacency_matrix, 0, destination)
            if self.goal_found:
                print(f"\nGoal Found at depth {self.depth}")
                return
            self.max_depth += 1

    def depth_limited_search(self, adjacency_matrix, source, goal):
        visited = [False] * self.num_nodes
        self.stack = [(source, 0)]  
        visited[source] = True

        while self.stack:
            element, current_depth = self.stack.pop()

            print(element, end="\t")

            if element == goal:
                self.goal_found = True
                self.depth = current_depth
                return

            if current_depth < self.max_depth:
                for destination in range(self.num_nodes - 1, -1, -1):  
                    if adjacency_matrix[element][destination] == 1 and not visited[destination]:
                        self.stack.append((destination, current_depth + 1))
                        visited[destination] = True


try:

    adjacency_matrix = [
    [0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0], 
    [0, 0, 0, 1, 1, 0],  
    [0, 0, 0, 0, 0, 1],  
    [0, 1, 0, 0, 0, 1],  
    [1, 0, 0, 0, 0, 0]   
    ]

    destination = int(input("Enter the destination node (0-5): "))
    if destination < 0 or destination > 5:
        raise ValueError("Invalid node number! Enter a number between 0 and 5.")

    iterative_deepening = IterativeDeepening()
    iterative_deepening.iterative_deepening(adjacency_matrix, destination)

except ValueError:
    print("Wrong Input format. Please enter a valid integer between 0 and 5.")
