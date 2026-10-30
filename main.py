from kivy.app import App
from kivy.uix.label import Label

class NeonGFX(App):
    def build(self):
        return Label(
            text="NEON GFX TOOL\nWelcome!",
            font_size=28
        )

NeonGFX().run()
