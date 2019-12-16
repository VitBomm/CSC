'''
Created on October 10, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''


# Tạo 1 tuple a chứa 4 số nguyên dương đầu tiên
tuple_a = (1, 2, 3, 4)
print('Tuple a:', tuple_a)

# Tạo 1 tuple b chứa 4 số nguyên dương tiếp theo
tuple_b = (5, 7, 6, 8)
print('Tuple b:', tuple_b)

# Tạo 1 tuple c là sự kết hợp của các phần tử trong tuple a và b

tuple_c = tuple_b + tuple_a 
print(tuple_c)  

# Tạo 1 tuple d từ tuple c với các phần tử được sắp xếp

tuple_d = sorted(tuple_c)
print(tuple(tuple_d))

# In phần tử thứ 3 của d

print("Phần từ thứ 3 của d: %i" % (tuple_d[2]))

# In 3 phần tử cuối cùng của d

print("Phần từ cuối của d: %i" % (tuple_d[-1]))
