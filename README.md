# Stopwatch Feature
This is the branch where I am working on a stopwatch feature for Clock App.

You can start the stopwatch, as well as stop it and reset it back to 0. You can also switch between the 'Clock' screen and the 'Stopwatch' screen.


## Change Log

### 24/12/22:

Branch created and first commit.

The class 'ClockApp' is no longer a ScreenManager, instead it is a vertical BoxLayout that contains two widgets: a ScreenManager, and another BoxLayout that contains the navigation buttons. This way, the navigation buttons will always remain static no matter the Screen displayed.
