from microbit import *
import radio
from GameData import Actions
from GameData import Matching
import music

class JoueurC:
    def __init__(self, nom):
        self.nom = nom

    def GetCall(self):
        while True:
            if button_a.is_pressed():
                display.scroll(str("A"))
                display.scroll(str("Ready"))
                radio.send(str("Ready"))
                music.play(music.POWER_UP)
                break

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
        ToSend = str(Matching[compteur])
        radio.send("Player one played: " + ToSend)
