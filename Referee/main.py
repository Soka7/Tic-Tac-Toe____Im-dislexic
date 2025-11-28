from microbit import *
import radio
import music
from StackFile import Stack

radio.on()
radio.config(channel = 83)

PlayerNum = 0

Memory1 = Stack()
Memory2 = Stack()

dico = {}

while True:
    incoming = radio.receive()
    if incoming:
        if incoming[:4] == "Ping":
            display.scroll(incoming)
            PlayerNum += 1
            if Memory1 not in dico.values():
                dico[incoming[4:]] = Memory1
            else:
                dico[incoming[4:]] = Memory2
            incoming = None
    if PlayerNum == 2:
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
                                    break
                            while True:
                                incoming = radio.receive()
                                if incoming:
                                    display.scroll(incoming)
                                    display.scroll(incoming[:7])
                                    if incoming[:7] == "Played:":
                                        display.scroll(incoming)
                                        display.scroll(incoming[8:])
                                        dico[4:].ToStack(incoming[8:])
                                        display.scroll(str(Memory._stack))
