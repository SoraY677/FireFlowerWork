from kivy.clock import Clock

event = None
isEventEnd = True


def startAnim(callbackAnim, interval=0.5):
    global event, isEventEnd
    if isEventEnd:
        # アニメーションを開始する
        event = Clock.schedule_interval(callbackAnim, interval)
        isEventEnd = False


def endAnim():
    global event, isEventEnd
    event.cancel()
    isEventEnd = True
