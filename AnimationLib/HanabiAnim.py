import math

from kivy.graphics import Color
from kivy.graphics import Rectangle
import HanabiBall


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


def flyAlgorythm(counter, arr):
    '''
    花火の移動アルゴリズム
    ※宮澤君にお願いしているところ
    '''

    getX = None
    getY = None

    firstStrike = 100
    secondStrike = 300

    # 花火が上昇中
    if(counter < firstStrike):
        dec = counter + 1
        return(
            [{"x": math.cos(math.radians(45 * (counter % 8))) * 2,
              "y": counter * 3,
              "color": (1, 1, 1)}]
        )

    # 　花火が拡散
    elif(counter < secondStrike):
        result = []
        dec = counter - firstStrike
        small = (dec + 1) / 25
        for tate in range(len(arr)):
            for yoko in range(len(arr[tate])):
                if arr[tate][yoko] != None:
                    color = (arr[tate][yoko][0] / small, arr[tate][yoko][1] / small, arr[tate][yoko][2] / small)

                    result.append(
                        {"x": (yoko - 15) * dec / 10,
                         "y": (tate - 15) * dec / 10 + 300,
                         "color": color})

        return result
    # 完全に消えた(アニメーションを停止)
    else:
        Animation.endAnim()
        return None


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
        arr = flyAlgorythm(_counter, HanabiBall.hanabiBall)
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
