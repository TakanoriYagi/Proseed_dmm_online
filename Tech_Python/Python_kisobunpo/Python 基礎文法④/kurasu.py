# 長方形の面積を出す、クラスを作成します。


# self変数は、インスタンス変数の定義に使います。インスタンス変数とはそのオブジェクトに属する変数のことです。
# いくつものオブジェクトを作ると、各オブジェクトはそれぞれ異なる属性値をインスタンス変数として持つことになります。
# インスタンス変数は、以下の構文で定義します。
# self.[変数名] = [値]
# 通常、インスタンス変数は __init__ という特別なメソッドの中で定義し（ initはinitialize ＝ 初期化の略です）
# オブジェクトを作るときにPythonから 呼び出されます。


class Chohokei:
    def __init__(self, tate, yoko):
        self.len = tate
        self.width = yoko

    def menseki(self):
        return self.len * self.width

    def change_size(self, tate, yoko):
        self.len = tate
        self.width = yoko


chohokei = Chohokei(20, 10)
print(chohokei.menseki())
chohokei.change_size(40, 20)
print(chohokei.menseki())

