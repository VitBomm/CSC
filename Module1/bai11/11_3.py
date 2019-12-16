'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Phương thức ghi nội dung vào tập tin
def write_file(filename, content):
    f = open(os.path.join(__location__,filename),'w+')
    f.write(content)



# Phương thức đọc nội dung tập tin
def read_file(filename):
    f = open(os.path.join(__location__,filename),'r')
    return f.read()


filename = input('Nhập tên tập tin:\n')
content = input('\nNhập nội dung:\n')
write_file(filename, content)
print('\nNội dung tập tin:\n ', read_file(filename))