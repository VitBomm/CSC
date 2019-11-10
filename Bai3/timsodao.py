n = int(input("Nhập số cần đảo: "))
tram = n%10
n = n/10
chuc = n% 10
n = n/10
donvi = n%10
n = n/10
print("%i%i%i" % (tram,chuc,donvi))