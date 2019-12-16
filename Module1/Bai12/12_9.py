tu = int(input("Từ số: "))
den = int(input("Tới số: "))
temp = ""

for j in range(1,10):
    temp = ""
    for i in range(tu, den+1):
        temp += "%i x %i = %i" % (i,j,i*j) + "\t"
    print(temp)
