# Pygame

is a cross-platform set of Python modules designed for writing video games.\
It includes computer graphics and sound libraries designed to be used with the Python programming language.

<br/>
<h2 style="color:yellowgreen">sys(system-specific parameters and functions) module</h2>

provides function and variable used to manipulate different parts of the Python runtime environment.

<br/>
<h2 style="color:yellowgreen">moudle index</h2>

| moudle                           | description                                                                                                                                                                                                                                                                                                                      | href                                                                                                                              |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| pygame`.init()`                  | initialize the Pygame library                                                                                                                                                                                                                                                                                                    | [the top level pygame package](https://www.pygame.org/docs/ref/pygame.html#pygame.init)                                           |
| `pygame.dispay.Info()`           | create a video display information object                                                                                                                                                                                                                                                                                        | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.Info)        |
| `pygame.display.set_mode()`      | initialize a window or screen for display                                                                                                                                                                                                                                                                                        | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode)    |
| `pygame.display.set_caption("")` | get the current window caption                                                                                                                                                                                                                                                                                                   | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption) |
| `pygame.image.load("")`          | load new image in gif format from a file                                                                                                                                                                                                                                                                                         | [pygame module for image transfer](https://www.pygame.org/docs/ref/image.html#pygame.image.load)                                  |
| `pygame.display.set_icon`        | change the system image for the display window                                                                                                                                                                                                                                                                                   | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.set_icon)    |
| ball`.get_rect()`                | get the rectangular area (with a width and height the same size as the image) of the surface<br/>⁝ pygame use the internally defined surface object to represent all loaded image<br/>⁝ the display always starts at (0, 0), is the top left of the screen. both axes increase positively towards the bottom right of the screen | [pygame object for representing images](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect)                     |
| `pygame.time.Clock()`            | create an object to help track time                                                                                                                                                                                                                                                                                              | [pygame module for monitoring time](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock)                                  |
| While True                       | limit the while loop during the Python runtime                                                                                                                                                                                                                                                                                   |
| `pygame.event.get()`             | get events from the queue<br/>⁝ the event is deleted after execution                                                                                                                                                                                                                                                             | [pygame module for interacting with events and queues](https://www.pygame.org/docs/ref/event.html#pygame.event.get)               |
| `sys.exit()`                     | exit the program itself                                                                                                                                                                                                                                                                                                          |                                                                                                                                   |
| event`.type`                     | event type identifier                                                                                                                                                                                                                                                                                                            | [pygame module for interacting with event handlers](https://www.pygame.org/docs/ref/event.html#pygame.event.EventType)            |
| event`.key`                      | contain functions for dealing with the keyboard                                                                                                                                                                                                                                                                                  | [pygame module to work with the keyboard](https://www.pygame.org/docs/ref/key.html)                                               |
| `pygame.display.get_active()`    | return tre when the display is active on the screen                                                                                                                                                                                                                                                                              | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.get_active)  |
| ballrect`.move()`                | move the rectangle, of return a new rectangle moved by the given offset<br/>⁝ symbol: direction, numeric: distance                                                                                                                                                                                                               | [pygame object for storing rectangular coordinates](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move)                   |
| `pygame.display.update()`        | update portions of the screen for software displays<br/>⁝ which is faster than .flip( )                                                                                                                                                                                                                                          | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.update)      |
| `pygame.display.flip()`          | update the full display surface to the screen                                                                                                                                                                                                                                                                                    | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.flip)        |
| screen`.fill()`                  | fill surface with a solid color using the RBG color system<br/>⁝ original opsition will be filled with white by default after the movement, so the background color needs to be constantly refreshed                                                                                                                             | [pygame object for representing images](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill)                         |
| screen`.bilt()`                  | copy the contents of one surface to another, that is, draw src to the dest position                                                                                                                                                                                                                                              | [pygame object for representing images](https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit)          |
| fclock`.tick()`                  | get the time in millisecons<br/>⁝ the frame refresh rate per second                                                                                                                                                                                                                                                              |                                                                                                                                   |

<br/>
<h2 style="color:yellowgreen">Pygame syntax</h2>

