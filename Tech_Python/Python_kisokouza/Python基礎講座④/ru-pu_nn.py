import numpy as np


def step_function(x):
    return np.array(x > 0, dtype=np.int)


X = np.array([[2.5, 3.0], [6.0, -4.0]])
W_X = np.array([[3.0, -2.0, -3.0], [4.0, 6.0, 7.0]])
W_U1 = np.array([[1.5, 8.9, 4.6], [3.2, -7.4, -2.1], [1.0, 2.9, -7.9]])
W_U2 = np.array([4.5, -3.5, -4.2])

for i in X:
    u1 = np.dot(i, W_X)
    z1 = step_function(u1)
    u2 = np.dot(z1, W_U1)
    z2 = step_function(u2)
    y = np.dot(z2, W_U2)
    print(y)