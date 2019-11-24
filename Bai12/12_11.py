# list_1 = []
# for i in range(5):
#     n = int(input())
#     list_1.append(n)
# list_1.sort(reverse=True)

# list_result1 = []
# for i in range(len(list_1)):
#     for j in range(i+1,len(list_1)):
#         if list_1[i] % list_1[j] == 0:
#             list_result1 += [(list_1[i],list_1[j])]
# print(list_result1)
# list_result2 = []
# for i in range(len(list_1)):
#     for j in range(i+1,len(list_1)):
#         if list_1[i] == 2*list_1[j]:
#             list_result2 += [(list_1[i],list_1[j])]
# print(list_result2)            
# list_result3 = []
# for i in range(len(list_1)):
#     for j in range(i+1,len(list_1)):
#         if list_1[i] + list_1[j] == 8:
#             list_result3 += [(list_1[i],list_1[j])]
# print(list_result3)
setA = {1,2,6,3,7}
setB = {1,4,5,8,9}
setC = setA | setB
print(setC)