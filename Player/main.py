from microbit import *
import radio
from players import *

radio.on()
radio.config(channel = 83)

Joueur = JoueurC("Joueur")

while True:
    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)
        if incoming == "Awaiting Response":
            Joueur.GetCall()
        else:
            Joueur.Play()
    display.clear()
