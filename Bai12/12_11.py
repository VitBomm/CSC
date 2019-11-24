# Nhập vào một list có 5 phần tử. Xuất list vừa tạo. Ví dụ: 2, 7, 1, 4, 8. Sau đó:
# - Xác định xem có cặp số nào trong các số đó có quan hệ chia hết hay không? 
# Nếu có thì in ra tất cả các cặp số đó. Ví dụ: cặp 2 & 1, 2 & 4, 2 & 8, 7 & 1, 1 & 4, 4 & 8, 1 & 8
# - Xác định xem có cặp số nào trong các số đó có quan hệ số này gấp 2 lần số kia hay không? 
# Nếu có thì in ra tất cả các cặp số đó. Ví dụ: cặp 2 & 1, 2 & 4, 4 & 8
# - Xác định xem có cặp số nào trong các số đó mà tổng hai số bằng 8 hay không? 
# Nếu có thì in ra tất cả các cặp số đó. Ví dụ: cặp 7 & 1
# - Gợi ý: Duyệt list
list_1 = []
for i in range(5):
    n = int(input())
    list_1.append(n)
list_1.sort(reverse=True)

list_result1 = []
for i in range(len(list_1)):
    for j in range(i+1,len(list_1)):
        if list_1[i] % list_1[j] == 0:
            list_result1 += [(list_1[i],list_1[j])]
print(list_result1)
list_result2 = []
for i in range(len(list_1)):
    for j in range(i+1,len(list_1)):
        if list_1[i] == 2*list_1[j]:
            list_result2 += [(list_1[i],list_1[j])]
print(list_result2)            
list_result3 = []
for i in range(len(list_1)):
    for j in range(i+1,len(list_1)):
        if list_1[i] + list_1[j] == 8:
            list_result3 += [(list_1[i],list_1[j])]
print(list_result3)