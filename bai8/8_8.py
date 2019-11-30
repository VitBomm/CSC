'''
Created on October 17, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Xây dựng hàm kiểm tra đảo ngược của hai list số

def reversed_list(lst1, lst2):
    return lst1 == lst2[::-1]
 
# In kết quả

print(reversed_list([1, 2, 3, 4], [4, 3, 2, 1]))   # Kết quả: True

print(reversed_list([1, 5, 3, 7], [3, 2, 1]))      # Kết quả: False