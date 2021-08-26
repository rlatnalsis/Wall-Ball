# Pygame

is a cross-platform set of Python modules designed for writing video games.\
It includes computer graphics and sound libraries designed to be used with the Python programming language.

<br/>
<h2 style="color:yellowgreen">sys(system-specific parameters and functions) module</h2>

provides function and variable used to manipulate different parts of the Python runtime environment.

<br/>
<h2 style="color:yellowgreen">Pygame moudle index</h2>

| moudle                           | description                                                                                                                                                                                                                                                                                                                      | href                                                                                                                              |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| pygame`.init()`                  | initialize the Pygame library                                                                                                                                                                                                                                                                                                    | [the top level pygame package](https://www.pygame.org/docs/ref/pygame.html#pygame.init)                                           |
| `pygame.display.set_mode()`      | initialize a window or screen for display                                                                                                                                                                                                                                                                                        | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode)    |
| `pygame.display.set_caption("")` | get the current window caption                                                                                                                                                                                                                                                                                                   | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption) |
| `pygame.image.load("")`          | load new image in gif format from a file                                                                                                                                                                                                                                                                                         | [pygame module for image transfer](https://www.pygame.org/docs/ref/image.html#pygame.image.load)                                  |
| ball`.get_rect()`                | get the rectangular area (with a width and height the same size as the image) of the surface<br/>⁝ pygame use the internally defined surface object to represent all loaded image<br/>⁝ the display always starts at (0, 0), is the top left of the screen. both axes increase positively towards the bottom right of the screen | [pygame object for representing images](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect)                     |
| `pygame.time.Clock()`            | create an object to help track time                                                                                                                                                                                                                                                                                              | [pygame module for monitoring time](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock)                                  |
| `pygame.event.get()`             | get events from the queue<br/>⁝ the event is deleted after execution                                                                                                                                                                                                                                                             | [pygame module for interacting with events and queues](https://www.pygame.org/docs/ref/event.html#pygame.event.get)               |
| event`.type`                     | event type identifier                                                                                                                                                                                                                                                                                                            | [pygame module for interacting with event handlers](https://www.pygame.org/docs/ref/event.html#pygame.event.EventType)            |
| event`.key`                      | contain functions for dealing with the keyboard                                                                                                                                                                                                                                                                                  | [pygame module to work with the keyboard](https://www.pygame.org/docs/ref/key.html#pygame.key.start_text_input)                   |
| `sys.exit()`                     | exit the program itself                                                                                                                                                                                                                                                                                                          |                                                                                                                                   |
| ballrect`.move()`                | move the rectangle, of return a new rectangle moved by the given offset<br/>⁝ symbol: direction, numeric: distance                                                                                                                                                                                                               | [pygame object for storing rectangular coordinates](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move)                   |
| screen`.fill()`                  | fill surface with a solid color using the RBG color system<br/>⁝ original opsition will be filled with white by default after the movement, so the background color needs to be constantly refreshed                                                                                                                             | [pygame object for representing images](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill)                         |
| screen`.bilt()`                  | copy the contents of one surface to another, that is, draw src to the dest position                                                                                                                                                                                                                                              | [pygame object for representing images](https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit)          |
| `pygame.display.update()`        | update portions of the screen for software displays                                                                                                                                                                                                                                                                              | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.update)      |
| fclock`.tick()`                  | get the time in millisecons<br/>⁝ the frame refresh rate per second                                                                                                                                                                                                                                                              |                                                                                                                                   |

<br/>
<h2 style="color:yellowgreen">Pygame syntax index</h2>

| syntax   | description                                                                                   |
| -------- | --------------------------------------------------------------------------------------------- |
| brackets | represent proportion of the tuples<br/>⁝ contents: number of pixels moving (offset) at a time |
| abs( )   | convert to absolute number                                                                    |
| int( )   | convert to an integer                                                                         |

<br/>
<h2 style="color:yellowgreen">Pygame command index</h2>

| command    | description                                    |
| ---------- | ---------------------------------------------- |
| While True | limit the while loop during the Python runtime |

<br/>
<h2 style="color:yellowgreen">Pygame event index</h2>

| event                                | description                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------- |
| pygame.QUIT                          | occur when you click the end game button (close window button)                  |
| pygame.KEYDOWN                       | occur when you click and detach the keyboard                                    |
| pygame.TEXTINPUT<br/>(pygame.locals) | represent keyboard keys<br/>⁝ prefer to the unicode attribute of pygame.KEYDOWN |

<br/>
<h2 style="color:yellowgreen">Pygame constants from pygame.locals index</h2>

| pygame constant | description | function                                       |
| --------------- | ----------- | ---------------------------------------------- |
| K_LEFT          | down arrow  | absolute horizontal speed reduced by 1 pixel   |
| K_RIGHT         | right arrow | absolute horizontal speed increased by 1 pixel |
| K_UP            | up arrow    | absolute vertical speed increased by 1 pixel   |
| K_DOWN          | down arrow  | absolute vertical speed reduced by 1 pixel     |

href.[pygame module to work with the keyboard](https://www.pygame.org/docs/ref/key.html#pygame.key.start_text_input)
