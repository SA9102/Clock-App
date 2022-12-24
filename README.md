# Stopwatch Feature
This is the branch where I am working on a stopwatch feature for Clock App.

You can start the stopwatch, as well as stop it and reset it back to 0. You can also switch between the 'Clock' screen and the 'Stopwatch' screen.

![stopwatch feature preview](https://user-images.githubusercontent.com/96877426/209443944-a0ef39f0-0084-4753-80bb-2ca818915cb8.gif)

## Change Log

### 24/12/22:

Fixed an issue where the stopwatch would not reset (and, when pressed, would cause the program to crash when 'Stop' is pressed after).

### 24/12/22:

Branch created and first commit.

The class 'ClockApp' is no longer a ScreenManager, instead it is a vertical BoxLayout that contains two widgets: a ScreenManager, and another BoxLayout that contains the navigation buttons. This way, the navigation buttons will always remain static no matter the Screen displayed.
