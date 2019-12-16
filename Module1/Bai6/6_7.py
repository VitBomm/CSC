# Học viên hãy viết chương trình đếm số lần xuất hiện của ký tự theo như yêu cầu sau:
# - Input: chuỗi ký tự và ký tự cần đếm số lần xuất hiện
# - Output: số lần xuất hiện
# Ví dụ:
# - Nhập chuỗi: mississippi
# - Nhập ký tự cần đếm số lần xuất hiện: s

# s xuất hiện 4 lần trong chuỗi mississippi

# P/S: Học viên có thể nâng cấp bài này lên bằng cách cho phép đếm số lần chuỗi ký tự con chứ không chỉ là ký tự.

a = input("Nhập chuỗi: ")
dem = input("Nhập sub: ")

print("Số lần xuất hiện của %s trong %s là %i"%(dem,a,len([i for i in range(len(a)) if a.startswith(dem,i)])))

