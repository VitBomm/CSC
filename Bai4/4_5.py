loaiphong = eval(input("Loại phòng: "))
sodem = eval(input("Số Đêm: "))

if loaiphong == "Standard":
    price = 1260000
elif loaiphong == "Superior Garden":
    price = 1550000
elif loaiphong == "Superior Ocean view":
    price = 1830000
elif loaiphong == "Garden View Bungalow":
    price = 1830000
elif loaiphong == "Pool View Bunggalow":
    price = 2120000
elif loaiphong == "Family Room":
    price = 2120000
elif loaiphong == "Beach Front Bungalow":
    price = 2540000
else:
    price = 4800000

if 1 < sodem < 4:
    price =  0.75 * price * sodem 
elif sodem >= 4:
    price = 0.7 * price * sodem

print("Số tiền cần phải thanh toán: %i" % (price))
