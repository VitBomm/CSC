n = int(input("Nhập số nguyên n: "))
x = int(input("Nhập số thực x: "))
#S = (x**2 + 1)**n
S = 1
for j in range(2):
    S *= x
S += 1
temp = S
for i in range(n-1):
    S *= temp

print("S: %i" %(S))
