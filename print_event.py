import Global
import event_form
from pickle import GLOBAL
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import Global

class PrintEvent(App):
    def build(self):
        #Runs the app in main.py to get values for variable
        submissionForm = event_form.EventForm()
        submissionForm.run()

        main_layout = BoxLayout(orientation="vertical")
        
        #I want to create an Event object based on input vars
        self.eventName = Label(text=Global.NAME)
        self.eventDate = Label(text=Global.DATE)
        self.eventStartTime = Label(text=Global.STARTTIME)
        self.eventEndTime = Label(text=Global.ENDTIME)
        self.eventLocation = Label(text=Global.LOCATION)
        self.eventDescription = Label(text=Global.DESCRIPTION)
        self.eventContact = Label(text=Global.CONTACT)

        
        main_layout.add_widget(self.eventName)
        main_layout.add_widget(self.eventDate)
        main_layout.add_widget(self.eventStartTime)
        main_layout.add_widget(self.eventEndTime)
        main_layout.add_widget(self.eventLocation)
        main_layout.add_widget(self.eventDescription)
        main_layout.add_widget(self.eventContact)
        

        return main_layout



if __name__ == "__main__":
    app2 = PrintEvent()
    app2.run()