| syntax   | description                                                                                   |
| -------- | --------------------------------------------------------------------------------------------- |
| print( ) | display text                                                                                  |
| brackets | represent proportion of the tuples<br/>⁝ contents: number of pixels moving (offset) at a time |
| abs( )   | convert to absolute number                                                                    |
| int( )   | convert to an integer                                                                         |

<br/>
<h2 style="color:yellowgreen">attribute of Video display Info</h2>

| attribute | description                                            | attribute | description                                           |
| --------- | ------------------------------------------------------ | --------- | ----------------------------------------------------- |
| current_h | height of the current video mode or of the destop mode | current_w | width of the current video mode or of the destop mode |

<br/>
<h2 style="color:yellowgreen">display flag</h2>

| display flag | description                                                                      | display flag | description                                                                                         |
| ------------ | -------------------------------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------- |
| FULLSCREEN   | create a fullscreen display<br/>⁝ add other exit methods when there is no border | NOFRAME      | display window will have no border or controls<br/>⁝ add other exit methods when there is no border |
| RESIZABLE    | display window should be sizeable                                                |

> formula: pygame`.display flag`

href. [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode)

<br/>
<h2 style="color:yellowgreen">event processing method</h2>

| type                 | command        | description                                                                                                        | type                 | command        | description                                                                                                            |
| -------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------ | -------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| handling events      | get( )         | get event from the queue                                                                                           | operatingevent queue | set_blocked( ) | control which events are allowed on the queue<br/>⁝ the given event types are not allowed to appear on the event queue |
| handling events      | poll( )        | get a single event from the queue                                                                                  | operatingevent queue | get_blocked( ) | test if a type of event is blocked from the queue                                                                      |
| handling events      | clear( )       | remove all events from the queue                                                                                   | generating event     | post( )        | place a new event on the queue                                                                                         |
| operatingevent queue | set_allowed( ) | control which events are allowed on the queue<br/>⁝ the given event types are allowed to appear on the event queue | generating event     | Event( )       | create a new event object                                                                                              |

> formula: pygame.event`.method`

