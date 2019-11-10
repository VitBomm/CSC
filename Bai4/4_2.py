x = eval(input("Nhập số cần tìm giá trị tuyệt đối: "))

if x < 0:
    x = -x

print("Giá trị tuyệt đối của x: %i" % (x))