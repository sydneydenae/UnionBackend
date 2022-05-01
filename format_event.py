import Global
import event
from pickle import GLOBAL
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import Global

class Format(App):
    def build(self):

        submissionForm = event.MainApp()
        submissionForm.run()

        main_layout = BoxLayout(orientation="vertical")
        
        self.eventContact = TextInput(
            multiline=False, readonly=False, halign="center", font_size=55, hint_text="Enter a contact number (###-###-####)"
        )
        
        main_layout.add_widget(self.eventContact)
        

        return main_layout



if __name__ == "__main__":
    app2 = Format()
    app2.run()