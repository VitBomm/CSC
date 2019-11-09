Sum = int(input("Tổng số tiền các món ăn và thức uống: "))
tax = int(input("Thuế phải trả cho hóa đơn: "))
tip = int(input("Tip: "))

print("Thuế phải trả %.2f" % (tax/100 * Sum))
print("Tip phải trả %.2f" % (tip/100 * Sum))
print("Tổng số tiền cần thanh toán %.2f: " % (Sum + (tax/100 * Sum) + (tip/100 * Sum)))