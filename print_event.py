import Global
import event_form
import event_obj
from pickle import GLOBAL
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import Global

class PrintEvent(App):
    def build(self):
        events = []

        #Runs the app in main.py to get values for variable
        submissionForm = event_form.EventForm()
        submissionForm.run()

        main_layout = BoxLayout(orientation="vertical")
        
        #I want to create an Event Object based on input vars
        newEventObj = event_obj.EventObject(Global.NAME, Global.DATE, Global.STARTTIME, Global.ENDTIME, Global.LOCATION, Global.DESCRIPTION, Global.CONTACT)
        events.append(newEventObj)

        #Prompt user if they have another event to input
        addEvent = input("Do you have another event to enter?(y/n)")

        if addEvent.lower() == "y":
            submissionForm.run()

            newEventObj2 = event_obj.EventObject(Global.NAME, Global.DATE, Global.STARTTIME, Global.ENDTIME, Global.LOCATION, Global.DESCRIPTION, Global.CONTACT)
            events.append(newEventObj2)



        for my_event in events:
            main_layout.add_widget(Label(text="Event Name: " + my_event.returnName()))
            main_layout.add_widget(Label(text="Event Date: " + my_event.returnDate()))
            main_layout.add_widget(Label(text="Event Start Time: " + my_event.returnStartTime()))
            main_layout.add_widget(Label(text="Event End Time: " + my_event.returnEndTime()))
            main_layout.add_widget(Label(text="Event Location: " + my_event.returnLocation()))
            main_layout.add_widget(Label(text="Event Description: " + my_event.returnDescription()))
            main_layout.add_widget(Label(text="Event contact #: " + my_event.returnContact()))

        
        return main_layout

if __name__ == "__main__":
    app2 = PrintEvent()
    app2.run()