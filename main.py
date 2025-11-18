from microbit import *
import radio
import music
radio.on()
radio.config(channel = 83)
while True:
    if button_a.was_pressed():
        radio.send(str("Start"))
        music.play(music.POWER_UP)
    if button_b.was_pressed():
        radio.send(str("Fight !"))
        music.play(music.POWER_DOWN)