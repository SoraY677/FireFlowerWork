from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
import math

from AnimationLib import HanabiAnim


class EditorPanel(BoxLayout):  # ユーザーインタフェースを初期化するクラス
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout()
        layout = GridLayout(cols=29)
        layout.size_hint = (1, 1)

        buttonlist = []

        for tate in range(0, 29):
            buttonlist.append([])
            for yoko in range(0, 29):
                z = math.sqrt(((14 - tate)**2) + ((14 - yoko)**2))
                if z <= 15:
                    buttonlist[tate].append(Button())
                    layout.add_widget(buttonlist[tate][yoko])
                else:
                    buttonlist[tate].append(None)
                    layout.add_widget(BoxLayout())
        self.ids['"edit_canvas"'].add_widget(layout)

        HanabiAnim.init(canvas=self.ids['"simulation_canvas"'].canvas, trigger=self.ids['"simulation_start"'])


class EditorApp(App):  # アプリケーションのロジックを記述するクラス
    def build(self):
        return EditorPanel()


EditorApp().run()
