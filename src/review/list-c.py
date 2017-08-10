a = []
a = list(range(10))
print(a)

b = [i for i in a if i % 2 == 0]
print(b)

a.append(10)
if 10 in a:
    print("10")
else:
    print("0")
