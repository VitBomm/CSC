# Viết chương trình:
# - Tạo list1 có số lượng phần tử tùy ý, giá trị mỗi phần tử kiểu số
# - Tạo list2 có số lượng phần tử tùy ý, giá trị mỗi phần tử kiểu số
# - In list1, list2
# - Tạo list3 từ list1 và list2 với những phần tử trong list3 
# được tạo thành từ những phần tử vừa có trong list1 vừa có trong list2
# - Tạo list4 từ list1 và list2 với những phần tử trong list4 
# được tạo thành từ những phần tử chỉ có trong list1 và chỉ có trong list2
# - Gợi ý:
list1 = set([1, 2, 3, 4])
list2 = set([1, 2,5])


list3 = list(list1.intersection(list2))
print(list3)
list4 = list(list1 - list2) + list(list2 - list1)
print(set(list4))