'''
Created on October 17, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''
import copy

# Xây dựng hàm xóa

def delete_starting_evens(lst):
    index = 0
    for i in lst[:]:
        if i % 2 != 0:
            return lst
        else:
            lst.remove(i)
    return lst


# In kết quả

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))    # Kết quả:  [11, 12, 15]

print(delete_starting_evens([6, 2, 18]))    # Kết quả:  []