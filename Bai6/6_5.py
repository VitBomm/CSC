# Xây dựng chương trình giải phương trình bậc 2: ax^2 + bx + c = 0
# - Người dùng nhập vào a, b, c (Input)
# - Dựa vào quy tắc xử lý trong file đính kèm, chương trình sẽ giải phương trình bậc 2
# và in ra nghiệm x1, x2 (Output)
import math
a = eval(input("Nhập a:"))
b = eval(input("Nhập b:"))
c = eval(input("Nhập c:"))

if a == 0:
    if b == 0:
        if c != 0:
            print("Phương trình vô nghiệm")
        else:
            print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình có nghiệm: %.2f" % (-c/a))
else:
    delta = pow(b,2) - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có 1 nghiệm kép: %.2f" % (-b/2*a))
    else:
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 = %.2f" % ((-b+ math.sqrt(delta) )/2*a))
        print("x2 = %.2f" % ((-b - math.sqrt(delta) )/2*a))
