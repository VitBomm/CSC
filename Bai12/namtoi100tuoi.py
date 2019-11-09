import datetime
now = datetime.datetime.now()
name = input("Tên người dùng: ")
age = int(input("Tuổi người dùng: "))
print("%s 100 tuổi vào năm : %i" %(name,(now.year - age + 100)))