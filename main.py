from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculator(App):
    def build(self):
        self.expression = ""

        root = GridLayout(cols=1, padding=10, spacing=8)

        self.display = TextInput(
            text="",
            readonly=True,
            multiline=False,
            font_size=36,
            halign="right"
        )
        root.add_widget(self.display)

        buttons = [
            ["C","(",")","⌫"],
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            [".","0","%","+"],
            ["="]
        ]

        for row in buttons:
            grid = GridLayout(cols=len(row), spacing=5)
            for txt in row:
                btn = Button(text=txt, font_size=26)
                btn.bind(on_press=self.click)
                grid.add_widget(btn)
            root.add_widget(grid)

        return root

    def click(self, instance):
        t = instance.text

        if t == "C":
            self.expression = ""

        elif t == "⌫":
            self.expression = self.expression[:-1]

        elif t == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Error"

        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += t

        self.display.text = self.expression


if __name__ == "__main__":
    Calculator().run()
