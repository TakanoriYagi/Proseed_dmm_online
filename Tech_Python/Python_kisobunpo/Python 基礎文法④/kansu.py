# f(x) = x * 2 を関数で作ってみます。


def f(x):
    return x * 2


print(f(2))


# 引数にあらかじめ数値を設定することもできます。
def f(x=2):
    return x * 3


print(f())
print(f(4))
