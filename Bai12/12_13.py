# Viết chương trình với yêu cầu sau:
# - Tạo 3 dictionary: dic1, dic2, dic3 có số lượng phần tử và 
# giá trị key:vulue là giá trị số tùy ý
# - Hãy viết chương trình tạo một dictionary mới dic4 với các
#  phần tử được lấy từ 3 dictionary trên.
# - Tìm phần tử có value lớn nhất/ nhỏ nhất trong dictionary

dic1 = {"temp": 1}
dic2 = {"temp1": 2}
dic3 = {"temp2": 3}
dic4 = {}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
max_dict = max(dic4.values())
min_dict = min(dic4.values())

for key,value in dic4.items():
    if dic4[key] == max_dict:
        print("%s có phần tử %i là lớn nhất" % (key,value))
    if dic4[key] == min_dict:
        print("%s có phần tử %i là nhỏ nhất" % (key,value))
