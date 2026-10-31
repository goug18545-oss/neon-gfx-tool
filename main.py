
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.clearcolor = (0.04, 0.05, 0.10, 1)


class NeonGFX(App):

    def build(self):
        root = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        title = Label(
            text="[b]NEON GFX TOOL[/b]",
            markup=True,
            font_size="30sp",
            color=(0, 0.9, 1, 1),
            size_hint_y=0.2
        )

        subtitle = Label(
            text="GAME PERFORMANCE HELPER",
            font_size="14sp",
            color=(0.7, 0.8, 1, 1),
            size_hint_y=0.1
        )

        info = Label(
            text="Welcome to NEON GFX TOOL\n\n"
                 "Choose your game settings\n"
                 "and learn how to improve\n"
                 "your gaming experience.",
            font_size="17sp",
            halign="center"
        )

        button = Button(
            text="DEVICE INFORMATION",
            font_size="18sp",
            size_hint_y=0.18,
            background_color=(0, 0.6, 0.9, 1)
        )

        button.bind(
            on_press=self.show_info
        )

        root.add_widget(title)
        root.add_widget(subtitle)
        root.add_widget(info)
        root.add_widget(button)

        return root

    def show_info(self, instance):
        instance.text = "NEON GFX TOOL READY"


if __name__ == "__main__":
    NeonGFX().run()
      
