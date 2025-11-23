from tkinter import *
import tkinter as tk

from StackFile import Stack
from Button import BetterButton
from TextHelper import BetterText

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
        self.BasicFont : tuple = ("Courier", 19)
        self.HoverFont : tuple = ("Courier", 20)

        # Buttons creation
        self.RulesButton : BetterButton = BetterButton(self.Root, "Rules", self.BasicFont)
        self.InfoButton : BetterButton = BetterButton(self.Root, "Informations", self.BasicFont)
        self.ReqButton : BetterButton = BetterButton(self.Root, "Requirements", self.BasicFont)
        self.TryButton : BetterButton = BetterButton(self.Root, "Demo", self.BasicFont)
        self.CreditButton : BetterButton = BetterButton(self.Root, "Credits", self.BasicFont)

        # Labels creation
        self.RulesTitle : BetterText = BetterText("Rules", self.BasicFont)
        self.RulesText : BetterText = BetterText("1. Rock beats Lizard and Scissors, but get beaten by Paper and Spock.\n\n"
                                                 "2. Lizard beats Spock and Paper, but get beaten by Scissors and Rock.\n\n"
                                                 "3. Spock beats Rock and Scissors, but get beaten by Paper and Lizard.\n\n"
                                                 "4. Scissors beats Paper and Lizard, but get beaten by Rock and Spock.\n\n"
                                                 "5. Paper beats Rock and Spock, but get beaten by Scissors and Lizard.\n\n"
                                                 "6. 'Oh, it's very simple. Scissors cuts paper, paper covers rock, rock \n crushes Lizard,"
                                                 "Lizard poisons Spock, Spock smashes scissors, scissors \n decapitates Lizard, Lizard eats paper,"
                                                 "paper disparoves Spock, Spock \n vaporizes rock, and as it always has, rock crushes scissors.'",
                                                 self.BasicFont)
        self.InfoTitle : BetterText = BetterText("Informations", self.BasicFont)
        self.ReqTitle : BetterText = BetterText("Requirements", self.BasicFont)
        self.TryTitle : BetterText = BetterText("Wanna try ?", self.BasicFont)
        self.CreditsTitle : BetterText = BetterText("Credits", self.BasicFont)

        # Root configuration
        self.Root.geometry('1200x760')
        self.Root.title("Helper")
        self.Root.config(background = "#161616")

        # Canvas configuration
        self.Canvas.config(height = 80,
                           width = 1200,
                           background = "#141414",
                           highlightbackground = "#141414")
        return None
    
    def _ResizeWindow(self, Width : int, Height : int) -> None:
        """
        Resize the window with a specified width and height.
        The window will appear at center of the screen.
        """
        ScreenWidth : int = self.Root.winfo_screenwidth()
        ScreenHeight : int = self.Root.winfo_screenheight()

        WindowX : float = ScreenWidth / 2 - Width / 2
        WindowY : float = ScreenHeight / 2 - Height / 2

        self.Root.geometry("%dx%d+%d+%d" % (Width, Height, WindowX, WindowY))

        return None
    
    def _SetCommands(self) -> None:
        """
        Set the commands for all buttons.
        """
        self.RulesButton.NewButton.config(command = self._ShowRules)

    def _ShowRules(self) -> None:
        """
        Show the rules.
        """
        self.CurrentMenu.ToStack("Rules")
        self.RulesTitle.PlaceText(0.5, 0.2, "center", True)
        self.RulesText.PlaceText(0.5, 0.55, "center", True)
        return None

    def _ResizeWidgets(self) -> None:
        """
        Configure the size of all the widgets of the UI.
        """
        self.RulesButton.SetSize(13, 2)
        self.InfoButton.SetSize(13, 2)
        self.ReqButton.SetSize(13, 2)
        self.TryButton.SetSize(13, 2)
        self.CreditButton.SetSize(13, 2)
        return None
    
    def _DesignWidgets(self) -> None:
        """
        Apply a defined style to all widgets.
        """
        self.RulesText.DesignText("#161616", "#FFFFFF", self.HoverFont)
        self.RulesTitle.DesignText("#161616", "#FFFFFF", ("Courier", 25))
        self.RulesButton.SetAppearence("#161616", "#FFFFFF", 10)
        self.RulesButton.Enhance("#FFFFFF", self.HoverFont, "#FFFFFF", self.BasicFont)
        self.InfoButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.InfoButton.Enhance("#FFFFFF", self.HoverFont, "#FFFFFF", self.BasicFont)
        self.ReqButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.ReqButton.Enhance("#FFFFFF", self.HoverFont, "#FFFFFF", self.BasicFont)
        self.TryButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.TryButton.Enhance("#FFFFFF", self.HoverFont, "#FFFFFF", self.BasicFont)
        self.CreditButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.CreditButton.Enhance("#FFFFFF", self.HoverFont, "#FFFFFF", self.BasicFont)
        return None
    
    def _PlaceWidgets(self) -> None:
        """
        Place all the widgets
        """
        self.RulesButton.PlaceButton(int (0.05 * self.WindowWidth / 5), 0, "nw")
        self.InfoButton.PlaceButton(int (1.05 * self.WindowWidth / 5), 0, "nw")
        self.ReqButton.PlaceButton(int (2.05 * self.WindowWidth / 5), 0, "nw" )
        self.TryButton.PlaceButton(int (3.05 * self.WindowWidth / 5), 0, "nw")
        self.CreditButton.PlaceButton(int (4.05 * self.WindowWidth / 5), 0, "nw")
        return None

    def ShowUi(self) -> None:
        """
        Display and place the UI on the screen.
        """
        self._ResizeWindow(1200, 760)
        self._ResizeWidgets()
        self._DesignWidgets()
        self._PlaceWidgets()
        self._SetCommands()
        self._ShowRules()
        self.Canvas.pack()
        self.Root.mainloop()
        return None
    
ui = Ui()
ui.ShowUi()