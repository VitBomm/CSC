loaixe = eval(input("Nhập loại xe: "))
sokm = eval(input("Số km di chuyển: "))
timewait = eval(input('Thời gian chờ: '))

costwait = 0
tiencuoc = 0
if timewait > 5:
    costwait = (timewait - 5) * 750

if loaixe == 4 and sokm > 0:
    tiencuoc += 11000
    if sokm > 31:
        tiencuoc += (31 * 15300) + (sokm - 31) * 12100
    else:
        tiencuoc += (31 - sokm) * 15300
else:
    tiencuoc += 12000
    if sokm > 31:
        tiencuoc += (31 * 16100) + (sokm - 31) * 13800
    else:
        tiencuoc += (31 - sokm) * 15300

print("Tiền chờ: %i" % (costwait))
print("Tiền cước: %i" % (tiencuoc))
