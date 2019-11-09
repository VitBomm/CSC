laisuat1nam = float(input("Lãi suất một năm: "))
sotiengui = int(input("Số tiền gửi: "))
sothang = int(input("Số tháng: "))

tienlai = (sotiengui * sothang) * (laisuat1nam/100/ 12)
tongsotien = sotiengui + tienlai

print("Tiền lãi: %.2f" % (tienlai))
print("Tổng số tiền: %.2f" % (tongsotien))