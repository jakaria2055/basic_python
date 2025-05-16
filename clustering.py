import random
import math
import matplotlib.pyplot as plt

# dataset = [(1,3), (3,5), (4,6), (6,10), (20, 12), (1,7), (3,5), (9,2), (5,3), (1,10)]

dataset = [
    (5, 0), (6, 1), (7, 0), (6, -1), (5, 1), (7, 1), (6, 0), (5, 0), (6, -1), (4, 1),
    (15, 10), (16, 11), (15, 11), (16, 10), (14, 10), (17, 11), (16, 12), (15, 12), (14, 11), (16, 9),
    (25, 20), (26, 21), (25, 22), (24, 21), (26, 20), (25, 19), (27, 21), (24, 20), (23, 19), (25, 19),
    (6, 7), (7, 8), (8, 7), (7, 7), (6, 8), (6, 6), (7, 6), (8, 8), (7, 8), (6, 7),
    (15, 10), (16, 9), (14, 9), (16, 8), (15, 8), (17, 9), (16, 10), (14, 10), (15, 11), (16, 10),
    (7, 2), (8, 3), (7, 2), (6, 3), (7, 3), (8, 2), (7, 1), (6, 2), (8, 1), (6, 1),
    (24, 21), (25, 22), (24, 20), (23, 21), (25, 20), (24, 22), (23, 23), (26, 22), (24, 23), (23, 22),
    (7, 8), (6, 8), (7, 9), (8, 8), (6, 7), (7, 7), (6, 9), (8, 9), (7, 6), (8, 6),
    (5, 1), (6, 0), (5, 0), (6, 1), (7, 1), (5, 0), (6, 1), (5, -1), (7, 0), (6, -1),
    (15, 11), (16, 11), (17, 10), (15, 10), (16, 9), (15, 9), (16, 9), (15, 8), (14, 10), (17, 11),
    (25, 19), (24, 20), (25, 21), (24, 22), (23, 20), (25, 22), (24, 21), (26, 20), (25, 20), (26, 21)
]

k= 3
all_claster = {"A":[], "B":[], "C":[]}
CR = {}

def visual_cluster(cluster_data):
    # Define colors for each key
    colors = {'A': 'blue', 'B': 'green', 'C': 'red'}

    # Plot each group with a different color
    for key, points in cluster_data.items():
        x_values, y_values = zip(*points)  # Separate the dataset into x and y values
        plt.scatter(x_values, y_values, color=colors[key], label=key)

    # Add labels and title
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Scatter Plot of Points by Key')

    # Show grid and legend
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

def visual(dataset):
    x_values, y_values = zip(*dataset)

    # Create a scatter plot
    plt.scatter(x_values, y_values, color='blue', label='Data points')

    # Add labels and title
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.title('Scatter Plot of the Dataset')

    # Show grid and legend
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()

rand_pos = []
while len(rand_pos)<k:
    x = random.randint(0, len(dataset)-1)
    if x not in rand_pos:
        rand_pos.append(x)

print(rand_pos)
random_selected_point = []
for i, cluster in enumerate(all_claster.keys()):
    # print(i, cluster)
    all_claster[cluster].append(dataset[rand_pos[i]])
    CR[cluster] = dataset[rand_pos[i]]
    random_selected_point.append(dataset[rand_pos[i]])

print(dataset)
visual(dataset)

for i in random_selected_point:
    dataset.remove(i)


print(all_claster)
print(CR)
print(dataset)

def dist(d1, d2):
    return math.sqrt((d1[0]-d2[0])**2 + (d1[1]-d2[1])**2)

def update_CR(cluster):
    min_distance = 9999
    selected_CR = None
    for p_CR in all_claster[cluster]:
        distances = []
        for comp in all_claster[cluster]:
            distances.append(dist(p_CR, comp))
        if min_distance > distance:
            min_distance = distance
            selected_CR = p_CR

    CR[cluster] = selected_CR

for datapoint in dataset:
    min_distance = 9999
    selected_cluster = None
    for cluster in CR.keys():
        current_representative = CR[cluster]
        distance = dist(datapoint, current_representative)

        if min_distance > distance:
            min_distance = distance
            selected_cluster = cluster

    all_claster[selected_cluster].append(datapoint)

print(all_claster)
visual_cluster(all_claster)