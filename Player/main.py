from microbit import *
import radio
import music
from players import *

radio.on()
radio.config(channel=83)

Joueur = JoueurC("Joueur")

while True:
    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)
        if incoming == "Call":
            Joueur.GetCall()
        elif incoming == "Fight !":
            display.scroll(incoming)
            Joueur.Play()
    display.clear()
