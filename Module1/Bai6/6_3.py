# Xây dựng chương trình tính và in ra kết quả của biểu thức S = (x^2 + 1)^n
# - Người dùng nhập vào một số nguyên n và một số thực x (Input).
# - Chương trình sẽ tính S = (x^2 + 1)^n
# và in ra Tổng S (Output).

n = int(input("Nhập số nguyên n: "))
x = float(input("Nhập số thực x:"))

print("(%.2f^2 + 1) ^ %.2f = %.2f" % (x,n,pow(pow(x,2) + 1,n)))