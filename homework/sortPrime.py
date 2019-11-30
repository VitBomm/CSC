# sort theo só nguyên tố
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
def get_list_prime(list_temp):
    prime_list = []
    index_list = []
    index = 0
    index_real = 0
    while(index < len(list_temp)):
        if checkPrime(list_temp[index]):
            prime_list.append(list_temp[index])
            index_list.append(index_real)
            del list_temp[index]
            index -= 1
        index += 1
        index_real += 1
    a = sorted(prime_list)
    for i in range(len(index_list)):
        list_temp.insert(index_list[i], a[i])

list_temp = [4,7,8,3,12,13]
get_list_prime(list_temp)
print(list_temp)
# = [4,3,8,7,12,13]