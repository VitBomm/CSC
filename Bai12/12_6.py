def convertword(a):
    if a == "scissors":
        return "s"
    elif a == "rock":
        return "r"
    else:
        return "p"    

player1 = input("Nhập tên người chơi 1:")
player2 = input("Nhập tên người chơi 2:")
print("Bắt đầu chơi")
while True:
    a = input()
    b = input()
    kq = convertword(a) + convertword(b)

    if kq == "sp" or "rs" or "pr":
        print("Người chiến thắng là %s" % (player1))
    elif kq == "ps" or "sr" or "rp":
        print("Người chiến thắng là %s" % (player2))
    else:
        print("Hòa")
    print("Hai bạn có muốn chơi tiếp hay không ? 1: Có; 0: Không")
    select = int(input())
    if select == 0:
        break
    else:
        continue
