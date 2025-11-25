import serial
from Ui import Ui

ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1) # Create the connection between Card and Pc

print("Reading from micro:bit...") # Debug message

ui = None

#region Instructions
# Don't forget to set the port to micro bit (interpreter(thonny))
# launch Thonny
# put this script : 
# from microbit import *
# while True:
#     if button_a.was_pressed():
#         print("O")
# Restart / stop
# Launch
# Close Thonny
# Run the file in the terminal using python3
#endregion

while True:
    line = ser.readline().decode('utf-8').strip() # Check if anything has been printed 
    if line == "O":
        if ui is None:
            ui = Ui()         # now create the UI
            ui.ShowUi()       # and show it
 