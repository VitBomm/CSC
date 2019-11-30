# Yêu cầu: Hãy viết lại các bài 7.2, 7.4, 7.6 trong bài 7 bằng 
# cách xây dựng phương thức/ hàm.

# Hướng dẫn:
# - Bài 7.2:
# + Xây dựng phương thức tao_list(list_create): dùng để nhập các 
# phần tử vào list. Kết quả trả về là list_original sau khi đã thêm các phần tử.
# + Xây dựng phương thức tinh_tong_list(list_create): dùng để tính 
# tổng các phần tử trong list. Kết quả trả về là tổng của list.

# - Bài 7.4:
# + Xây dựng phương thức dem_slxh(tuple_original, x): dùng để đếm 
# số lần xuất hiện của x trong tuple. Kết quả trả về là số lần xuất hiện.

# - Bài 7.6:
# + Xây dựng phương thức in_dictionary(dictionary): 
# dùng để in dictionary theo định dạng mỗi item (key : value) hiển thị trên một dòng.
# + Xây dựng phương thức tim_kiem_dictionary(dictionary, key_search): 
# dùng để tìm key_search trong từ điển. Kết quả trả về là chuỗi key : value nếu tìm thấy, 
# ‘Không tìm thấy <key_search>’ nếu không tìm thấy.
# + Xây dựng phương thức them_dictionary(dictionary, key_insert, value_insert): 
# dùng để thêm key : value mới vào dictionary. Kết quả trả về là dictionary sau khi đã thêm

# 7.2
list_so = []
def tinh_tong_list(list_so):
    return sum(list_so)

def tao_list(list_create):
    while(True):
        try:
            a = int(input())
            list_create.append(a)
        except:
            break
# tao_list(list_so)
# print(list_so)
# temp = tinh_tong_list(list_so)
# print("Tổng các phần tử trong list",temp)

# 7.4
# def dem_slxh(tuple_original, x):
#     return tuple_original.count(x)

# tup = (1,2,3,4,5,1,1,1)
# print(dem_slxh(tup,1))

# 7.6
dictionary = {'work': ['công việc', 'việc làm', 'tác phẩm'], 'bark': ['vỏ cây', 'tiếng sủa', 'thuyền ba cột buồm'], 'bat':['con dơi', 'gậy', 'đánh bóng'], 'board': ['bảng', 'ban quản lý', 'lên tàu'], 'bowl' : ['cái bát', 'khán đài', 'quả bóng quần'], 'stamp' : ['con tem', 'phiếu mua hàng', 'con dấu'], 'club' : ['câu lạc bộ', 'gậy đánh golf', 'dùi cui']}
def in_dictionary(dictionary):
    print("(Key : Value)")
    for key, value in dictionary.items():
        print("(%s : %s)" % (key,str(value)))

in_dictionary(dictionary)



# def tim_kiem_dictionary(dictionary, find):
#     for key, value in dictionary.items():
#         if find == key:
#             return "(%s : %s)" % (key, str(value))
#     return "Không tìm thấy key cần tìm"
# find = input("Nhập key cần tìm kiếm: ")
# result_find = tim_kiem_dictionary(dictionary, find)
# print(result_find)

key_insert = input("Nhập vào key cần insert: ")
value_insert = input("Nhập vào value cần insert")
def them_dictionary(dictionary, key_insert, value_insert):
    if key_insert not in dictionary.keys():
        dictionary.update({
            key_insert : value_insert
        })
    else:
        print("Key đã tồn tại trong dictionary")

them_dictionary(dictionary, key_insert, value_insert)
print("Dictionary sau khi insert")
print(dictionary)



