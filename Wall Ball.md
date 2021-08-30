# Pygame

is a cross-platform set of Python modules designed for writing video games.\
It includes computer graphics and sound libraries designed to be used with the Python programming language.

<br/>
<h2 style="color:yellowgreen">sys(system-specific parameters and functions) module</h2>

provides function and variable used to manipulate different parts of the Python runtime environment.

<br/>
<h2 style="color:yellowgreen">moudle index</h2>

| moudle                           | description                                                                                                                                                                                                                                                                                                               | href                                                                                                                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| pygame`.init()`                  | initialize the Pygame library                                                                                                                                                                                                                                                                                             | [the top level pygame package](https://www.pygame.org/docs/ref/pygame.html#pygame.init)                                           |
| `pygame.dispay.Info()`           | create a video display information object ⁝ in FULLSCREEN mode                                                                                                                                                                                                                                                            | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.Info)        |
| `pygame.display.set_mode()`      | initialize a window or screen for display                                                                                                                                                                                                                                                                                 | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode)    |
| `pygame.Color()`                 | color class represents an RGBA color value ranging from 0 to 255 ⁝ allow basic arithmetic operations                                                                                                                                                                                                                      | [pygame object for color representations](https://www.pygame.org/docs/ref/color.html)                                             |
| `pygame.display.set_caption("")` | get the current window caption                                                                                                                                                                                                                                                                                            | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption) |
| `pygame.display.set_icon`        | change the system image for the display window                                                                                                                                                                                                                                                                            | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.set_icon)    |
| ball`.get_rect()`                | get the rectangular area (with the same width and height as the image) of the surface<br/>⁝ pygame use the internally defined surface object to represent all loaded image<br/>⁝ the display always starts at (0, 0), is the top left of the screen. both axes increase positively towards the bottom right of the screen | [pygame object for representing images](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.get_rect)                     |
| `pygame.time.Clock()`            | create an object to help track time                                                                                                                                                                                                                                                                                       | [pygame module for monitoring time](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock)                                  |
| While True                       | limit the while loop during the Python runtime ⁝ ball moves one step per cycle, so control cycle interval to control speed                                                                                                                                                                                                |
| event`.type`                     | event type identifier                                                                                                                                                                                                                                                                                                     | [pygame module for interacting with event handlers](https://www.pygame.org/docs/ref/event.html#pygame.event.EventType)            |
| `sys.exit()`                     | exit the program itself                                                                                                                                                                                                                                                                                                   |                                                                                                                                   |
| event`.key`                      | contain functions for dealing with the keyboard                                                                                                                                                                                                                                                                           | [pygame module to work with the keyboard](https://www.pygame.org/docs/ref/key.html)                                               |
| ballrect`.move(w, h)`            | move the rectangle, of return a new rectangle moved by the given offset<br/>⁝ symbol: direction, numeric: distance                                                                                                                                                                                                        | [pygame object for storing rectangular coordinates](https://www.pygame.org/docs/ref/rect.html#pygame.Rect.move)                   |
| `pygame.display.get_active()`    | return true when the display is active on the screen                                                                                                                                                                                                                                                                      | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.get_active)  |
| `pygame.display.update()`        | update portions of the screen for software displays<br/>⁝ which is faster than .flip( )                                                                                                                                                                                                                                   | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.update)      |
| `pygame.display.flip()`          | update the full display surface to the screen                                                                                                                                                                                                                                                                             | [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.flip)        |
| screen`.fill()`                  | fill surface with a solid color using the RBG color system<br/>⁝ original opsition will be filled with white by default after the movement, so the background color needs to be constantly refreshed                                                                                                                      | [pygame object for representing images](https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill)                         |
| screen`.bilt()`                  | copy the contents of one surface to another, that is, draw src to the dest position                                                                                                                                                                                                                                       | [pygame object for representing images](https://www.pygame.org/docs/ref/surface.html?highlight=blit#pygame.Surface.blit)          |
| fclock`.tick()`                  | get the time in millisecons<br/>⁝ the frame refresh rate per second                                                                                                                                                                                                                                                       |                                                                                                                                   |

<br/>
<h2 style="color:yellowgreen">Pygame syntax</h2>

| syntax   | description                                |
| -------- | ------------------------------------------ |
| def      | define something                           |
| print( ) | display text                               |
| brackets | number of pixels (offset) moving at a time |
| abs( )   | convert to absolute number                 |
| int( )   | convert to an integer                      |

<br/>
<h2 style="color:yellowgreen">attribute of Video display Info</h2>

| attribute | description                                             | attribute | description                                            |
| --------- | ------------------------------------------------------- | --------- | ------------------------------------------------------ |
| current_h | height of the current video mode or of the desktop mode | current_w | width of the current video mode or of the desktop mode |

> formula: vInfo`.attribute`

<br/>
<h2 style="color:yellowgreen">display flag</h2>

| display flag | description                                        | display flag | description                      |
| ------------ | -------------------------------------------------- | ------------ | -------------------------------- |
| FULLSCREEN   | create a fullscreen display                        | RESIZABLE    | create a sizeable display window |
| NOFRAME      | create a display window without border or controls |

> add other exit methods when there is no border

> formula: pygame`.display flag`

href. [pygame module to control the display window and screen](https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode)

<br/>
<h2 style="color:yellowgreen">image function</h2>

| method    | description                                | href                                                                                                   |
| --------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| (" ")     | load new BMP image from a file             | [pygame module for image transfer](https://www.pygame.org/docs/ref/image.html#pygame.image.load_basic) |
| load(" ") | load new image (in gif format) from a file | [pygame module for image transfer](https://www.pygame.org/docs/ref/image.html#pygame.image.load)       |
| save(" ") | save an image to file                      | [pygame module for image transfer](https://www.pygame.org/docs/ref/image.html#pygame.image.save)       |

> format: pygame.image`.method`

<br/>
<h2 style="color:yellowgreen">surface vs. rectangle</h2>

| class   | description                           | class | description                                       |
| ------- | ------------------------------------- | ----- | ------------------------------------------------- |
| Surface | pygame object for representing images | Rect  | pygame object for storing rectangular coordinates |

<br/>
<h2 style="color:yellowgreen">rect class</h2>

| method     | description                                 | method         | description                                      |
| ---------- | ------------------------------------------- | -------------- | ------------------------------------------------ |
| copy       | copy the rectangle                          | unionall       | the union of many rectangles                     |
| move       | move the rectangle                          | unionall_ip    | the union of many rectangles, in place           |
| move_ip    | move the rectangle, in place                | fit            | resize and move a rectangle with aspect ratio    |
| inflate    | grow or shrink the rectangle size           | normalize      | correct negative sizes                           |
| inflate_ip | grow or shrink the rectangle size, in place | contains       | test if one rectangle is inside another          |
| upate      | set the position and size of the rectangle  | collidepoint   | test if a point is inside a rectangle            |
| clamp      | move the rectangle inside another           | colliderect    | test if two rectangles overlap                   |
| clamp_ip   | move the rectangle inside another, in place | dollidelist    | test if one rectangle in a list intersects       |
| clip       | crop a rectangle inside another             | collidelistall | test if all rectangles in a list intersect       |
| clipline   | crop a line inside a rectangle              | collidedict    | test if one rectangle in a dictionary intersects |
| union      | join two rectangles into one                | collidedictall | test if all rectangles in a dictionary intersect |
| uion_ip    | join two rectangles into one, in place      |

> formula: pygame.Rect`.method`

href. [pygame object for storing rectangular coordinates](https://www.pygame.org/docs/ref/rect.html)

<br/>
<h2 style="color:yellowgreen">drawing graphics</h2>

| method  | description            | method  | description                                                 |
| ------- | ---------------------- | ------- | ----------------------------------------------------------- |
| rect    | draw a rectangle       | line    | draw a straight line ⁝ normal (aliased) line                |
| polygon | draw a polygon         | lines   | draw multiple contiguous straight line segments             |
| circle  | draw a circle          | aaline  | draw a straight anti-aliased line                           |
| ellipse | draw an ellipse        | aalines | draw multiple contiguous straight antialiased line segments |
| arc     | draw an elliptical arc |

> formula: pygame.draw`.method`

href. [pygame module for drawing shapes](https://www.pygame.org/docs/ref/draw.html) ⁝ refer to each parameters

<br/>
<h2 style="color:yellowgreen">color object</h2>

| object    | description                                    | object | description                             |
| --------- | ---------------------------------------------- | ------ | --------------------------------------- |
| r         | get or set the red value of the color          | b      | get or set the blue value of the color  |
| g         | get or set the green value of the color        | a      | get or set the alpha value of the color |
| normalize | return the normalized RGBA values of the color |

> formula: pygmae.Color`.object`

href. [pygame object for color representations](https://www.pygame.org/docs/ref/color.html#pygame.Color.r)

<br/>
<h2 style="color:yellowgreen">font class</h2>

| class                    | description                                           |
| ------------------------ | ----------------------------------------------------- |
| pygame`.freetype.Font()` | create a new font instance from a supported font file |

> location: C:\Windows\Fonts\ `font path` \
> extension: _`.ttf`, _`.ttc`

href. [enhanced pygame module for loading and rendering computer fonts](https://www.pygame.org/docs/ref/freetype.html#pygame.freetype.Font) ⁝ refer to the parameters

<br/>
<h2 style="color:yellowgreen">drawing text</h2>

has to write `import pygame.freetype`.\
assigning this parameter will override the setting value in font

| method | description                       | method    | description                          |
| ------ | --------------------------------- | --------- | ------------------------------------ |
| render | return rendered text as a surface | render_to | render text onto an existing surface |

> formula: pygame.freetype.Font`.method`

<br/>
<h2 style="color:yellowgreen">event processing method</h2>

| type                 | command        | description                                                            |
| -------------------- | -------------- | ---------------------------------------------------------------------- |
| handling events      | get( )         | get event from the queue ⁝ the event is deleted after execution        |
| handling events      | poll( )        | get a single event from the queue                                      |
| handling events      | clear( )       | remove all events from the queue                                       |
| operatingevent queue | set_allowed( ) | control which event types are allowed to appear on the event queue     |
| operatingevent queue | set_blocked( ) | control which event types are not allowed to appear on the event queue |
| operatingevent queue | get_blocked( ) | test if a event type is prohibited from the queue                      |
| generating event     | post( )        | place a new event on the queue                                         |
| generating event     | Event( )       | create a new event object                                              |

> formula: pygame.event`.method`

href. [pygame module for interacting with events and queues](https://www.pygame.org/docs/ref/event.html#pygame.event.get)

<br/>
<h2 style="color:yellowgreen">event type</h2>

is pygame class object for representing events

| type     | event           | situation                                           | type               | event         | situation                               |
| -------- | --------------- | --------------------------------------------------- | ------------------ | ------------- | --------------------------------------- |
| system   | QUIT            | click the end game button (close window button)     | joystick           | JOYAXISMOTION | joystick axis is changed                |
| system   | ACTIVEEVENT     | mouse input, off-screen (GUI), or screen activation | joystick           | JOYBALLMOTION | move(rotate) the joystick ball          |
| keyboard | KEYDOWN         | click the keyboard                                  | joystick           | JOYHAMOTION   | joystick hat is changed                 |
| keyboard | KEYUP           | click and detach the keyboard                       | joystick           | JOYBUTTONDOWN | press the joystick button               |
| mouse    | MOUSEMOTION     | move the mouse                                      | joystick           | JOYBUTTONUP   | press and release the joystick button   |
| mouse    | MOUSEBUTTONDOWN | press the mouse button                              | window user defind | VIDEORESIZE   | user resizes window ⁝ in RESIZABLE mode |
| mouse    | MOUSEBUTTONUP   | press and release the mouse button                  | window user defind | USERVENT      | uer randomly sets Events                |

> formula: `event.type` == game`.event`

href. [pygame module for interacting with events and queues](https://www.pygame.org/docs/ref/event.html)

<br/>
<h2 style="color:yellowgreen">attribute for event type</h2>

is set of member attributes based on the type

| event                                        | attribute | decription                                                                                                                   |
| -------------------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| KEYDOWN                                      | unicode   | a single character string that is fully translated ⁝ not recommended. code of the button, platform dependent                 |
| KEYDOWN, KEYUP                               | key       | constant name of the keyboard                                                                                                |
| KEYDOWN, KEYUP                               | mod       | combination value of key modifier                                                                                            |
| MOUSEMOTION, MOUSEBUTTONDOWN , MOUSEBUTTONUP | pos       | the current coordinates of the mouse (x, y), relative to the upper left corner of the window                                 |
| MOUSEMOTION                                  | rel       | the movement distance of the mouse (X, Y), relative to the last event                                                        |
| MOUSEMOTION                                  | buttons   | the state of the mouse button (a, b, c), correspoding to the three mouse buttons                                             |
| MOUSEBUTTONDOWN, MOUSEBUTTONUP               | button    | the values are 1/2/3/4/5, which correspond to left-click, center-click, right-click, scroll up and scroll down, respectively |

> formula: event`.attirbute`

<br/>
<h2 style="color:yellowgreen">TEXTINPUT event</h2>

is represent keyboard keys that refer to the unicode attribute of pygame.KEYDOWN

| constant | description | feature                                        | constant | description | feature                                      |
| -------- | ----------- | ---------------------------------------------- | -------- | ----------- | -------------------------------------------- |
| K_LEFT   | left arrow  | absolute horizontal speed reduced by 1 pixel   | K_UP     | up arrow    | absolute vertical speed increased by 1 pixel |
| K_RIGHT  | right arrow | absolute horizontal speed increased by 1 pixel | K_DOWN   | down arrow  | absolute vertical speed reduced by 1 pixel   |

> formula: `event.key` == pygame`.contant name`

href. [pygame module to work with the keyboard](https://www.pygame.org/docs/ref/key.html)

<br/>
<h2 style="color:yellowgreen">key modifier attribute</h2>

is a bitmask of all the modifier keys that were in a pressed state when the event occurred, and contains the modifier information of the pygame.KEYDOWN and pygame.KEYUP events

| constant name | description                         | constant name | description                   |
| ------------- | ----------------------------------- | ------------- | ----------------------------- |
| KMOD_NONE     | no modifier key pressed             | KMOD_RALT     | right alt                     |
| KMOD_LSHIFT   | left shift                          | KMOD_ALT      | left alt, right alt or both   |
| KMOD_RSHIFT   | right shift                         | KMOD_LMETA    | left meta                     |
| KMOD_SHIFT    | left shif, right shift or both      | KMOD_RMETA    | right meta                    |
| KMOD_LCTRL    | left control                        | KMOD_META     | left meta, right meta or both |
| KMOD_RCTRL    | right control                       | KMOD_CAPS     | caps lock                     |
| KMOD_CTRL     | left control, right control or both | KMOD_NUM      | num lock                      |
| KMOD_LALT     | left alt                            | KMOD_MODE     | AltGr                         |

> formula: event`.mod` = constant | constant ... |

<br/>
<br/>
<h2 style="color:yellow">explain for function and variable</h2>

| variable             | explain                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| speed = [1, 1]       | tuple[number of horizontal axes moving at a sitting, number of vertical axes moving at a sitting] |
| fps = 300            | 300 frames per second                                                                             |
| ballrect.move(speed) | consist of two tuples, speed[0] and speed[1], x-coordinate of 'speed' and y-coordinate of 'speed' |

<br/>
<h2 style="color:yellow">explain for formula</h2>

is description of command directly above

| formula                                                                                            | explain                                                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| speed[0] = speed[0] if speed[0] == 0<br/>else (abs(speed[0]) - 1) \* int(speed[0] / abs(speed[0])) | remain horizontal offset if h.o is 0<br/>else ,when h.o is more/less than 0, h.o minus 1 and remain symbol                                                                                                                                                                             |
| speed[0] = speed[0] + 1 if speed[0] > 0<br/>else speed[0] - 1                                      | h.o plus 1 if h.o is more than 0<br/>else, when h.o is 0 or less than 0, h.o minus 1                                                                                                                                                                                                   |
| event.pos[0] - ballrect.left<br/>, event.pos[1] - ballrect.top                                     | (x-coordinate of the mouse) - (middle-left-coordinate of the current ballrect ⁝ only have x-coordinate)<br/>, (y-coordinate of the mouse) - (middle-top-coordinate of the current ballrect ⁝ only have y-coordinate)<br/>[screen size and coordinates](https://www.jbmpa.com/pygame/4) |
