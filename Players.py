from microbit import *
import radio
from GameData import Actions
from Stack import Stack
from GameData import Matching

class JoueurC:
    def __init__(self, nom : str) -> None:
        self.nom : str = nom
        self.Memory : Stack = Stack()
        return None

    def GetCall(self) -> None:
        display.scroll(str("Press A to respond the call"))
        if button_a.was_pressed():
            radio.send(str("Ready for battle"))
        return None

    def Play(self) -> None:
        compteur : int = 0
        sent : bool = False
        while not sent:
            if button_a.was_pressed():
                compteur = (compteur + 1) % 5 
                # Allow the selection to loop, so when you are add the end and press "A" it goes back to the begginning
                display.show(Actions[Matching[compteur]]["Shape"]) 
                sleep((2000))
            elif button_b.was_pressed():
                display.clear()
                sent = True
                break
        radio.send(f"Player one played:{Matching[compteur]}")
        self.Memory.ToStack(compteur)
        return None