# Viết chương trình tìm thú trong vườn thú với yêu cầu sau:
# - Tạo ra một list có các con thú.
# - Nhập vào một con thú cần tìm
# => Chương trình in ra danh sách các con thú, số lượng các con thú 
# và kết quả tìm kiếm con thú (Con thú cần tìm có/không có trong list).

animals = ['turtle','tortoise','dog','cat','bird','lion']

find_animal = input('Nhập con thú cần tìm: ')

print("Danh sách các con thú: ")
for i in animals:
    print(i)
print("Số lượng các con thú: %i" % (len(animals)))
print("Con thú cần tìm: %s trong list" %("có " if find_animal in animals else "không"))