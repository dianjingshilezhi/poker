#比较黑方与白方手牌
def poker(white,black):
    type_white,high_white=analyse(white)
    type_black,high_black=analyse(black)
    if type_black>type_white:
        return 'black-win'
    elif type_white>type_black:
        return 'white-win'
    else:
        if high_black>high_white:
            return 'black-win'
        elif high_white>high_black:
            return 'white-win'
        else:return 'tie'
#分析手牌，返回手牌的类型与最大值
def analyse(pok):
    number={'2':[2,0],'3':[3,0],'4':[4,0],'5':[5,0],'6':[6,0],'7':[7,0],'8':[8,0],'9':[9,0],'10':[10,0],'J':[11,0],'Q':[12,0],'K':[13,0],'A':[14,0]}
    number2 = number
    for i in range(5):
        number2[pok[i][0]][1] = number2[pok[i][0]][1] + 1
    if straight_flush(pok,number):
        return 9, number[pok[4][0]][0]  # 同花顺
    bool,high=four_of_the_kind(pok,number2)
    if bool:
        return 8,high#铁支
    bool,high= Full_house(pok,number2)
    if bool:
        return 7,high#葫芦
    elif flush(pok,number):
        return 6, number[pok[4][0]][0]  # 同花
    elif straight(pok,number):
        return 5, number[pok[4][0]][0]  # 顺子
    bool,high=Three_of_kind(pok,number2)
    if bool:
        return 4,high#三条
    bool,high=two_pair(pok,number2)
    if bool:
        return 3,high   # 双对
    bool,high=one_pair(pok,number2)
    if bool:
        return 2,high  # 一对
    else:return 1,number[pok[4][0]][0]#散牌

def straight_flush(pok,number):
    for i in range(4):
        if not (pok[i][1]==pok[i+1][1] and number[pok[i][0]][0]==number[pok[i+1][0]][0]-1):
            return False
    return True
def four_of_the_kind(pok,number):
    for i in range(5):
        if number[pok[i][0]][1] == 4:
            return True,number[pok[i][0]][0]
    return False,0
def Full_house(pok,number):
    for i in range(5):
        for m in range(5):
            if number[pok[i][0]][1] == 3 and number[pok[m][0]][1] == 2:
                return True,number[pok[i][0]][0]
    return False,0
def flush(pok,number):
    for i in range(4):
        if pok[i][1] != pok[i + 1][1]:
            return False
    return True
def straight(pok,number):
    for i in range(4):
        if number[pok[i][0]][0] != number[pok[i + 1][0]][0] - 1:
            return False
    return True
def Three_of_kind(pok,number):
    for m in range(5):
        if number[pok[m][0]][1] == 3:
            return True,number[pok[m][0]][0]
    return False,0
def two_pair(pok,number):
    for i in range(5):
        for m in range(5):
            if pok[i][0] != pok[m][0] and number[pok[i][0]][1] == 2 and number[pok[m][0]][1] == 2:
                return True,number[pok[m][0]][0]
    return False,0
def one_pair(pok,number):
    for i in range(5):
        if number[pok[i][0]][1] == 2:
            return True,number[pok[i][0]][0]
    return False,0
