'''
Created on October 24, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Học viên xây dựng phương thức ghi nội dung vào cuối tập tin
def write_to_end_of_file(filename, content):
    f = open(os.path.join(__location__,filename),'a', encoding='utf-8')
    f.write(content)
    f.write('\n')
    f.close()






    

# Phương thức đọc nội dung tập tin
def read_file(filename):
    f = open(os.path.join(__location__,filename),'r', encoding='utf-8')
    str = f.read()
    f.close()
    return str


filename = input('Nhập tên tập tin:\n')
while True:
    choice = int(input('Do you want to write file ? 1: Yes, 0: No \n'))
    if choice == 0:
        break
    content = input("Noi Dung: \n")
    write_to_end_of_file(filename, content)
print('\nNội dung tập tin sau khi ghi: ')
print(read_file(filename))

    

# In kết quả
'''
Nhập tên tập tin:
QuaDeoNgang.txt
Nhập nội dung:
Bước tới Đèo Ngang, bóng xế tà,
Bạn có muốn tiếp tục ghi nội dung vào file? 1: Có; 0: Không
1
Nhập nội dung:
Cỏ cây chen đá, lá chen hoa.
Bạn có muốn tiếp tục ghi nội dung vào file? 1: Có; 0: Không
1
Nhập nội dung:
Lom khom dưới núi, tiều vài chú
Bạn có muốn tiếp tục ghi nội dung vào file? 1: Có; 0: Không
1
Nhập nội dung:
Lác đác bên sông, chợ mấy nhà.
Bạn có muốn tiếp tục ghi nội dung vào file? 1: Có; 0: Không
0
Đã ghi nội dung vào tập tin QuaDeoNgang.txt

Nội dung tập tin sau khi ghi:  
Bước tới Đèo Ngang, bóng xế tà,
Cỏ cây chen đá, lá chen hoa.
Lom khom dưới núi, tiều vài chú
Lác đác bên sông, chợ mấy nhà.

'''