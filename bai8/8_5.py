'''
Created on October 17, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Xây dựng hàm kiểm tra vị trí có giá trị giống nhau trong hai list số

def same_values(lst1, lst2):
    temp = []
    zip1 = list(zip(lst1,lst2))
    print(zip1)
    for i in range(len(zip1)):
        if zip1[i][0] == zip1[i][1]:
            temp.append(i)
    return temp


# In kết quả

print(same_values([5, 1, -10, 3, 3, 9], [5, 10, -10, 3, 5, 20]))     # Kết quả:  [0, 2, 3]

print(same_values([3, 2, -10, 43, 3], [5, 10, -10, 3, 5]))           # Kết quả:  [2]