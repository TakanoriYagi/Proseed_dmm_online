import numpy as np

# ２×２行列を、x, y それぞれ定義しています。
x = np.array([[1.0, 2.0], [3.0, 4.0]])
y = np.array([[5.0, 6.0], [7.0, 8.0]])

# np.dot()は行列の積を求めるメソッドです。
z = np.dot(x, y)

print(z)
