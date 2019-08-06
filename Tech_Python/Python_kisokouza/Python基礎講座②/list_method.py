# append()
print("append()")
x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
x.append(6)
print(x)

# clear()
print("clear()")
x.clear()
print(x)

# extend()
print("extend()")
x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
y = [6, 7, 8, 9]
x.extend(y)
print(x)

# insert()
print("insert()")
x.clear()
x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
x.insert(3, 10)
print(x)

# del
print("del")
x.clear()
x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
del x[3]
print(x)

# remove()
print("remove()")
x.clear()
x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
x.remove(1)
print(x)

# pop()
print("pop()")
x.clear()
x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(x.pop(3))
print(x)

# index()
print("index()")
x.clear()
x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(x.index(2))

# count()
print("count()")
x.clear()
x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(x.count(2))

# sort()
print("sort()")
x.clear()
x = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
x.sort()
print(x)
x.sort(reverse=True)
print(x)

