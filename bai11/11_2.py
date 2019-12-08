import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_report_file(filename):
    file_in = open(os.path.join(__location__,filename),'r')
    print('\nNội dung tập tin: ')
    count_lines = 0
    count_words = 0
    count_chars = 0
    str1 = ''
    
    # Học viên viết code để thống kê (số dòng, số từ, số ký tự)
    lines = file_in.readlines()
    count_lines = len(lines)
    for x in lines:
        count_words += len(x.split(' '))
        for i in x.split(' '):
            count_chars += len(i)

    file_in.close()
    
    print(str1)
    print("\n----- Thống kê: Số dòng/ Số từ/ Số ký tự -----")
    print('Lines:', count_lines, ', Words:', count_words, ', Chars:', count_chars)


filename = input('Nhập tên tập tin:\n')
read_report_file(filename)



# In kết quả
'''
Nhập tên tập tin:
Hope.txt

Nội dung tập tin:
I hoped that he would love me,
And he has kissed my mouth,
But I am like a stricken bird
That cannot reach the south.
For though I know he loves me,
To-night my heart is sad;
His kiss was not so wonderful
As all the dreams I had.

----- Thống kê: Số dòng/ Số từ/ Số ký tự -----
Lines: 8 , Words: 49 , Chars: 232

'''