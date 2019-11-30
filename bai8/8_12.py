# Học viên áp dụng các built-in function map(), 
# reduce(), filter() cho những bài tập list, tuple của bài List – Tuple - Dictionary
# - Tính tổng các phần tử trong list
# - List các số lớn hơn x
# - List các số nguyên tố
# - List các phần tử âm
# - List các phần tử dương.
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
from functools import reduce
listtemp = [1,2,3,4,5,6,7,8,-1,-2,-3,-4,5]
x = int(input("Nhập vào x: "))
tong_list = reduce(lambda item1, item2 : item1 + item2, listtemp)
greater_than_x = list(filter(lambda item: item > x, listtemp))
prime_list = list(filter(checkPrime,listtemp))
greater_than_0 = list(filter(lambda item: item > 0, listtemp))
less_than_0 = list(filter(lambda item: item < 0, listtemp))

print("Tổng các phần tử trong list:",tong_list)
print("Các phần tử lớn hơn x trong list:",greater_than_x)
print("Các phần tử là số nguyên tố trong list:",prime_list)
print("Các phần tử lớn hơn 0 trong list:",greater_than_0)
print("Các phần tử nhỏ hơn 0 trong list:",less_than_0)



