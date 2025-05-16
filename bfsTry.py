# graph = [
#          [0, 1, 1, 1, 0],
#          [1, 0, 0, 1, 0],
#          [1, 0, 0, 1, 1],
#          [1, 1, 1, 0, 1],
#          [0, 0, 1, 1, 0]
#         ]

# queue = []
# visited = []
# starting = 4

# queue.append(starting)
# head = 0
# while(len(queue)>head):
#     current_node = queue[head]
#     head += 1
#     if current_node not in visited:
#         visited.append(current_node)
#         adj_nodes = graph[current_node]

#         for i in range(len(adj_nodes)):
#             if adj_nodes[i]==1:
#                 queue.append(i)

# print(visited)




import random
from collections import deque

# Function to print the grid nicely
def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))
    print()

# Function to perform BFS on the grid
def bfs(grid, start, goal):
    N = len(grid)
    visited = [[False] * N for _ in range(N)]
    parent = [[None] * N for _ in range(N)]
    
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[x][y]
            path.append(start)
            path.reverse()
            return path
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and grid[nx][ny] == 0:
                queue.append((nx, ny))
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
    
    return None  # No path found

# === Main Program ===

# Step 1: Input grid size
N = int(input("Enter grid size N: "))

# Step 2: Generate N x N grid with random obstacles (1 = obstacle, 0 = free)
grid = [[random.choice([0, 0, 0, 1]) for _ in range(N)] for _ in range(N)]  # More chance for free cells

print("\nGenerated Grid (0 = free, 1 = obstacle):")
print_grid(grid)

# Step 3: Get user input for start and goal positions
sx, sy = map(int, input("Enter start position (row col): ").split())
gx, gy = map(int, input("Enter goal position (row col): ").split())

# Check for valid start and goal
if grid[sx][sy] == 1 or grid[gx][gy] == 1:
    print("❌ Start or Goal is on an obstacle. Try again.")
else:
    path = bfs(grid, (sx, sy), (gx, gy))

    if path:
        print("✅ Path found:")
        print(" -> ".join(str(p) for p in path))
        
        # Show path in grid
        for x, y in path:
            if (x, y) != (sx, sy) and (x, y) != (gx, gy):
                grid[x][y] = "*"
        
        print("\nGrid with path (*):")
        print_grid(grid)
    else:
        print("❌ No path found from start to goal.")
