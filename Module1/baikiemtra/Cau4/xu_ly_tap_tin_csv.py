import os
import csv
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_file_csv(filename):
    f = open(os.path.join(__location__,filename),newline='', encoding='utf-8')
    temp = csv.reader(f)
    for row in temp:
        print(', '.join(row))
    f.close()

def write_csv_file(filename, listContent):  
    f = open(os.path.join(__location__,filename),'a',newline='', encoding='utf-8')
    writer = csv.writer(f)
    writer.writerow(listContent)
    f.close()

def hoc_sinh_diem_cao_nhat(filename):
    f = open(os.path.join(__location__,filename),newline='', encoding='utf-8')
    temp = csv.reader(f)
    max_point = -1
    user_max_point = -1
    for row in temp:
        if max_point < int(row[2]):
            max_point = int(row[2])
            user_max_point = row
    if (isinstance(user_max_point,list)):
        print("Thông Tin Sinh Viên Có Điểm Cao Nhất: ")
        print(user_max_point)
    else:
        print("Không có dữ liệu")
    f.close()