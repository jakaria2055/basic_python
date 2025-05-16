import matplotlib.pyplot as plt
import numpy as np

x = np.array([12, 15, 11, 14, 13, 16, 10, 17, 12, 14, 13, 11, 15])
y = np.array([8, 7, 9, 6, 8, 5, 9, 4, 7, 6, 8, 9, 7])
plt.scatter(x, y, color = "hotpink")

x = np.array([20, 23, 19, 22, 21, 24, 18, 25, 20, 22, 21, 19, 23])
y = np.array([4, 3, 5, 2, 4, 1, 5, 0, 3, 2, 4, 5, 3])

plt.scatter(x, y, color='#88c999')

plt.show()