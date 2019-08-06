import numpy as np

def step_function1(x):
    y = x > 0  # 配列要素に対して不等号の演算をしてTrue/Falseのbool値を返す
    return y.astype(np.int)  # boolからintに型変換。Trueなら1を返す。

def step_function2(x):
    return np.array(x > 0, dtype=np.int)  # 圧縮記述

test = np.array([1, -1, 1, -1])

print(step_function1(test))
print(step_function2(test))
