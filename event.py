from pickle import GLOBAL
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import Global

class MainApp(App):
    def build(self):
        
        main_layout = BoxLayout(orientation="vertical")
        self.eventName = TextInput(
            multiline=False, readonly=False, halign="center", font_size=55, hint_text="Enter the event name"
        )
        self.eventDate = TextInput(
            multiline=False, readonly=False, halign="center", font_size=55, hint_text="Enter the event date (MM/DD/YYYY)"
        )
        self.eventStartTime = TextInput(
            multiline=False, readonly=False, halign="center", font_size=55, hint_text="Enter the event start time(HH:MM)"
        )
        self.eventEndTime = TextInput(
            multiline=False, readonly=False, halign="center", font_size=55, hint_text="Enter the event end time(HH:MM)"
        )
        self.eventDescription = TextInput(
            multiline=True, readonly=False, halign="center", font_size=55, hint_text="Enter a description for the event"
        )
        self.eventContact = TextInput(
            multiline=False, readonly=False, halign="center", font_size=55, hint_text="Enter a contact number (###-###-####)"
        )
        main_layout.add_widget(self.eventName)
        main_layout.add_widget(self.eventDate)
        main_layout.add_widget(self.eventStartTime)
        main_layout.add_widget(self.eventEndTime)
        main_layout.add_widget(self.eventDescription)
        main_layout.add_widget(self.eventContact)
        

        submit_button = Button(
            text="Submit", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        submit_button.bind(on_press=self.on_submit)

        main_layout.add_widget(submit_button)

        return main_layout

    #on_submit assign all variable values
    def on_submit(self, instance):
        Global.NAME = self.eventName.text
        Global.DATE = self.eventDate.text
        Global.STARTTIME = self.eventStartTime.text
        Global.ENDTIME = self.eventEndTime.text
        Global.DESCRIPTION = self.eventDescription.text
        Global.CONTACT = self.eventContact.text
        
        self.display_event(Global.NAME, Global.DATE, Global.STARTTIME, Global.ENDTIME, Global.DESCRIPTION, Global.CONTACT)
    
    def display_event(self, name, date, start, end, description, contact):
        print(name)
        print(date)
        print(start)
        print(end)
        print(description)
        print(contact)


if __name__ == "__main__":
    app = MainApp()
    app.run()