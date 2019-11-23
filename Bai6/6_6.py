# Học viên viết chương trình xử lý chuỗi bằng cách sử dụng hàm thư viện Strings.

# - Người dùng nhập vào chuỗi s, chuỗi s_sub, chuỗi s_find, chuỗi s_replace.
# - Chương trình sẽ xử lý chuỗi và in ra các kết quả sau:
# + In chuỗi s
# + Loại bỏ khoảng trắng ở đầu và cuối chuỗi
# + In chuỗi với ký tự đầu chuỗi viết hoa
# + Đếm và in ra số lần chuỗi con s_sub xuất hiện trong chuỗi s
# + Tìm kiếm s_find trong s và thay thế bằng s_replace, in chuỗi sau khi tìm kiếm và thay thế.

s = input("Nhập vào chuỗi s: ")
s_sub = input("Nhập vào chuỗi s_sub:")
s_find = input("Nhập vào chuỗi s_find:")
s_replace = input("Nhập vào chuỗi s_replace:")

print("In chuỗi s: %s" % (s))
print("Loại bỏ khoảng trắng đầu và cuối: %s" % (s.strip()))
print("In chuỗi với kí tự đầu viết hoa s: %s" % (s.capitalize()))
print("Đếm và in ra số lần chuỗi con s_sub xuất hiện trong chuỗi s: %i" % (len([i for i in range(len(s)) if s.startswith(s_sub, i)])))
print("Tìm kiếm s_find trong s và thay thế bằng s_replace, in chuỗi sau khi tìm kiếm và thay thế: %s" % (s.replace(s[s.find(s_find)],s_replace)))