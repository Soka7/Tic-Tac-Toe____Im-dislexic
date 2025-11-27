from microbit import *
import radio
import music
from StackFile import Stack

radio.on()
radio.config(channel = 83)

Memory = Stack()

while True:

    if button_a.was_pressed():
        radio.send(str("Call"))
        music.play(music.POWER_UP)
    incoming = radio.receive()
    if incoming:
        if incoming == "Ready":
            display.scroll(incoming)
            if button_b.was_pressed():
                radio.send(str("Fight !"))
                music.play(music.POWER_DOWN)
        elif incoming[18] == "Player one played:":
            display.scroll(incoming)
            Memory.ToStack()
            display.scroll(str(Memory._stack))