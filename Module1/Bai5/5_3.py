n = int(input("Nhập n: "))
a = 0
b = 1
print(a)
print(b)
for i in range(n - 2):
    if i % 2 == 0:
        a = a + b
        print(a)
    else:
        b = b + a
        print(b)