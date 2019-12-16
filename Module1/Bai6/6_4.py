# Xây dựng chương trình tính và in ra kết quả của biểu thức A = (x^2 + x + 1)^n + (x^2 - x + 1)^n
# - Người dùng nhập vào một số nguyên n và một số thực x (input)
# - Chương trình sẽ tính A = (x^2 + x + 1)^n + (x^2 - x + 1)^n
# và in ra kết quả A (output)

n = int(input("Nhập số nguyên n: "))
x = float(input("Nhập số thực x: "))
result = pow(pow(x,2) + x + 1,n) + pow(pow(x,2) - x + 1,n)
print("(%.2f^2 + %.2f + 1)^%i + (%.2f^2 - %.2f + 1)^%i = %f" % (x,x,n,x,x,n, result))
