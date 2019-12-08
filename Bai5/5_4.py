
# from pakage_bai5 import ham_bai_5 as bai5
# n = int(input("Nhập n: "))
# SumOdd = 0
# SumEven = 0
# Tich = 1
# Tichdived3 = 1
# SumPrime = 0
# for i in range(1,n+1,2):
#     SumOdd += i

# print("Tổng các số lẻ nhỏ hơn bằng %i: %i" %(n,SumOdd))

# for i in range(0,n+1,2):
#     SumEven += i

# print("Tổng các số chẳn nhỏ hơn bằng %i: %i" %(n,SumEven))

# for i in range(1,n+1):
#     Tich *= i

# print("Tích các số nhỏ hơn bằng %i: %i" %(n,Tich))

# for i in range(3,n+1,3):
#     Tichdived3 *= i

# print("Tích các số nhỏ hơn bằng %i chia hết cho 3: %i" %(n, Tichdived3))

# print(bai5.KiemTraSoNguyenTo(n))

import sys
sys.path.append('..\Python Visual Studio')
import bai9.ham_bai_5 as ham_bai_5
ham_bai_5.print_hell()


