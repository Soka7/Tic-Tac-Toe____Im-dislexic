import serial
from Ui import Ui

class Com:
    def __init__(self) -> None:
        """
        Create the class by creating the connection with the card and pc.
        """
        self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1) # Create the connection between Card and Pc
        self.ui = None
        print("Reading from micro:bit...") # Debug message
        return None
    
    def SpawnUi(self) -> None:
        """
        Check if the UI should appear and make it appear if it should.
        """
        line = self.ser.readline().decode('utf-8').strip() # Check if anything has been printed
        if line == "BABBA":
            if self.ui is None:
                ui = Ui()         # now create the UI
                ui.ShowUi()       # and show it
        return None

#region Instructions
# Don't forget to set the port to micro bit (interpreter(thonny))
# launch Thonny
# put the ThonnyCom.py script in it
# Restart / stop 
# Launch
# Close Thonny
# Run the file in the terminal using python3
#endregion

com = Com()
while True:
    com.SpawnUi()