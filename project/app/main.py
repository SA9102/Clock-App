
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.metrics import dp
from datetime import datetime

class ImageButton(ButtonBehavior, Image):
    # Instead of always having a standard button, we can have an image that
    # behaves like a button, which is what this widget is
    pass

class DateText(Label):
    text = 'Hello'

class ClockApp(ScreenManager): 
    # This class is the root of the app/

    # Get local time right now in hours and minutes
    current_time = StringProperty(str(datetime.now().strftime('%H:%M')))

    seconds_on = False
    day_and_month_on = False
    day_of_week_on = False
    year_on = False

    def __init__(self, **kwargs):
        super(ClockApp, self).__init__(**kwargs)
        # Get the current local time every half a second
        Clock.schedule_interval(self.update_time, 0.5)

    def update_time(self, *args):
        # This method gets the current time to be displayed on the screen.
        # The seconds may or may not be retrieved, which depends on the value of
        # 'seconds_on' which the user can toggle in the settings.

        if self.seconds_on:
            self.current_time = str(datetime.now().strftime('%H:%M:%S'))
        else:
            self.current_time = str(datetime.now().strftime('%H:%M'))

    def toggle_seconds(self, instance, seconds_switch_on):
        self.seconds_on = seconds_switch_on

    def toggle_day_and_month(self, instance, day_and_month_switch_on):
        if day_and_month_switch_on:
            self.date_label = Label(text=datetime.now().strftime('%d %b'), pos=(0, dp(-60)))
            self.ids.clock_screen_id.add_widget(self.date_label)
        else:
            self.ids.clock_screen_id.remove_widget(self.date_label)
        self.day_and_month_on = day_and_month_switch_on

class Main(App):
    def build(self):
        return ClockApp()

if __name__ == '__main__':
    Main().run()