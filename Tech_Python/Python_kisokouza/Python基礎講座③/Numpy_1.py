# Numpyを使用するには、まず、importでNumpyを読み込む必要があります。
# 今後、様々なパッケージを使用すると思いますが、Importが必要になってきます。
# as と名前を付けることができ、今後その名前で呼び出せます。
# 今回は、Numpyをnpと名前をつけています。一般的に、Numpyはnpと名前を付けられます。
import numpy as np

x = [1.0, 2.0, 3.0]
y = [4.0, 5.0, 6.0]
z = x + y

print(z)

x_matrix = np.array([1.0, 2.0, 3.0])
y_matrix = np.array([4.0, 5.0, 6.0])
z_matrix = x_matrix + y_matrix

print(z_matrix)

