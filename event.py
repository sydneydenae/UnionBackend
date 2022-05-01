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
            multiline=False, readonly=False, halign="center", font_size=55, text="Enter the event name"
        )
        self.eventDate = TextInput(
            multiline=False, readonly=False, halign="center", font_size=55, text="Enter the event date (MM/DD/YYYY)"
        )
        self.eventStartTime = TextInput(
            multiline=False, readonly=False, halign="center", font_size=55, text="Enter the event start time(HH:MM)"
        )
        self.eventEndTime = TextInput(
            multiline=False, readonly=False, halign="center", font_size=55, text="Enter the event end time(HH:MM)"
        )
        self.eventDescription = TextInput(
            multiline=True, readonly=False, halign="center", font_size=55, text="Enter a description for the event"
        )
        self.eventContact = TextInput(
            multiline=False, readonly=False, halign="center", font_size=55, text="Enter a contact number (###-###-####)"
        )
        main_layout.add_widget(self.eventName)
        main_layout.add_widget(self.eventDate)
        main_layout.add_widget(self.eventStartTime)
        main_layout.add_widget(self.eventEndTime)
        main_layout.add_widget(self.eventDescription)
        main_layout.add_widget(self.eventContact)
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
        equals_button.bind(on_press=self.on_submit)
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

    #def displayEvent(self, name, date, start, end, description, contact):
    #   pass;

    #on_submit assign all variable values
    def on_submit(self, instance):
        inputEN = self.eventName.text
        inputED = self.eventDate.text
        inputST = self.eventStartTime.text
        inputET = self.eventEndTime.text
        inputEDes = self.eventDescription.text
        inputEC = self.eventContact.text

       #displayEvent(inputEN, inputED, inputST, inputET, inputEDes, inputEC)

    




        
        


if __name__ == "__main__":
    app = MainApp()
    app.run()