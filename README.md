# Stopwatch Feature
This is the branch where I am working on a stopwatch feature for Clock App.

You can start the stopwatch, as well as stop it and reset it back to 0. You can also switch between the 'Clock' screen and the 'Stopwatch' screen.

(<a target="_blank" href="https://icons8.com/icon/2969/settings">Settings</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>)

![stopwatch feature preview](https://user-images.githubusercontent.com/96877426/209838820-00c99fd6-0302-444f-a100-367510ad71d9.gif)



## Change Log

### 28/12/22:

Previously, when the 'Milliseconds' option was toggled, it would only show/hide once the stopwatch has begun or resumed. This has now been fixed; the milliseconds now show/hide even when the stopwatch is paused or not started.

### 28/12/22:

Added option to show or hide the milliseconds.

### 26/12/22:

Added stopwatch time in 'hh:mm:ss' format with leading fractional second.

### 24/12/22:

Fixed an issue where the stopwatch would not reset (and, when pressed, would cause the program to crash when 'Stop' is pressed after).

### 24/12/22:

Branch created and first commit of this branch.

The class 'ClockApp' is no longer a ScreenManager, instead it is a vertical BoxLayout that contains two widgets: a ScreenManager, and another BoxLayout that contains the navigation buttons. This way, the navigation buttons will always remain static no matter the Screen displayed.

