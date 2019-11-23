# Viết chương trình xử lý list số theo các yêu cầu sau:

# Yêu cầu 1:
# - Tạo list số: Cho phép người dùng lần lượt nhập các 
# phần tử số cho list cho đến khi không muốn nhập nữa.
# - Chương trình sẽ :
# + In ra list các số vừa nhập.
# + Tính tổng các phần tử trong list.

# Yêu cầu 2:
# - Người dùng nhập vào một số x cần tìm
# - Chương trình sẽ cho biết :
# + x có xuất hiện trong list hay không? Nếu có thì cho biết x xuất hiện bao nhiêu lần?
# + x có lớn hơn tất cả các số trong list không?
# + Nếu không thì x nhỏ hơn những số nào trong list? (In ra tất cả các số lớn hơn x)

list_so = []
while(True):
    try:
        a = int(input())
        list_so.append(a)
    except:
        break
print(list_so)
print(sum(list_so))

x = int(input("Nhập vào số x cần tìm: "))

if x in list_so:
    print("x có xuất hiện trong list:")
    print("x xuất hiện: %i trong list" % (list_so.count(x)))
else:
    print("x không có xuất hiện trong list")
if x > max(list_so):
    print("x lớn hơn tất cả số trong list")
else:
    print("x không lớn hơn tất cả số trong list")
    print("Các số mà x nhỏ hơn: %s" % (str([y for y in list_so if y > x])))

