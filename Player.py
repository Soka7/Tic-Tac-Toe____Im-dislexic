from microbit import *
from Joueurs import JoueurC
import radio

radio.on()
radio.config(channel = 83)

Joueur1 = JoueurC("Joueur1")

while True:
    incoming = radio.receive()
    if incoming:
        display.scroll(incoming)
        if incoming == "Awaiting Response":
            Joueur1.GetCall()
        else:
            Joueur1.Play()
        sleep(2000)
    display.clear()