'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''

import csv
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Học viên xây dựng phương thức đọc nội dung tập tin .CSV
def read_csv_file(filename):    
    f = open(os.path.join(__location__,filename),newline='')
    temp = csv.reader(f)
    for row in temp:
        print(', '.join(row))




    

filename = input('Nhập tên tập tin .csv:\n')
print('\nNội dung tập tin:')
print(read_csv_file(filename))



# In kết quả
'''
Nhập tên tập tin .csv:
menu.csv

Nội dung tập tin:
['Monday', 'ham', 'biscuits', 'corn', 'spinach', 'apple pie']
['Tuesday', 'steak', 'rolls', 'yams', 'beets', 'crème brulee']
['Wednesday', 'fried chicken', 'biscuits', 'mashed potatoes', 'cole slaw', 'vanilla ice cream']
['Thursday', 'clam rolls', 'tartar sauce', 'french fries', 'ice tea', 'chocolate ice cream']
['Friday', 'meat loaf', 'biscuits', 'lima beans', 'garden salad', 'chocolate cake']
None

'''