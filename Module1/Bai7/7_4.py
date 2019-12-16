'''
Created on October 10, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''


# Tạo 1 tuple có 10 phần tử chuỗi bất kỳ
tuple_strings = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange','red', 'blue')

# In tuple vừa tạo
print('Tuple:', tuple_strings)

# Nhập index dương (0 <= index < 10), index âm (-1 >= index >= -9)
chuoi_1 = 'Nhập số từ 0 đến ' + str(len(tuple_strings) -1) + ': \t'
chuoi_2 = 'Nhập số từ -1 đến ' + str(-(len(tuple_strings))) + ':\t'
index_duong = int(input(chuoi_1))
index_am = int(input(chuoi_2))


# In giá trị của phần tử trong tuple có index dương và index âm đã nhập

print(tuple_strings[index_duong])
print(tuple_strings[index_am])

# Nhập chuỗi cần tìm s_find 
s_find = input('Nhập chuỗi cần tìm:\n')

# Tìm và đếm số lần xuất hiện của s_find trong tuple 
print("Số lần xuất hiện s_find trong tuple: %i "% (tuple_strings.count(s_find)))
