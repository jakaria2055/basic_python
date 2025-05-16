# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([80, 85,90,95,100,105,110,115,120,125])
# y = np.array([240,250,260,270,280,290, 300, 310,320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)

# plt.grid(color = 'green', linestyle='--', linewidth = 0.5)

# plt.show()
# -----------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(3,2, 1)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(3,2, 2)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(3,2, 3)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(3,2, 4)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(3,2, 5)
plt.plot(x,y)

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(3,2, 6)
plt.plot(x,y)


plt.show()



