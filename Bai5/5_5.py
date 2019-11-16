n = input("Nhập chuỗi cần đảo ngược:")
m = n.split(' ')
s = ""
for i in range(len(m)):
    s += str(m[i][::-1]) + ' '
print(s.strip())