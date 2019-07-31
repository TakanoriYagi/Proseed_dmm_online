cars = {"A": "ポルシェ",
        "B": "フェラーリ",
        "C": "ランボルギーニ",
        "D": "マセラティ",
        "E": "ベンツ",
        }
print(cars["A"])

# 追加してみます。
cars["F"] = "アウディ"
print(cars)

# 削除してみます。
del cars["E"]
print(cars)
