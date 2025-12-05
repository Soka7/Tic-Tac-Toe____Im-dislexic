from microbit import *
import radio
import music
from players import *
from random import randint

radio.on()
radio.config(channel=83)

Joueur = JoueurC("Joueur")
Joueur.num = randint(0,10000)

while True:
    radio.send(str("Ping") + str(Joueur.num))
    while True:
        incoming = radio.receive()
        if incoming:
            display.scroll(incoming)
            if incoming == "Fight !":
                display.scroll(incoming)
                Joueur.Play()
        display.clear()
