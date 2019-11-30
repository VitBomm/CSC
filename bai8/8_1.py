def tinh_can(nam):
    dict_can = {
        0: "Canh",
        1: "Tân",
        2: "Nhâm",
        3: "Quý",
        4: "Giáp",
        5: "Ất",
        6: "Bính",
        7: "Đinh",
        8: "Mậu",
        9: "Kỷ",
    }
    return dict_can[nam%10]

def tinh_chi(nam):
    dict_chi = {
        0: "Thân",
        1: "Dậu",
        2: "Tuất",
        3: "Hợi",
        4: "Tý",
        5: "Sửu",
        6: "Dần",
        7: "Mão",
        8: "Thìn",
        9: "Tỵ",
        10: "Ngọ",
        11: "Mùi",
    }
    return dict_chi[nam%12]

nam_duong_lich = int(input())
print(tinh_can(nam_duong_lich),tinh_chi(nam_duong_lich))