cars = {"A": "ポルシェ",
        "B": "フェラーリ",
        "C": "ランボルギーニ",
        "D": "マセラティ",
        "E": "ベンツ",
        }

n = input("アルファベットで車を選んでください")
if n in cars:
    car = cars[n]
    print(car)
else:
    print("見つかりません。")

# コンテナの中に、コンテナがあるパターン。

# 空のリストを用意しています。
cars2 = []

german = ["ベンツ", "アウディ", "ポルシェ"]
italia = ["フェラーリ", "マセラティ", "ランボルギーニ"]
japan = ["トヨタ", "日産", "マツダ"]

cars2.append(german)
cars2.append(italia)
cars2.append(japan)

print(cars2)

german = cars2[0]
print(german)

