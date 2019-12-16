'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''
# Viết chương trình ghi danh sách số điện thoại vào cuối file csv như sau:
# - Người dùng nhập tên tập tin csv (ví dụ: danhba.csv), 
# danh sách số điện thoại (Tên – Số điện thoại)
# - Chương trình sẽ ghi danh sách số điện thoại vào tập tin.
import csv
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Học viên xây dựng phương thức ghi nội dung vào tập tin .csv
def write_csv_file(filename, listContent):  
    f = open(os.path.join(__location__,filename),'a',newline='')
    writer = csv.writer(f)
    for content in listContent:
        writer.writerow(content)
    f.close()





# Học viên xây dựng phương thức đọc nội dung tập tin .csv
def read_csv_file_column(filename):
    f = open(os.path.join(__location__,filename),newline='')
    temp = csv.reader(f)
    for row in temp:
        print(', '.join(row))
    f.close()
    








filename = input('Nhập tên tập tin .csv:\n')
listContent = [['Johnny Lee', '0913 753852'], ['Peter Son', '0989 753951'], ['Johnnathan','0903 123456']]
write_csv_file(filename, listContent)
print('\nNội dung tập tin sau khi ghi: ')
read_csv_file_column(filename)


# In kết quả
'''
Nhập tên tập tin .csv:
danhba.csv

Nội dung tập tin sau khi ghi:
Name     Fone
Sarah	0989 788951
Daisy	0973 329496
Owthen	0773 700951
Lee	    0383 900852
Johnny Lee       0913 753852
Peter Son        0989 753951
Johnnathan       0903 123456

'''