from microbit import *
from GameData import Matching
from Pile import Pile
from GameData import Actions
import radio
radio.on()

pile = Pile()

while True:
    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)
        sleep(2000)
        compteur = 0
        for i in range(5):
            if button_a.was_pressed():
                compteur += 1
                display.show(Actions["?"])
                sleep((2000))
            elif button_b.was_pressed():
                display.clear()
                break
        radio.send(f"Player one played:{Matching[compteur]}")
        pile.empile(compteur)
    display.clear()