# Dãy Fibonacci là dãy vô hạn các số tự nhiên 
# bắt đầu bằng hai phần tử 0 và 1, có quy luật khá đơn giản: “Phần tử đứng sau bằng tổng hai phần tử trước đó cộng lại”.

# Trong bài tập này, Học viên viết lại bài tập 
# Dãy Fibonacci bằng cách xây dựng hàm (Dùng kỹ thuật đệ quy)
# - Người dùng nhập vào giá trị n (Input)
# - Chương trình sẽ in ra dãy số Fibonacci đến n (Output)

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

n = int(input("Nhập vào n: "))
if n <= 0:
    print("Error")
for i in range(n):
    print(Fibonacci(i))
    

