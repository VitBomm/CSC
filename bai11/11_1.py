'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
# Xây dựng phương thức đọc nội dung tập tin

def read_file(filename):
    f = open(os.path.join(__location__,filename),'r')
    print(f.read())
    

filename = input('Nhập tên tập tin:\n')
print(filename)
print('\nNội dung tập tin:')
print(read_file(filename))



# In kết quả
'''
Nhập tên tập tin:
Johny.txt

Nội dung tập tin:
Johny, Johny
Yes, Papa?
Eating sugar?
No, papa!
Telling lies?
No, papa!
Open your mouth
Ha, ha, ha!

'''