href. [pygame module for interacting with events and queues](https://www.pygame.org/docs/ref/event.html#pygame.event.get)
<br/>

| class     | description                           |
| --------- | ------------------------------------- |
| EventType | pygame object for representing events |

<br/>
<h2 style="color:yellowgreen">event type</h2>

| type     | event           | situation                                                          | type               | event         | situation                               |
| -------- | --------------- | ------------------------------------------------------------------ | ------------------ | ------------- | --------------------------------------- |
| system   | QUIT            | click the end game button (close window button)                    | joystick           | JOYAXISMOTION | joystick axis is changed                |
| system   | ACTIVEEVENT     | mouse enters, leaves the screen (GUI), or screen activation status | joystick           | JOYBALLMOTION | joystick ball moves(rotates)            |
| keyboard | KEYDOWN         | click the keyboard                                                 | joystick           | JOYHAMOTION   | joystick hat is changed                 |
| keyboard | KEYUP           | click and detach the keyboard                                      | joystick           | JOYBUTTONDOWN | joystick button is pressed              |
| mouse    | MOUSEMOTION     | mouse moves                                                        | joystick           | JOYBUTTONUP   | joystick button is pressed and released |
| mouse    | MOUSEBUTTONDOWN | mouse button is pressed                                            | window user defind | VIDEORESIZE   | user resizes window                     |
| mouse    | MOUSEBUTTONUP   | mouse button is pressed and released                               | window user defind | USERVENT      | Events randomly set by the user         |

> formula: pygame.event == game`.event`

href. [pygame module for interacting with events and queues](https://www.pygame.org/docs/ref/event.html)

br/>

<h2 style="color:yellowgreen">attribute for event type</h2>

is set of member attributes based on the type

| event                                        | attribute | decription                                                                                  |
| -------------------------------------------- | --------- | ------------------------------------------------------------------------------------------- |
| KEYDOWN                                      | unicode   | not recommended. code of the button, platform dependent                                     |
| KEYDOWN, KEYUP                               | key       | constant name of the button                                                                 |
| KEYDOWN, KEYUP                               | mod       | combination value of key modifier                                                           |
| MOUSEMOTION, MOUSEBUTTONDOWN , MOUSEBUTTONUP | pos       | the current corrdinates of the mouse (x y), relative to the upper left corner of the window |
| MOUSEMOTION                                  | rel       | the relative movement distance of the mouse (X, Y), relative to the last event              |
| MOUSEMOTION                                  | buttons   | the state of the mouse button (a, b, c), correspoding to the three mouse buttons            |
| MOUSEBUTTONDOWN, MOUSEBUTTONUP               | button    | the value is 0/1/2, correspoding to three keys respectively                                 |

> formula: event`.attirbute`

<br/>
<h2 style="color:yellowgreen">attribute for pygame.event queue</h2>

is additional attributes of pygame.KEYDOWN, pygame.KEYUP event

| attribute   | description                                          | attribute   | description                                                                            |
| ----------- | ---------------------------------------------------- | ----------- | -------------------------------------------------------------------------------------- |
| event`.key` | an integer ID representing every key on the keyboard | event`.mod` | a bitmask of all the modifier keys that were in a pressed state when the event occured |

<br/>
is additional attributes of pygame.KEYDOWN event

| attribute       | description                                                                                                                      |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| event`.unicode` | a single character string that is the fully translated character entered, this takes into account the shift and composition keys |

<br/>
<h2 style="color:yellowgreen">TEXTINPUT event</h2>

is represent keyboard keys that refer to the unicode attribute of pygame.KEYDOWN

| constant name | description | feature                                        | constant name | description | feature                                      |
| ------------- | ----------- | ---------------------------------------------- | ------------- | ----------- | -------------------------------------------- |
| K_LEFT        | down arrow  | absolute horizontal speed reduced by 1 pixel   | K_UP          | up arrow    | absolute vertical speed increased by 1 pixel |
| K_RIGHT       | right arrow | absolute horizontal speed increased by 1 pixel | K_DOWN        | down arrow  | absolute vertical speed reduced by 1 pixel   |

> formula: event.key == pygame`.contant`

href. [pygame module to work with the keyboard](https://www.pygame.org/docs/ref/key.html)

<br/>
<h2 style="color:yellowgreen">key modifier attribute</h2>

is a bitmask of all the modifier keys that were in a pressed state when the event occurred, and contains the modifier information of the pygame.KEYDOWN and pygame.KEYUP events

| constant name | description                      | constant name | description                           | constant name | description                   | constant name | description                     |
| ------------- | -------------------------------- | ------------- | ------------------------------------- | ------------- | ----------------------------- | ------------- | ------------------------------- |
| KMOD_NONE     | no modifier keys pressed         | KMOD_LCTRL    | left control                          | KMOD_RALT     | right alt                     | KMOD_META     | left meta or right meta or both |
| KMOD_LSHIFT   | left shift                       | KMOD_RCTRL    | right control                         | KMOD_ALT      | left alt or right alt or both | KMOD_CAPS     | caps lock                       |
| KMOD_RSHIFT   | right shift                      | KMOD_CTRL     | left control or right control or both | KMOD_LMETA    | left meta                     | KMOD_NUM      | num lock                        |
| KMOD_SHIFT    | left shif or right shift or both | KMOD_LALT     | left alt                              | KMOD_RMETA    | right meta                    | KMOD_MODE     | AltGr                           |

> event`.mod` = constant | constant ...

<br/>
<br/>
<h2 style="color:yellow">explain for function and variable</h2>

| variable             | explain                                                   | contents                                                                                          |
| -------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| speed = [1, 1]       | each number of axes moving at a sitting                   | tuple[number of horizontal axes moving at a sitting, number of vertical axes moving at a sitting] |
| fps = 300            | frames per second                                         |
| ballrect.move(speed) | 'speed' has two tuples, so .move() consists of two tuples | speed[0], speed[1]                                                                                |

<br/>
<h2 style="color:yellow">explain for formula</h2>

| formula                                                                                            | explain                                                                                                    |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| speed[0] = speed[0] if speed[0] == 0<br/>else (abs(speed[0]) - 1) \* int(speed[0] / abs(speed[0])) | remain horizontal offset if h.o is 0<br/>else ,when h.o is more/less than 0, h.o minus 1 and remain symbol |
| speed[0] = speed[0] + 1 if speed[0] > 0<br/>else speed[0] - 1                                      | h.o plus 1 if h.o is more than 0<br/>else, when h.o is 0 or less than 0, h.o minus 1                       |
