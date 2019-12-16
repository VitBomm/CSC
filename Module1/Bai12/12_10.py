# Viết chương trình Tính tổng các số nguyên tố trong list có n phần tử, mỗi phần tử có giá trị ngẫu nhiên.
# - Sử dụng console
# - Hãy viết chương trình cho phép người dùng nhập vào số nguyên n là số phần tử cho list.
# => Chương trình tự động phát sinh giá trị (giá trị trong khoảng 0 - 100) cho các phần tử trong list => Xuất list
# - Tính tổng các số nguyên tố trong list
# - Gợi ý: Dùng hàm randrange ([start,] stop [,step]) để tạo số ngẫu nhiên
import random

def CreateList(n):
    listtemp = []
    for i in range(n):
        listtemp.append(random.randrange(100))
    return listtemp

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

n = int(input("Nhập số lượng phần tử trong list:"))

list1 = CreateList(n)
print(list1)
print("Tổng các số nguyên tố trong list: %i"%(sum([x for x in list1 if checkPrime(x)])))
    