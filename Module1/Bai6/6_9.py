# Học viên viết chương trình xử lý ngày, tháng, năm bằng cách sử dụng hàm thư viện Datetimes.
# - Người dùng nhập vào ngày, tháng, năm (hợp lệ)
# - Chương trình sẽ xử lý ngày, tháng, năm, và in kết quả theo các yêu cầu sau:
# + Xuất ngày theo định dạng ngày – tháng - năm
# + Cho biết năm được nhập vào có phải là năm nhuận hay không?
# + Cho biết ngày/tháng/năm nhập vào là thứ mấy?
# + Cho biết tháng nhập vào có bao nhiêu ngày?

from datetime import datetime
import calendar
ngay = int(input("Ngày: "))
thang = int(input("Tháng: "))
nam = int(input("Năm: "))
dateinput = datetime(nam,thang,ngay)
dict_temp = {0:"Hai",1:"Ba",2:"Tư",3:"Năm",4:"Sáu",5:"Bảy",6:"Chủ Nhật"}
print("Xuất ngày theo định dạng ngày – tháng - năm: %s" %(dateinput.strftime("%d-%m-%Y")))
print("Cho biết năm được nhập vào có phải là năm nhuận hay không? : %s" %(str(calendar.isleap(dateinput.year))))
print("Cho biết ngày/tháng/năm nhập vào là thứ mấy?: %s" % (dict_temp[calendar.weekday(dateinput.year,dateinput.month,dateinput.day)]))
print("Cho biết tháng nhập vào có bao nhiêu ngày? %i" % (calendar.monthrange(dateinput.year, dateinput.month)[1]))
