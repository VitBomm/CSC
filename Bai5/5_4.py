n = int(input("Nhập n: "))
SumOdd = 0
SumEven = 0
Tich = 1
Tichdived3 = 1
SumPrime = 0
for i in range(1,n+1,2):
    SumOdd += i

print("Tổng các số lẻ nhỏ hơn bằng %i: %i" %(n,SumOdd))

for i in range(0,n+1,2):
    SumEven += i

print("Tổng các số chẳn nhỏ hơn bằng %i: %i" %(n,SumEven))

for i in range(1,n+1):
    Tich *= i

print("Tích các số nhỏ hơn bằng %i: %i" %(n,Tich))

for i in range(3,n+1,3):
    Tichdived3 *= i

print("Tích các số nhỏ hơn bằng %i chia hết cho 3: %i" %(n, Tichdived3))
def checkPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, x//2 + 1, 2):
        if x % i == 0:
            return False
    return True

for i in range(n+1):
    if checkPrime(i):
        SumPrime += i

print("Tổng các số nguyên tố nhỏ hơn hay bằng %i: %i" %(n,SumPrime))


