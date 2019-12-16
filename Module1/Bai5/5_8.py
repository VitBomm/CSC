n = int(input("Nhập số nguyên n: "))
x = int(input("Nhập số thực x: "))
S0 =  (x**2 + x + 1)**n + (x**2 - x + 1)**n
#
print("Kết quả đúng %i" %(S0))
S1 = 1
S2 = 1

for j in range(2):
    S1 *= x
    S2 *= x
S1 += x + 1
temp1 = S1
for i in range(n-1):
    S1 *= temp1
S2 = S2 - x + 1
temp = S2
for i in range(n-1):
    S2 *= temp
S = S1 + S2

print("S: %i" %(S))

