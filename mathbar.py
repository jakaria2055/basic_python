# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array(["A","B","C","D"])
# y = np.array([3,8,1,10])

# plt.bar(x,y, color='#4CAF50', width = 0.1)

# plt.show()
#--------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()