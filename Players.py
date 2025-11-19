from microbit import *
import radio
from GameData import Actions
from Stack import Stack
from GameData import Matching

class JoueurC:
    def __init__(self, nom):
        self.nom = nom
        self.Memory = Stack()

    def GetCall(self):
        display.scroll(str("Press A to respond the call"))
        if button_a.was_pressed():
            radio.send(str("Ready for battle"))

    def Play(self):
        compteur = 0
        for _ in range(5):
            if button_a.was_pressed():
                compteur += 1
                display.show(Actions[Matching[compteur]])
                sleep((2000))
            elif button_b.was_pressed():
                display.clear()
                break
        radio.send(f"Player one played:{Matching[compteur]}")
        self.Memory.ToStack(compteur)