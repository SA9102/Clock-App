
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

class ClockApp(ScreenManager): 
    # This class is the root of the app/

    # Get local time right now in hours and minutes
    current_time = StringProperty(str(datetime.now().strftime('%H:%M')))

    seconds_on = False
    day_and_month_on = False
    day_of_week_on = False
    year_on = False

    # The date that will be shown on the screen. Initially no date is shown.
    date_label = Label(pos=(0, dp(-60)))

    def __init__(self, **kwargs):
        super(ClockApp, self).__init__(**kwargs)
        # Get the current local time every half a second
        Clock.schedule_interval(self.update_time, 0.5)
        self.ids.clock_screen_id.add_widget(self.date_label)

    def update_time(self, *args):
        # This method gets the current time to be displayed on the screen.
        # The seconds may or may not be retrieved, which depends on the value of
        # 'seconds_on' which the user can toggle in the settings.

        self.current_time = str(datetime.now().strftime('%H:%M' + (':%S' if self.seconds_on else '')))

    def update_screen(self, instance, switch_value, option):
        # Whenever the options relating to the date are toggled, this function will update.
        # Essentially, it uses the date options that are enabled to decided what to display in the main screen.
        # For example, if 'Day of Week' is on, then this will show, otherwise it won't.

        if option == 'seconds':
            self.seconds_on = switch_value
        if option == 'day_+_month':
            self.day_and_month_on = switch_value
        if option == 'day_of_week':
            self.day_of_week_on = switch_value
        if option == 'year':
            self.year_on = switch_value

        self.date_label.text = datetime.now().strftime(('%a ' if self.day_of_week_on else '')
                                                        + ('%d %b ' if self.day_and_month_on else '')
                                                        + ('%Y' if self.year_on else '')).strip()

class Main(App):
    def build(self):
        return ClockApp()

if __name__ == '__main__':
    Main().run()