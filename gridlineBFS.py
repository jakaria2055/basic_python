# graph = [[0, 1, 0, 0, 0],
#          [0, 1, 0, 1, 0],
#          [0, 0, 0, 1, 0],
#          [1, 1, 0, 0, 0],
#          [0, 0, 0, 1, 0]]

# start = (0, 0)
# goal = (4, 4)

# queue = [start]
# visited = [start]
# parent = {}  # to track path
# found = False

# # Direction: up, down, left, right
# dir = [(-1,0), (1,0), (0,-1), (0,1)]

# while len(queue) > 0:
#     x, y = queue.pop(0)

#     if (x, y) == goal:
#         found = True
#         break

#     for dx, dy in dir:
#         nx = x + dx
#         ny = y + dy

#         if 0 <= nx < 5 and 0 <= ny < 5:
#             if graph[nx][ny] == 0 and (nx, ny) not in visited:
#                 queue.append((nx, ny))
#                 visited.append((nx, ny))
#                 parent[(nx, ny)] = (x, y)

# if found:
#     path = []
#     node = goal
#     while node != start:
#         path.append(node)
#         node = parent[node]
#     path.append(start)
#     path.reverse()

#     print("✅ Path Found:")
#     for p in path:
#         print(p, end=" -> ")
#     print("Done")
# else:
#     print("❌ No path found")

#---------------------------------------------
import matplotlib.pyplot as plt

graph = [[0, 1, 0, 0, 0],
         [0, 1, 0, 1, 0],
         [0, 0, 0, 1, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 1, 0]]

start = (0, 0)
goal = (4, 4)

queue = [start]
visited = [start]
parent = {}
found = False

dir = [(-1,0), (1,0), (0,-1), (0,1)]

while len(queue) > 0:
    x, y = queue.pop(0)

    if (x, y) == goal:
        found = True
        break

    for dx, dy in dir:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 5 and 0 <= ny < 5:
            if graph[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.append((nx, ny))
                parent[(nx, ny)] = (x, y)

# Mark path if found
path = []
if found:
    node = goal
    while node != start:
        path.append(node)
        node = parent[node]
    path.append(start)
    path.reverse()

# ========== Plotting ==========

fig, ax = plt.subplots()
for i in range(5):
    for j in range(5):
        if graph[i][j] == 1:
            color = 'black'  # obstacle
        elif (i, j) == start:
            color = 'green'  # start
        elif (i, j) == goal:
            color = 'red'    # goal
        elif (i, j) in path:
            color = 'blue'   # path
        else:
            color = 'white'  # free cell

        rect = plt.Rectangle([j, 5 - i - 1], 1, 1, facecolor=color, edgecolor='gray')
        ax.add_patch(rect)

plt.xlim(0, 5)
plt.ylim(0, 5)
plt.gca().set_aspect('equal')
plt.axis('off')
plt.title("BFS Path Visualization")
plt.show()
