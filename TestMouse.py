#This is a program to examine the data sent by the mouse.
#When the mouse is moved, the binary value sent is displayed.
#Move it horizontally and vertically and note how many bytes from the beginning the byte changes.

#With a so-called gaming mouse, the data has this structure.
#| button(8bit) | x-axis(16bit) | y-axis(16bit) | wheel(16bit) |

#For some mouse, the data is structured like this.
#| button(8bit) | unknown(8bit) | x-axis(16bit) | y-axis(16bit) | wheel(16bit) |

#With an ordinary mouse, the data has this structure.
#| button(8bit) | x-axis(8bit) | y-axis(8bit) | wheel(8bit) |

import os

mouse = os.open('/dev/hidraw0', os.O_RDWR | os.O_NONBLOCK)

while True:
    try:
        buf = os.read(mouse, 64)
        print(buf.hex())
    except BlockingIOError:
        pass
    except KeyboardInterrupt:
        os._exit(1)
