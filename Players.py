from microbit import *
import radio
from GameData import Actions
from StackFile import Stack
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
        while True:
            if button_a.was_pressed():
                compteur = (compteur + 1) % 5 #Thx to Yolked.
                display.show(Actions[Matching[compteur]]["Shape"])
                sleep((2000))
            elif button_b.was_pressed():
                display.clear()
                break
        radio.send(f"Player one played:{Matching[compteur]}")
        self.Memory.ToStack(compteur)