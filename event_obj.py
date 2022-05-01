import Global
import event_form
from pickle import GLOBAL
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import Global

class EventObject():
    def __init__(self, eventName, eventDate, startTime, endTime, location, description, contact):
        self.eventName = eventName
        self.eventDate = eventDate
        self.eventStartTime = startTime
        self.eventEndTime = endTime
        self.eventLocation = location
        self.eventDescription = description
        self.eventContact = contact

    def returnName(self):
        return self.eventName

    def returnDate(self):
        return self.eventDate

    def returnStartTime(self):
        return self.eventStartTime

    def returnEndTime(self):
        return self.eventEndTime

    def returnLocation(self):
        return self.eventLocation

    def returnDescription(self):
        return self.eventDescription

    def returnContact(self):
        return self.eventContact

