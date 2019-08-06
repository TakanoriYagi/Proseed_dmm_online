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

# # 前回は、このように書いていた。それをNumpyで行列表記してみよう。
# X = [x1, x2]
# W_X = [[w1u1, w1u2, w1u3], [w2u1, w2u2, w2u3]]
# W_U = [w3, w4, w5]
# # u1, u2 , u3　を求める
# u1 = X[0]*W_X[0][0] + X[1]*W_X[1][0]
# u2 = X[0]*W_X[0][1] + X[1]*W_X[1][1]
# u3 = X[0]*W_X[0][2] + X[1]*W_X[1][2]
#
# # yを求める
# y = u1*W_U[0] + u2*W_U[1] + u3*W_U[2]
# Numpyで書いてみる

X = np.array([x1, x2])
W_X = np.array([[w1u1, w1u2, w1u3], [w2u1, w2u2, w2u3]])
W_U = np.array([w3, w4, w5])
#
u = np.dot(X, W_X)
y = np.dot(u, W_U)

print(u)
print(y)
