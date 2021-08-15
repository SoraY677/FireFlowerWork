from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from functools import partial
import HanabiBall
from kivy.graphics import Color

import math

from AnimationLib import HanabiAnim

_color = [0.2, 0.2, 0.2, 1]


class EditorPanel(BoxLayout):  # ユーザーインタフェースを初期化するクラス
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        HanabiBall.init()
        layout = GridLayout(cols=29)
        layout.size_hint = (1, 1)

        buttonlist = []

        for tate in range(0, 29):
            buttonlist.append([])
            for yoko in range(0, 29):
                z = math.sqrt(((14 - tate)**2) + ((14 - yoko)**2))
                if z <= 15:
                    buttonlist[tate].append(Button())
                    buttonlist[tate][yoko].background_color = [0.2, 0.2, 0.2, 1]

                    def callback(num, instance):
                        global _color
                        instance.background_color = _color
                        HanabiBall.hanabiBall[num[0]][num[1]] = [_color[0], _color[1], _color[2]]
                        print(HanabiBall.hanabiBall[num[0]][num[1]])

                    buttonlist[tate][yoko].bind(on_press=partial(callback, [tate, yoko]))
                    layout.add_widget(buttonlist[tate][yoko])
                else:
                    buttonlist[tate].append(None)
                    layout.add_widget(BoxLayout())
        self.ids['"edit_canvas"'].add_widget(layout)

        HanabiAnim.init(canvas=self.ids['"simulation_canvas"'].canvas, trigger=self.ids['"simulation_start"'])

    def choose_color(self, colornum):
        global _color
        _color = (
            (0.9, 0, 0, 1),
            (0.94, 0.45, 0, 1),
            (1, 0.98, 0, 1),
            (0.58, 0.7, 0.2, 1),
            (0, 0.8, 0.26, 1),
            (0, 0.68, 0.9, 1),
            (0, 0.6, 0.74, 1),
            (0.2, 0.2, 0.7, 1),
            (0.6, 0.08, 0.6, 1),
            (0.8, 0, 0.53, 1),
            (1, 1, 1, 1),
            (0, 0, 0, 1)
        )[colornum - 1]


class EditorApp(App):  # アプリケーションのロジックを記述するクラス
    def build(self):
        return EditorPanel()


EditorApp().run()
