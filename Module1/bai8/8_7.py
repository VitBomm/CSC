'''
Created on October 17, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Xây dựng hàm tính lũy thừa
def exponents(bases,powers):
    temp = []
    for i in bases:
        for j in powers:
            temp.append(i**j)
    return temp

    





# In kết quả
print(exponents([2, 3, 4, 5], [1, 2, 3]))  # Kết quả in ra: [2, 4, 8, 3, 9, 27, 4, 16, 64, 5, 25, 125]