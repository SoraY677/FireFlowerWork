from kivy.clock import Clock


def startAnim(callbackAnim, interval=0.5):
    # アニメーションを開始する
    Clock.schedule_interval(callbackAnim, interval)
