import math
from kivy.graphics import Color

hanabiBall = []


def init():
    # 花火の玉の初期状態を生成
    global hanabiBall
    for tate in range(0, 29):
        hanabiBall.append([])
        for yoko in range(0, 29):
            z = math.sqrt(((14 - tate)**2) + ((14 - yoko)**2))
            if z <= 15:
                hanabiBall[tate].append(None)
            else:
                hanabiBall[tate].append([0, 0, 0])
