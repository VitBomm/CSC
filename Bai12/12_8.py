from operator import mul
n = int(input("Nhập n: "))
nthanthan = 1
nthan = 1
for i in range(1,n+1):
    nthan *= i
if n % 2 == 0:
    for i in range(2,n+1,2):
        nthanthan *= i
else:
    for i in range(1,n+1,2):
        nthanthan *= i
print("n! = %i"  % (nthan))
print("n!! = %i" % (nthanthan))
