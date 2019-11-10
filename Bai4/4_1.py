a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
d = int(input("Nhập d: "))

gtln = a
if b > gtln:
    gtln = b
if c > gtln:
    gtln = c
if d > gtln:
    gtln = d

print("Giá Trị lớn nhất là: %i" %(gtln))
