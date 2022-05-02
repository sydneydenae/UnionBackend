from turtle import window_width
import Global
import event_form
import event_obj
from pickle import GLOBAL
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import Global

class PrintEvent(App):
    def build(self):
        events = []

        #Creates EventForm object
        submissionForm = event_form.EventForm()
        
        #Layout
        main_layout = GridLayout(cols=1, spacing=100, size_hint_y=None)
        main_layout.bind(minimum_height = main_layout.setter('height'))

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(main_layout)
        

        #Prompt user if they have another event to input
        addEvent = 'y'
        while addEvent.lower() == "y":
            submissionForm.run()
            events.append(event_obj.EventObject(Global.NAME, Global.DATE, Global.STARTTIME, Global.ENDTIME, Global.LOCATION, Global.DESCRIPTION, Global.CONTACT))
            addEvent = input("Do you have another event to enter?(y/n)")

        main_layout.add_widget(Label())
        for my_event in events:
            main_layout.add_widget(Label(text="Event Name: " + my_event.returnName()))
            main_layout.add_widget(Label(text="Event Date: " + my_event.returnDate()))
            main_layout.add_widget(Label(text="Event Start Time: " + my_event.returnStartTime()))
            main_layout.add_widget(Label(text="Event End Time: " + my_event.returnEndTime()))
            main_layout.add_widget(Label(text="Event Location: " + my_event.returnLocation()))
            main_layout.add_widget(Label(text="Event Description: " + my_event.returnDescription()))
            main_layout.add_widget(Label(text="Event contact #: " + my_event.returnContact()))
            main_layout.add_widget(Label())

        
        return root

if __name__ == "__main__":
    app2 = PrintEvent()
    app2.run()