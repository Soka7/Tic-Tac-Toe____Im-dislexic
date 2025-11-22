from tkinter import *
import tkinter as tk

from StackFile import Stack
from Button import BetterButton

# Reminder to install Nunito (font) and use it on Linux
# Maybe a Class text allowing to easily choose how to place label or just use label, idk

class Ui:
    def __init__(self) -> None:
        """
        Create the UI.
        """
        # Creating window
        self.Root = tk.Tk()
        self.Canvas = tk.Canvas()
        self.CurrentMenu = Stack()
        self.WindowWidth : int = 1200
        self.WindowHeight: int = 760

        # Buttons creation
        self.RulesButton : BetterButton = BetterButton(self.Root, "Rules")
        self.InputButton : BetterButton = BetterButton(self.Root, "Inputs Map")
        self.ReqButton : BetterButton = BetterButton(self.Root, "Requirements")
        self.TryButton : BetterButton = BetterButton(self.Root, "Demo")
        self.CreditButton : BetterButton = BetterButton(self.Root, "Credits")

        # Setting the size of the buttons
        self.RulesButton.SetSize(20, 4)
        self.InputButton.SetSize(20, 4)
        self.ReqButton.SetSize(20, 4)
        self.TryButton.SetSize(20, 4)
        self.CreditButton.SetSize(20, 4)

        # Setting the Style of the buttons
        self.RulesButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.InputButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.ReqButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.TryButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.CreditButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)

        # Root configuration
        self.Root.geometry('1200x760')
        self.Root.title("Helper")
        self.Root.config(background = "#212121")

        # Canvas configuration
        self.Canvas.config(height = 80,
                           width = 1200,
                           background = "#161616",
                           highlightbackground = "#1A1A1A")
        return None
    
    def _ResizeWindow(self, width : int, height : int) -> None:
        """
        Resize the window with a specified width and height.
        The window will appear at center of the screen.
        """
        ScreenWidth : int = self.Root.winfo_screenwidth()
        ScreenHeight : int = self.Root.winfo_screenheight()

        WindowX : float = ScreenWidth / 2 - width / 2
        WindowY : float = ScreenHeight / 2 - height / 2

        self.Root.geometry("%dx%d+%d+%d" % (width, height, WindowX, WindowY))

        return None
    
    def _PlaceAllButtons(self) -> None:
        """
        Place all the buttons.
        """
        self.RulesButton.PlaceButton(int (0.16 * self.WindowWidth / 5), 0, "nw")
        self.InputButton.PlaceButton(int (1.16 * self.WindowWidth / 5), 0, "nw")
        self.ReqButton.PlaceButton(int (2.16 * self.WindowWidth / 5), 0, "nw" )
        self.TryButton.PlaceButton(int (3.16 * self.WindowWidth / 5), 0, "nw")
        self.CreditButton.PlaceButton(int (4.16 * self.WindowWidth / 5), 0, "nw")
        return None

    def ShowUi(self) -> None:
        """
        Display and place the UI on the screen.
        """
        self._ResizeWindow(1200, 760)
        self._PlaceAllButtons()
        self.Canvas.pack()
        self.Root.mainloop()
        return None
    
ui = Ui()
ui.ShowUi()