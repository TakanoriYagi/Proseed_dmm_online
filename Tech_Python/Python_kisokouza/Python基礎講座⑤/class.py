import numpy as np


class test1:
    def step_function(x):
        print(np.array(x > 0, dtype=np.int))


class test2:
    # 初期値を設定するときはこのように書きます。
    # self は初期化メソッドといいます。
    def __init__(self):
        self.enpitsu = 50
        self.keshigomu = 100

    def goukeikinngaku(self, number_e, number_k):
        goukei = self.enpitsu*number_e + self.keshigomu*number_k
        goukei = str(goukei)
        print(goukei + "円")

a = np.array([1.0])
y = test1
y.step_function(a)

z = test2()
z.goukeikinngaku(20, 20)
