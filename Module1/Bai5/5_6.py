n = input("Một chuỗi bất kỳ:")

countNum = 0
countChar = 0
for i in n:
    if ord(i) in range(65,91) or ord(i) in range(97,123):
        countChar += 1
    if ord(i) in range(48,58):
        countNum += 1

print("Số lượng ký tự trong chuỗi %i" % (countChar))
print("Số lượng số trong chuỗi %i" % (countNum))