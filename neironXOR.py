# ФРЕНК РОЗЕНБЛАТТ 1957 год
import numpy as np
import matplotlib.pyplot as plt

class_cnt = 5
bias = 3

x1 = np.random.random(class_cnt)
x2 = x1 + [np.random.randint(10)/10 for i in range(class_cnt)] + bias
C1 = [x1, x2]

x1 = np.random.random(class_cnt)
x2 = x1 - [np.random.randint(10)/10 for i in range(class_cnt)] - 0.1 + bias
C2 = [x1, x2]

f = [0 + bias, 1 + bias]


w2 = 0.3
w3 = -bias*w2
w = np.array([-w2, w2, w3])
for i in range(class_cnt):
    x = np.array([C2[0][i], C2[1][i], 1])
    y = np.dot(w, x)
    if y >= 0:
        print("C1")
    else:
        print("C2")

plt.scatter(C1[0][:], C1[1][:], s=10, c="red")
plt.scatter(C2[0][:], C2[1][:], s=10, c="blue")
plt.plot(f)
plt.grid(True)
plt.show()

