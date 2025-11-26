from microbit import *

Input : str = "" # String stocking the player inputs.

while True:
    if button_a.was_pressed(): # If the player pressed a, add A.
        Input += "A"
    if button_b.was_pressed(): # If the player pressed b, add B.
        Input += "B"
    if len(Input) == 5: # Since the combination for the UI is 5 letters long
        print(Input)    # When it's 5 letter long, we print it, it gets read with serial
        Input = Input[1:] # When the input is 5 letters long, replace it with the 5 last letters.
