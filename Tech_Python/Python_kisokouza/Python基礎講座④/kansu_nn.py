import numpy as np

x1 = 1.0
x2 = 2.0
w1u1 = 3.0
w1u2 = 1.0
w1u3 = -3.0
w2u1 = 2.5
w2u2 = 2.0
w2u3 = -1.0
w3 = -4.0
w4 = 1.5
w5 = 4.2

# ステップ関数を定義
def step_function(x):
    return np.array(x>0, dtype=int)

X = np.array([x1, x2])
W_X = np.array([[w1u1, w1u2, w1u3], [w2u1, w2u2, w2u3]])
W_U = np.array([w3, w4, w5])

u = np.dot(X, W_X)
# ステップ関数をここで使用している。
z = step_function(u)
y = np.dot(z, W_U)

print(y)

