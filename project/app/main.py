from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.metrics import dp
from datetime import datetime

class ImageButton(ButtonBehavior, Image):
    # Instead of always having a standard button, we can have an image that
    # behaves like a button, which is what this widget is. This is for the
    # 'settings' button
    pass

class ClockApp(BoxLayout): 
    # This class is the root of the app

    # Get local time right now in hours and minutes
    current_time = StringProperty(str(datetime.now().strftime('%H:%M')))

    seconds_on = False
    day_and_month_on = False
    day_of_week_on = False
    year_on = False

    # The date that will be shown on the screen. Initially no date is shown.
    date_label = Label(pos=(0, dp(-60)))


    # This contains the stopwatch_time in seconds. It is used to get the time in the format 'hh:mm:ss'
    # which will be displayed in the app.
    stopwatch_time = 0
    # This is the variable that will be displayed in the app
    stopwatch_time_displayed = StringProperty('00:00:00.0')
    # True if the time reaches '99:59:59.9'
    stopwatch_time_limit_reached = False
    milliseconds_on = True
    hours = 0
    minutes = 0


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

    def start_stopwatch(self, instance):
        # Start the clock to update the stopwatch every 0.1 seconds

        Clock.schedule_interval(self.update_stopwatch, 0.1)
        self.ids.start_button.disabled = True
        self.ids.stop_button.disabled = False

    def stop_stopwatch(self, instance):
        # Stop the clock to stop the stopwatch

        Clock.unschedule(self.update_stopwatch)
        self.ids.start_button.disabled = False
        self.ids.stop_button.disabled = True

    def reset_stopwatch(self, instance):
        # Reset stopwatch to 0


        self.stopwatch_time = 0
        self.stopwatch_time_displayed = '00:00:00.0'

        # When the reset button is pressed, enable the 'start' button if the stopwatch
        # has reached the limit.
        if self.stopwatch_time_limit_reached:
            self.ids.start_button.disabled = False
            self.stopwatch_time_limit_reached = False

    def update_stopwatch(self, *args):
        # This method is called every 0.1 seconds, so add 0.1 to stopwatch_time
        # every time this method is called


        # Stop the stopwatch when the time reaches '99:59:59.9'
        if self.stopwatch_time < 359999.8:
            self.stopwatch_time += 0.1

            # Get the number of minutes and hours
            # Truncate the time to 1 decimal place.
            self.minutes = int(self.stopwatch_time) // 60
            self.hours = int(self.minutes) // 60
            # Ensure that the time displayed is always in the format 'hh:mm:ss.ms'
            self.stopwatch_time_displayed = ('0' if self.hours < 10 else '') + str(self.hours) + ':' + ('0' if self.minutes % 60 < 10 else '') + str(self.minutes % 60) + ':' + ('0' if self.stopwatch_time % 60 < 10 else '') + (str(float('%.1f'%(self.stopwatch_time % 60))) if self.milliseconds_on else str(int(self.stopwatch_time % 60)))
        # If the stopwatch reached '99:59:59.9'
        else:
            # Stop the clock schedule
            Clock.unschedule(self.update_stopwatch)
            self.ids.stop_button.disabled = True
            self.stopwatch_time_limit_reached = True

    def toggle_milliseconds(self, instance, switch_active):
        # Called when the 'Milliseconds' option is toggled
        # The milliseconds on the stopwatch will be displayed if this option is True

        self.milliseconds_on = switch_active
        # Ensure that the 'millisecond on/off update' happens even when the stopwatch is paused or has not started.
        self.stopwatch_time_displayed = ('0' if self.hours < 10 else '') + str(self.hours) + ':' + ('0' if self.minutes % 60 < 10 else '') + str(self.minutes % 60) + ':' + ('0' if self.stopwatch_time % 60 < 10 else '') + (str(float('%.1f'%(self.stopwatch_time % 60))) if self.milliseconds_on else str(int(self.stopwatch_time % 60)))

class Main(App):
    def build(self):
        return ClockApp()

if __name__ == '__main__':
    Main().run()