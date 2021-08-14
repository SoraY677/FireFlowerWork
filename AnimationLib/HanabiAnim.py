import math

from kivy.graphics import Color
from kivy.graphics import Rectangle


from . import Animation

_counter = 0
_canvas = None
_trigger = None


def init(canvas, trigger):
    global _canvas, _trigger
    _canvas = canvas
    _trigger = trigger
    # ボタンを押した際にイベントを発生させる
    _trigger.bind(on_press=_fireTrigger)


_prevPos = {"x": 0, "y": 0}


def flyAlgorythm(counter, length):
    '''
    花火の移動アルゴリズム
    ※宮澤君にお願いしているところ
    '''

    getX = None
    getY = None

    firstStrike = 100
    secondStrike = 200

    # 花火が上昇中
    if(counter < firstStrike):
        def getX(counter, index):
            return math.cos(math.radians(45 * (counter % 8))) * 2

        def getY(counter, index):
            return counter * 3

    # 　花火が拡散
    elif(counter < firstStrike * 2):
        def getX(counter, index):
            return math.cos(math.radians(360 / length * index)) * (counter - firstStrike)

        def getY(counter, index):
            return math.sin(math.radians(360 / length * index)) * (counter - firstStrike) + firstStrike * 3 - (counter / 20) ** 2

    # 完全に消えた(アニメーションを停止)
    else:
        Animation.endAnim()
        return None

    color = 1 - counter % firstStrike / firstStrike
    return [
        {"x": getX(counter, i),
         "y": getY(counter, i),
         "color": (color, color, color)}
        for i in range(0, length)]


_pointList = []


def _flyHanabi(dt):
    '''
    花火を飛ばす処理を連続する
    '''

    global _canvas, _counter, _pointList

    try:
        for point in _pointList:
            _canvas.remove(point)
    except:
        pass
    _pointList = []

    with _canvas:
        arr = flyAlgorythm(_counter, 9)
        if arr != None:
            for item in arr:

                r, g, b = item["color"]
                Color(r, g, b)
                _pointList.append(Rectangle(pos=(item["x"] + 200, item["y"] + 200), size=(5, 5)))
        else:
            _counter = 0
    _counter += 1


def _fireTrigger(_instance):
    Animation.startAnim(_flyHanabi, 0.01)
