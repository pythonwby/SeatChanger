# SeatImageClass of SeatChanger v1.0.4
# Updated on 2024.6.6

import datetime


class SeatImageClass:
    SeatList = [[33,2,10,41,23,26,48,35,14,49,17,12,15,16,6,34,20,30,3,42,51,45,32,7,40],
                # 靠左列，第五组靠后
                [37,19,11,9,21,24,46,50,47,13,22,31,18,29,4,25,1,28,43,8,39,27,36,5,38]]  # 靠右列，第五组靠前
    SeatListNew = [[0] * 25, [0] * 25]
    NumberToName = ["", "蔡宇轩", "陈锦轩", "陈怡杉", "代宇彤", "丁艺贝", "丁屹城", "丁梓馨", "冯浚", "高千惠",
                    "郭俊雄",
                    "韩呈奕", "华婧朵", "晋熙儿", "冷宣澄", "李欣蔓", "李育涵", "刘瑞琦", "刘雅雯",
                    "刘姿雨", "柳子慧", "罗梓涵", "毛家盼", "毛琳悦", "孟雨禾", "潘志杰", "彭悦", "秦树成", "邱宣博",
                    "宋修仪", "宋雅静", "孙浩涵", "汤文博", "汪君瑜", "王淑涵", "魏晋宇", "魏熠宸",
                    "吴博远", "吴谦益", "夏康洋", "向宏博", "熊梓煊", "徐艺轩", "杨惜婷", "姚熙子正", "易峻熙",
                    "詹晨旺",
                    "张峻豪", "赵艺涵", "周子君", "熊通", "左恩森"]
    SeatImage = [[-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, [-1] * 8, ]
    StartDate = "2024-6-6"

    def __init__(self, SeatListShare):
        self.SeatListShare = SeatListShare
        self.SeatImage[1][0] = 44
        for i in range(2):
            for j in range(25):
                self.SeatListShare[i][j] = self.SeatList[i][j]
        self.ListToImage()

    def UpdateSeatListFromShare(self):
        for i in range(2):
            for j in range(25):
                self.SeatList[i][j] = self.SeatListShare[i][j]
        self.ListToImage()

    def NextWeek(self):
        self.SeatListNew[0][0] = self.SeatList[0][23]
        self.SeatListNew[0][1] = self.SeatList[0][24]
        self.SeatListNew[1][0] = self.SeatList[1][23]
        self.SeatListNew[1][1] = self.SeatList[1][24]
        for i in range(2, 25):
            self.SeatListNew[0][i] = self.SeatList[0][i - 2]
            self.SeatListNew[1][i] = self.SeatList[1][i - 2]

        for i in range(0, 25):
            self.SeatList[0][i] = self.SeatListNew[0][i]
            self.SeatList[1][i] = self.SeatListNew[1][i]

    def LastWeek(self):
        self.SeatListNew[0][23] = self.SeatList[0][0]
        self.SeatListNew[0][24] = self.SeatList[0][1]
        self.SeatListNew[1][23] = self.SeatList[1][0]
        self.SeatListNew[1][24] = self.SeatList[1][1]
        for i in range(0, 23):
            self.SeatListNew[0][i] = self.SeatList[0][i + 2]
            self.SeatListNew[1][i] = self.SeatList[1][i + 2]
        for i in range(0, 25):
            self.SeatList[0][i] = self.SeatListNew[0][i]
            self.SeatList[1][i] = self.SeatListNew[1][i]

    def ListToImage(self):
        for i in range(1, 7):
            self.SeatImage[6][i] = self.SeatList[1][i - 1]
            self.SeatImage[5][i] = self.SeatList[0][i - 1]
        for i in range(0, 8):
            self.SeatImage[4][i] = self.SeatList[1][i + 6]
            self.SeatImage[3][i] = self.SeatList[0][i + 6]
        for i in range(0, 4):
            self.SeatImage[2][i * 2 + 1] = self.SeatList[0][i + 14]
            self.SeatImage[2][i * 2] = self.SeatList[1][i + 14]
        for i in range(0, 7):
            self.SeatImage[1][i + 1] = self.SeatList[1][i + 18]
            self.SeatImage[0][i + 1] = self.SeatList[0][i + 18]

    def PrintImage(self):  # for debug
        for i in range(0, 8):
            for j in range(0, 7):
                if self.SeatImage[j][i] == -1:
                    print('      ', end='')
                    continue
                tmp = self.NumberToName[self.SeatImage[j][i]]
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

    def count_thursdays(self, start_date):
        start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        start = start + datetime.timedelta(days=1)
        end = datetime.datetime.today()
        delta = (end - start).days
        thursdays = 0
        for i in range(delta):
            date = start + datetime.timedelta(i)
            if date.weekday() == 3:
                thursdays += 1
        return thursdays
