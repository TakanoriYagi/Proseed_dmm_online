import numpy as np

def step(x):
    return np.array(x > 0, dtype=int)


X = np.array([[2.5, 3.0], [6.0, -4.0]])


class newralnetwork():
    def __init__(self):
        self.W_X = np.array([[3.0, -2.0, -3.0], [4.0, 6.0, 7.0]])
        self.W_U1 = np.array([[1.5, 8.9, 4.6, 2.1], [3.2, -7.4, -2.1, -1.0], [1.0, 2.9, -7.9, 5.9]])
        self.W_U2 = np.array([4.5, -3.5, -4.2, 2.5])

    def nn(self, x):
        u1 = np.dot(x, self.W_X)
        z1 = step(u1)
        u2 = np.dot(z1, self.W_U1)
        z2 = step(u2)
        y = np.dot(z2, self.W_U2)

        if(y > 0):
            print("パターンA")
        else:
            print("パターンB")


for i in X:
    a = newralnetwork()
    a.nn(i)