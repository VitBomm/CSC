# Một website yêu cầu người dùng nhập tên người dùng và mật khẩu để đăng ký. Tuy nhiên để bảo mật, 
# hệ thống yêu cầu cần phải kiểm tra xem mật khẩu người dùng nhập vào có đủ an toàn hay không.
# Các tiêu chí kiểm tra mật khẩu người dùng tạo bao gồm:
# 1. Ít nhất 1 chữ cái viết thường
# 2. Ít nhất có 1 ký số từ [0-9]
# 3. Ít nhất 1 kí tự viết HOA
# 4. Ít nhất có 1 ký tự đặc biệt trong các giá trị [$ # @]
# 5. Độ dài mật khẩu tối thiểu: 6
# 6. Độ dài mật khẩu tối đa: 12
# Chương trình như sau:
# - Người dùng sẽ nhập vào mật khẩu (Input)
# - Chương trình sẽ kiểm tra mật khẩu đó có đáp ứng những tiêu chí trên hay không?
# và in ra Mật khẩu bạn nhập là an toàn / không an toàn (Output)

# Ví dụ:
# + Input: ABd1234@1
# + Output: Mật khẩu bạn nhập là an toàn
password = input("Nhập mật khẩu cần kiểm tra: ")
def checkpassword(password):
    lowercase = False
    uppercase = False
    number = False
    specialchar = False
    lenpass = False
    if len(password) in range(6,13):
        lenpass = True
    for i in password:
        if ord(i) in range(97,123):
            lowercase = True
        if ord(i) in range(65,91):
            uppercase = True
        if ord(i) in range(48,58):
            number = True
        if i in ['#', '$', '@']:
            specialchar = True

    if lowercase and uppercase and number and specialchar and lenpass:
        print("Mật khẩu bạn nhập là an toàn")
    else:
        print("Mật khẩu bạn nhập là không an toàn")

checkpassword(password)


        