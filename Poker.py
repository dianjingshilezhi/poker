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
        else:return 'pie'
#分析手牌，返回手牌的类型与最大值
def analyse(pok):
    number={'2':[2,0],'3':[3,0],'4':[4,0],'5':[5,0],'6':[6,0],'7':[7,0],'8':[8,0],'9':[9,0],'10':[10,0],'J':[11,0],'Q':[12,0],'K':[13,0],'A':[14,0]}
    i=0
    while i<4:
        if pok[i][1]==pok[i+1][1] and number[pok[i][0]][0]==number[pok[i+1][0]][0]-1:
            i=i+1
        else:return
    return 9,number[pok[4][0]][0]
