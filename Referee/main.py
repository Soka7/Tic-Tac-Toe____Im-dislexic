from microbit import *
import radio
import music
from StackFile import Stack

radio.on()
radio.config(channel = 83)

Memory = Stack()

while True:

    if button_a.is_pressed():
        radio.send(str("Call"))
        music.play(music.POWER_UP)
        while True:
            incoming = radio.receive()
            if incoming:
                if incoming == "Ready":
                    while True:
                        display.scroll(incoming)
                        while True:
                            if button_b.is_pressed():
                                radio.send(str("Fight !"))
                                display.scroll("Fight !")
                                music.play(music.POWER_DOWN)
                elif incoming[18] == "Player one played:":
                    display.scroll(incoming)
                    Memory.ToStack()
                    display.scroll(str(Memory._stack))