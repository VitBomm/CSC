x = int(input("Nhập số cần kiểm tra: "))
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

if checkPrime(x):
    print("Đây là số nguyên tố ")
else:
    print("Đây không phải là số nguyên tố")

