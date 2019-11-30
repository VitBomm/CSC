# Học viên viết lại các bài tập của Bài 5 (Tính S, Tính A, và Kiểm tra số nguyên tố) 
# bằng cách xây dựng phương thức/ hàm.

# Hướng dẫn:
# - Bài Tính S:
# Xây dựng phương thức tinh_S(n, x): với n và x là tham số truyền vào, 
# phương thức có giá trị trả về là S = (x^2+ 1)^n

# - Bài Tính A:
# Xây dựng phương thức tinh_A(n, x): với n và x là tham số truyền vào, 
# phương thức có giá trị trả về là A = (x^2 + x + 1)^n + (x^2 - x + 1)^n

# - Bài Kiểm tra số nguyên tố:
# Xây dựng phương thức kiem_tra_so_nguyen_to(x): x là tham số truyền vào,
# phương thức có giá trị trả về là True nếu x là số nguyên tố, có giá trị trả về là False nếu x không là số nguyên tố

def checkPrime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, x//2 + 1, 2):
        if x % i == 0:
            return False
    return True

def tinh_A(n, x):
    return (x**2 + x + 1) ** n + (x**2 - x + 1) ** n

def tinh_S(n, x):
    return ( x**2 + 1 ) ** n



