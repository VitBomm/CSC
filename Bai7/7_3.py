# Viết chương trình thực hiện xử lý list số như sau:

# - Tạo list số: Cho phép người dùng lần lượt nhập các phần tử
#  số cho list cho đến khi không muốn nhập nữa.
# - Chương trình sẽ thực hiện những công việc sau:
# + In ra list các số vừa nhập.
# + Tìm và in ra tất cả các số nguyên tố có trong list.
# + Tính trung bình cộng của các phần tử âm/ phần tử dương trong list
# + Tìm giá trị chẵn lớn nhất/ giá trị lẻ nhỏ nhất trong list
# + Sắp xếp list theo giá trị tăng dần

def Average(lst):
    if len(lst) == 0:
        return "0"
    return sum(lst) / len(lst) 

def checkPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, x//2 + 1, 2):
        if x % i == 0:
            return False
    return True

list_so = []
while(True):
    try:
        a = int(input())
        list_so.append(a)
    except:
        break
print(list_so)
print("Các số nguyên trong list: %s"%(str([x for x in list_so if checkPrime(x)])))
print("Giá trị trung bình các số âm: %s" %(str(Average([x for x in list_so if x < 0]))))
print("Giá trị trung bình các số dương:  %s" % (str(Average([x for x in list_so if x >= 0]))))
temp = ""
list_so.sort(reverse=True)
found = False
for i in list_so:
    if i % 2 == 0:
        print("Giá trị chẵn lớn nhất là: %i" %(i))
        found = True
        break
if found == False:
    print("không tìm thấy giá trị chẵn trong list")

list_so.sort()
found = False
for i in list_so:
    if i % 2 != 0:
        print("Giá trị lẻ nhỏ nhất nhất là: %i" %(i))
        found = True
        break
if found == False:
    print("không tìm thấy giá trị lẻ trong list")
print("Sắp xếp list theo giá trị tăng dần: %s" % (str(list_so)))
