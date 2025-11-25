from microbit import *

Input : str = "" # String stocking the player inputs

while True:
    if button_a.was_pressed(): # if the player pressed a, add A
        Input += "A"
    if button_b.was_pressed(): # if the player pressed n, add B
        Input += "B"
    if len(Input) == 5: # Since the combination for the UI is 5 letters long
        print(Input)    # When it's 5 letter long, we print it, it gets read with serial
        Input = ""      # if it's the right one the UI shows, and we reset the combination