graph = [[0, 1, 1, 1, 0],
         [1, 0, 0, 1, 0],
         [1, 0, 0, 1, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 1, 1, 0]
        ]
queue = []
visited = []
starting = 4

queue.append(starting)
head = 0
while(len(queue)>0):
    current_node = queue.pop()
    head = head + 1
    if current_node not in visited:
        visited.append(current_node)
        adj_nodes = graph[current_node]
       
        for i in range(len(adj_nodes)):
            if adj_nodes[i] == 1:
                queue.append(i)
               
print(visited)