# Tạo list
#  Nhập số phần tử trong list
#  Cho phép người dùng lần lượt nhập các phần tử cho list cho đến khi
# không muốn nhập nữa
# => Chương trình sẽ thực hiện những công việc sau:
# a/ Đếm tần suất xuất hiện của các phần tử. Chẳng hạn với list gồm
# các phần tử: 12 34 12 34 43 12 5 thì tần suất xuất hiện các phần tử là 12 (3
# lần), 34 (2 lần), 12 (2 lần), 5 (1 lần).

list_temp = []

while(True):
    x = eval(input("Nhập giá trị: "))
    list_temp.append(x)
    con = int(input("Tiếp tục nhập giá trị? 1: Có, 0: Không "))
    if con == 0:
        break

print('List: ', list_temp)
temp2 = set(list_temp)
sorted1 = sorted(list_temp)
sorted2 = sorted(list_temp,reverse=True)

for i in temp2:
    count_temp = list_temp.count(i)
    print("Phần tử ",i,' xuất hiện ',count_temp,' lần')

if list_temp == sorted1 or list_temp == sorted2:
    print("List có thứ tự")
else:
    print("List không có thứ tự")