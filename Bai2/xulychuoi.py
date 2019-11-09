s1 = input("Chuỗi s1")
s2 = input("Chuỗi s2")
s3 = input("Chuỗi s3")
index = int(input("Chỉ mục index"))

print("Chiều dài: s1 = %i, s2 = %i, s3 = %i" % (len(s1), len(s2), len(s3)))
s4 = s1[index::]
print(s4*2)