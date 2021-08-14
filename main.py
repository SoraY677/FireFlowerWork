from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class EditorPanel(BoxLayout):  # ユーザーインタフェースを初期化するクラス
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class EditorApp(App):  # アプリケーションのロジックを記述するクラス
    def build(self):
        return EditorPanel()


EditorApp().run()
