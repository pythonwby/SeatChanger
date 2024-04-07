import os

SeatList = [[7, 22, 6, 10, 23, 37, 14, 5, 27, 46, 12, 51, 39, 15, 49, 3, 2, 18, 50, 43, 41, 19, 1, 8, 47],
            # 靠左列，第五组靠后
            [29, 30, 48, 25, 34, 31, 36, 33, 16, 45, 11, 35, 28, 32, 21, 13, 24, 38, 20, 4, 42, 17, 26, 9,
             40]]  # 靠右列，第五组靠前
SeatListNew = [[0] * 25, [0] * 25]
NumberToName = ["", "蔡宇轩", "陈锦轩", "陈怡杉", "代宇彤", "丁艺贝", "丁屹城", "丁梓馨", "冯浚", "高千惠", "郭俊雄",
                "韩呈奕", "华婧朵", "晋熙儿", "冷宣澄", "李欣蔓", "李育涵", "刘瑞琦", "刘雅雯",
                "刘姿雨", "柳子慧", "罗梓涵", "毛家盼", "毛琳悦", "孟雨禾", "潘志杰", "彭悦", "秦树成", "邱宣博",
                "宋修仪", "宋雅静", "孙浩涵", "汤文博", "汪君瑜", "王淑涵", "魏晋宇", "魏熠宸",
                "吴博远", "吴谦益", "夏康洋", "向宏博", "熊梓煊", "徐艺轩", "杨惜婷", "姚熙子正", "易峻熙", "詹晨旺",
                "张峻豪", "赵艺涵", "周子君", "熊通", "左恩森"]
SeatImage = [[-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, ]
SeatImage[1][0] = 44
times = int(input('输入计算次数：'))
# def NextWeek():
#     SeatListNew[0][0]=SeatList[0][23]
#     SeatListNew[0][1]=SeatList[0][24]
#     SeatListNew[1][0]=SeatList[1][23]
#     SeatListNew[1][1]=SeatList[1][24]
#     for i in range(2,25):
#         SeatListNew[0][i]=SeatList[0][i-2]
#         SeatListNew[1][i]=SeatList[1][i-2]


# for i in range(1,len(SeatList[0])):
#     print(NumberToName[SeatList[0][i]]+" "+NumberToName[SeatList[1][i]],end="\n")
for k in range(1, times + 1):
    SeatListNew[0][0] = SeatList[0][23]
    SeatListNew[0][1] = SeatList[0][24]
    SeatListNew[1][0] = SeatList[1][23]
    SeatListNew[1][1] = SeatList[1][24]
    for i in range(2, 25):
        SeatListNew[0][i] = SeatList[0][i - 2]
        SeatListNew[1][i] = SeatList[1][i - 2]

    for i in range(0, 25):
        SeatList[0][i] = SeatListNew[0][i]
        SeatList[1][i] = SeatListNew[1][i]

    for i in range(1, 7):
        SeatImage[6][i] = SeatList[1][i - 1]
        SeatImage[5][i] = SeatList[0][i - 1]
    for i in range(0, 8):
        SeatImage[4][i] = SeatList[1][i + 6]
        SeatImage[3][i] = SeatList[0][i + 6]
    for i in range(0, 4):
        SeatImage[2][i * 2 + 1] = SeatList[0][i + 14]
        SeatImage[2][i * 2] = SeatList[1][i + 14]
    for i in range(0, 7):
        SeatImage[1][i + 1] = SeatList[1][i + 18]
        SeatImage[0][i + 1] = SeatList[0][i + 18]

    print(f"{k}周后")
    for i in range(0, 8):
        for j in range(0, 7):
            if SeatImage[j][i] == -1:
                print('      ', end='')
                continue
            tmp = NumberToName[SeatImage[j][i]]
            if tmp == '彭悦':
                tmp = '彭  悦'
            if tmp == '熊通':
                tmp = '熊  通'
            if tmp == '冯浚':
                tmp = '冯  浚'
            if tmp == '姚熙子正':
                tmp1 = "\b\b" + tmp
                tmp = tmp1
            tmp += " "
            print(tmp, end="")
            if j == 1 or j == 4:
                print("|", end="")
        print("\n", end="")
    print('''
------------------------------------------
''')

os.system("pause")