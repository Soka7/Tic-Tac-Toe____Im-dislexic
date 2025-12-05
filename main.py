from microbit import *
import radio
import music
from StackFile import Stack
from Checkwinner import CheckWinner

radio.on()
radio.config(channel = 83)

PlayerNum = 0

Memory1 = Stack()
Memory2 = Stack()

dico = {}

TwoReps = 0

while True:
    incoming = radio.receive()
    if incoming:
        if incoming[:4] == "Ping":
            display.scroll(incoming)
            PlayerNum += 1
            if Memory1 not in dico.values():
                dico[incoming[-4:]] = Memory1
                Ping1 = incoming[-4:]
            else:
                dico[incoming[-4:]] = Memory2
                Ping2 = incoming[-4:]
            incoming = None
    if PlayerNum == 2:
        for i in range(3):
            TwoReps = 0
            while True:
                if button_b.is_pressed():
                    radio.send(str("Fight !"))
                    display.scroll("Fight !")
                    music.play(music.POWER_DOWN)
                    break
            while True:
                incoming = radio.receive()
                if incoming:
                    if incoming != None:
                        display.scroll(str("ok"))
                        if type(incoming[:4]) != None:
                            incoming = incoming[8:]
                            display.scroll(str("ok"))
                            display.scroll(incoming[:5])
                            display.scroll(incoming[-4:])
                            if incoming[-4:] == Ping1:
                                TwoReps += 1
                                Res1 = incoming[:5]
                                display.scroll(incoming)
                                display.scroll(Res1)
                                RefM1 = dico[incoming[-4:]]
                                dico[incoming[-4:]].ToStack(Res1)
                                display.scroll(str(RefM1._stack))

                            elif incoming[-4:] == Ping2:
                                TwoReps += 1
                                Res2 = incoming[:5]
                                display.scroll(incoming)
                                display.scroll(Res2)
                                RefM2 = dico[incoming[-4:]]
                                dico[incoming[-4:]].ToStack(Res2)
                                display.scroll(str(RefM2._stack))

                            display.scroll(TwoReps)
                            if button_a.is_pressed():
                                if button_b.is_pressed():
                                    TwoReps += 1
                            if TwoReps >1:
                                while True:
                                    if button_a.is_pressed():
                                        display.scroll("ok")
                                        display.scroll(Res1)
                                        display.scroll(Res2)
                                        Winn = CheckWinner(Res1, Res2)
                                        display.scroll(str(Winn))
                                        if Winn == "1: Won !":
                                            RefM1.ToUnStack()
                                            RefM1.ToStack(0)
                                            RefM2.ToUnStack()
                                            RefM2.ToStack(1)
                                        elif Winn == "2: Won !":
                                            RefM2.ToUnStack()
                                            RefM2.ToStack(0)
                                            RefM1.ToUnStack()
                                            RefM1.ToStack(1)
                                        elif Winn == "T: Tie !":
                                            RefM2.ToUnStack()
                                            RefM2.ToStack(0)
                                            RefM1.ToUnStack()
                                            RefM1.ToStack(0)
                                        display.scroll(str(RefM1._stack))
                                        display.scroll(str(RefM2._stack))
                                        break
                                break
                                J1P = 0
                                J2P = 0
                                for points in RefM1._stack:
                                    J1P += points
                                for points in RefM2._stack:
                                    J2P += points
                                display.scroll(J1P)
                                display.scroll(J2P)
                                if J1P > J2P:
                                    display.scroll("J1 wins")
                                else:
                                    display.scroll("J2 wins")
