'''
Created on October 10, 2019

@author: Trung Tâm Tin Học - Trường Đại học Khoa học Tự nhiên TP.HCM
'''


# Tạo một từ điển ((key: từ tiếng Anh, value: list nghĩa Tiếng Việt))
dictionary = {'work': ['công việc', 'việc làm', 'tác phẩm'], 'bark': ['vỏ cây', 'tiếng sủa', 'thuyền ba cột buồm'], 'bat':['con dơi', 'gậy', 'đánh bóng'], 'board': ['bảng', 'ban quản lý', 'lên tàu'], 'bowl' : ['cái bát', 'khán đài', 'quả bóng quần'], 'stamp' : ['con tem', 'phiếu mua hàng', 'con dấu'], 'club' : ['câu lạc bộ', 'gậy đánh golf', 'dùi cui']}

# Chương trình thực hiện các công việc:
i = 1
while i == 1:    
    cv = int(input('Bạn muốn làm gì? 1: Hiển thị từ điển; 2: Tra từ, 3: Thêm từ, 4: Xóa từ\t'))

    # Hiển thị từ điển, và cho biết trong từ điển hiện tại có bao nhiêu từ?
    if cv == 1:
        print('Dictionary:')
        print('Từ Anh \t Nghĩa Việt')
        for key,value in dictionary.items():
            print("%s\t%s" % (key,value))
        print("Trong từ điển hiện tại có: %i" % (len(dictionary.keys())))
        
    # Tìm kiếm từ tiếng Anh => nếu tìm thấy thì hiển thị key và value. 
    # Nếu không tìm thấy thì thông báo không tìm thấy
    elif cv == 2:
        name_search = input('Nhập từ cần tra:\t')
        if name_search in dictionary.keys():
            print("%s\t %s" % (name_search, dictionary[name_search]))
        else:
            print("Không tìm thấy")

    # Thêm từ vào từ điển, Hiển thị từ điển sau khi thêm 
    elif cv == 3:
        word = input('Nhập từ Anh:\t')
        meaning = input('Nhập nghĩa Việt:\t')
        if word in dictionary.keys():
            print("đã tồn tại từ trong Dictionary")
        else:
            dictionary[word] = meaning
    
    

    # Xóa một từ trong từ điển, dựa trên key cung cấp , và Hiển thị từ điển sau khi xóa
    elif cv == 4:
        word_delete = input('Nhập từ cần xóa:\t')
        x = int(input('Bạn có thật sự muốn xóa hay không? 1: Xóa, 0: Không\t'))
        if x == 1:
            if word_delete in dictionary.keys():
                del dictionary[word_delete]
             
    

    
    
    i = int(input('Tiếp tục lựa chọn? 1: Có; 0: Không\t'))