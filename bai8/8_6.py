'''
Created on October 17, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

# Xây dựng hàm đếm số lần x xuất hiện trong chuỗi word

def count_char_x(word, x):
    return word.count(x)
      
# In kết quả

print(count_char_x("mississippi", "s"))       # Kết quả:   4

print(count_char_x("mississippi", "m"))       # Kết quả:   1