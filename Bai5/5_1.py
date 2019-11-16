'''
Created on Feb 9, 2017

Trung Tam Tin Hoc - DH KHTN
'''
# Đếm ngược - Count down


n = int(input('Input number:\n'))

# In ra màn hình các giá trị đếm ngược từ n đến 1 bằng cách sử dụng vòng lặp while

m = n
print('Start!!!')
while(n>0):
    print(n)
    n -= 1
# In ra màn hình các giá trị đếm ngược từ n đến 1 bằng cách sử dụng vòng lặp for
print('Start!!!')
for i in range(m):
    print(m - i)
    