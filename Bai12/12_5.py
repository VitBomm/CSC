def checkYear(year):
    if year % 400 == 0:
        return 1
    if year % 4 == 0 and year % 100 != 0:
        return 1
    return 0

def checkValidate(day, month, year):
    if 0 > month > 12  or year < 0 or 0 > day > 31:
        return 0
    if month in [4,9,6,11]:
        if day == 31:
            return 0
    elif month == 2:
        if checkYear(year):
            if day > 29:
                return 0
        else:
            if day > 28:
                return 0
    return 1

Day = int(input("Nhập ngày: "))
Month = int(input("Nhập tháng: "))
Year = int(input("Nhập năm: "))
if checkValidate(Day,Month,Year):
    print('Ngày hợp lệ')
else:
    print('Ngày không hợp lệ')