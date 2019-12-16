# Nhập tên tập tin csv và nội dung bao gồm danh sách các sinh viên.
# Một sinh viên bao gồm mã sinh viên, tên sinh viên, điểm.
# Nếu chưa tồn tại tập tin: tạo tập tin csv và ghi nội dung vào
# Nếu đã tồn tại tập tin: ghi thêm nội dung vào cuối tập tin tin csv
# Hỏi người dùng có muốn tiếp tục ghi nữa hay không? Người dùng
# chọn 1: có, chọn 0: không
# Nếu chọn 1: yêu cầu người dùng nhập nội dung => ghi nội
# dung vào cuối tập tin, xuống dòng
# Nếu chọn 0: kết thúc chương trình
# - Đọc nội dung từ file csv vừa tạo và hiển thị ra màn hình.
# - In ra thông tin các sinh viên có điểm cao nhất.
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

from xu_ly_tap_tin_csv import read_file_csv, write_csv_file, hoc_sinh_diem_cao_nhat

filename = input('Vui lòng nhập tên file để ghi dữ liệu: ')
while(True):
    manv = input("Nhập mã nhân viên: ")
    tennv = input("Nhập tên nhân viên: ")
    diem = input("Điểm: ")
    write_csv_file(filename,[manv,tennv,diem])
    con = int(input("Nhập giá trị tiếp hay không ? 1 Có, 0 : Không "))
    if con == 0:
        break
read_file_csv(filename)
hoc_sinh_diem_cao_nhat(filename)

