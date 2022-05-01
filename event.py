from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.eventName = TextInput(
            multiline=False, readonly=False, halign="right", font_size=55
        )
        self.eventTime = TextInput(
            multiline=False, readonly=False, halign="right", font_size=55
        )
        self.eventDescription = TextInput(
            multiline=True, readonly=False, halign="right", font_size=55
        )
        main_layout.add_widget(self.eventName)
        main_layout.add_widget(self.eventTime)
        main_layout.add_widget(self.eventDescription)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.eventName.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.eventName.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.eventName.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.eventName.text
        if text:
            solution = str(eval(self.eventName.text))
            self.eventName.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()