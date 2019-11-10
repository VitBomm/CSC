MST = input()
name = input()
TongThuNhap = int(input())
SoNguoiPhuThuoc = int(input())
Sotiengiamtru = 108000000 + (SoNguoiPhuThuoc*3600000*12)
sotienchiuthue = TongThuNhap - Sotiengiamtru
sotienchiuthue = sotienchiuthue / 100000
if sotienchiuthue > 960:
    print("Số tiền chịu thuế phải đóng: %i" % (0.35*sotienchiuthue))
elif sotienchiuthue > 624:
    print("Số tiền chịu thuế phải đóng: %i" % (0.3*sotienchiuthue))
elif sotienchiuthue > 384:
    print("Số tiền chịu thuế phải đóng: %i" % (0.25*sotienchiuthue))
elif sotienchiuthue > 216:
    print("Số tiền chịu thuế phải đóng: %i" % (0.20*sotienchiuthue))
elif sotienchiuthue > 120:
    print("Số tiền chịu thuế phải đóng: %i" % (0.15*sotienchiuthue))
elif sotienchiuthue > 60:
    print("Số tiền chịu thuế phải đóng: %i" % (0.10*sotienchiuthue))
elif sotienchiuthue > 0:
    print("Số tiền chịu thuế phải đóng: %i" % (0.5*sotienchiuthue))
else:
    print("Số tiền chịu thuế phải đóng: 0")