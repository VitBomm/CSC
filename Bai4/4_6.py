dtb = eval(input("Nhập điểm trung bình: "))

if dtb > 8:
    loai = "Giỏi"
elif dtb > 6.5:
    loai = "Khá"
elif dtb > 5.0:
    loai = "Trung Bình"
elif dtb > 0:
    loai = "Yếu"

print("Xếp loại học sinh: %s" % (loai))