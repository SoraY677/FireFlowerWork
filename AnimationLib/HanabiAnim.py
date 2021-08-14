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
    print(_canvas)
    # ボタンを押した際にイベントを発生させる
    _trigger.bind(on_press=_fireTrigger)


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
        Color(0, 0, 0)
        _pointList.append(Rectangle(pos=(300, _counter + 100), size=(5, 5)))

    _counter += 1


def _fireTrigger(_instance):
    Animation.startAnim(_flyHanabi, 0.01)
