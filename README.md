# Stopwatch Feature
This is the branch where I am working on a stopwatch feature for Clock App.

You can start the stopwatch, as well as stop it and reset it back to 0. You can also switch between the 'Clock' screen and the 'Stopwatch' screen.

![stopwatch feature preview](https://user-images.githubusercontent.com/96877426/209566207-e46436ff-59ab-4497-aadb-73a35483b7d2.gif)

![image](https://user-images.githubusercontent.com/96877426/209566382-025e808d-f164-4ade-a15f-c55048bdb592.png)



## Change Log

### 26/12/22:

Added stopwatch time in 'hh:mm:ss' format with leading fractional second.

### 24/12/22:

Fixed an issue where the stopwatch would not reset (and, when pressed, would cause the program to crash when 'Stop' is pressed after).

### 24/12/22:

Branch created and first commit.

The class 'ClockApp' is no longer a ScreenManager, instead it is a vertical BoxLayout that contains two widgets: a ScreenManager, and another BoxLayout that contains the navigation buttons. This way, the navigation buttons will always remain static no matter the Screen displayed.
