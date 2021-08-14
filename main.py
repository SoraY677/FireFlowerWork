from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


from AnimationLib import HanabiAnim


class EditorPanel(BoxLayout):  # ユーザーインタフェースを初期化するクラス
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        HanabiAnim.init(canvas=self.ids['"simulation_canvas"'].canvas, trigger=self.ids['"simulation_start"'])


class EditorApp(App):  # アプリケーションのロジックを記述するクラス
    def build(self):
        return EditorPanel()


EditorApp().run()
