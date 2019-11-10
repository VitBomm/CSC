sokwh = eval(input("Số kwh tiêu thụ: "))
if 0 < sokwh < 50:
    price = 1678
elif 51 < sokwh < 100:
    price = 1734
elif 101 < sokwh < 200:
    price = 2014
elif 201 < sokwh < 300:
    price = 2536
elif 301 < sokwh < 400:
    price = 2834
else:
    price 2927

print("Tổng tiền cần phải chi trả: %i" % (price * sokwh))