# Học viên sử dụng biểu thức Lambda để tính Chu vi (P) 
# và Diện tích (S) theo yêu cầu sau:
# - Người dùng nhập vào r (bán kính), a (chiều dài), 
# b (chiều rộng) từ bàn phím (input)
# - Chương trình sẽ tính và in ra (output):
# + P, S hình tròn
# + P, S hình chữ nhật

# Ví dụ:
# - Tính diện tích hình tròn : s_tron = lambda r: math.pi * math.pow(r,2)
import math
r = eval(input("Nhập vào bán kính r: "))
a = eval(input("Nhập vào chiều dài a: "))
b = eval(input("Nhập vào chiều rộng a: "))
s_tron = lambda r: math.pi * math.pow(r,2)
p_tron = lambda r: 2*r * math.pi
s_nhat = lambda a,b : a * b
p_nhat = lambda a,b : (a + b) * 2
print("Diện tích hình tròn",s_tron(r))
print("Chu vi hình tròn",p_tron(r))
print("Diện tích hình chữ nhật",s_nhat(a,b))
print("Chu vi hình chữ nhật",p_nhat(a,b))

