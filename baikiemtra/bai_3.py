# Tạo danh sách nhân viên kiểu dictionary với key là mã nhân viên,
# value bao gồm các thông tin : tên nhân viên, số điện thoại, lương.
#  Cho phép người dùng lần lượt nhập các phần tử cho danh sách cho
# đến khi không muốn nhập nữa
# => Chương trình sẽ thực hiện những công việc sau:
# - Hiển thị danh sách nhân viên.
# - Cho phép người dùng tim kiếm theo mã nhân viên.
import copy
dict_temp = {}
print("Nhập thông tin danh sách nhân viên: ")
while(True):
    manv = input("Nhập mã nhân viên: ")
    tennv = input("Nhập tên nhân viên: ")
    sdt = input("Nhập số điện thoại: ")
    salary = eval(input("Nhập lương: "))
    dict_temp[manv] = [tennv, sdt, salary]
    con = int(input("Nhập giá trị tiếp hay không ? 1 Có, 0 : Không "))
    if con == 0:
        break

print("DSNV : ",dict_temp)
print('*'*50,'Danh sách nhân viên','*'*50)
print('Mã nv',' '*25,'Họ Tên',' '*25,'Số điện thoại',' '*25,'Lương')
for key,values in dict_temp.items():
    print(key,' '*25,values[0], ' '*25, values[1], ' '*25,values[2])

x = input("Nhập mã nhân viên cần tìm: ")
if x in dict_temp.keys():
    print("Thông tin nhân viên")
    result = copy.copy(dict_temp[x])
    result.insert(0,x)
    print(result)
else:
    print("Không tìm thấy nhân viên với mã: ",x)
