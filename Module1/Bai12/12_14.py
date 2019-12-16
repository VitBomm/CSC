# Viết chương trình:
# - Cho phép người dùng nhập vào số nguyên dương n.
# - Chương trình sẽ tạo một dictionary có n phần tử, 
# với mỗi phần tử có key là các giá trị lần lượt từ 1 đến n và value = key * key

n = int(input("Số lượng phần tử: "))
dict_n = {}
for i in range(1,n+1):
    dict_n[i] = pow(i,2)

print(dict_n)