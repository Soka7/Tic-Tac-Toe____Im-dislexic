from tkinter import *
import tkinter as tk

from StackFile import Stack
from Button import BetterButton
from TextHelper import BetterText
from GameData import Matching
from Checkwinner import CheckWinner
from random import randint

# Error : Need the micro bit import * 
# Solution : Use the reason why Python is slow : MU Editor
# Issues : Tkinter isn't in MU Editor
# Potential Fix : Using Thonny Editor
# Future Issue : The Microbit also need Thonny

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
        self.ComputerChoice : str = ""
        self.PlayerChoice : str = ""

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
        self.Infotext : BetterText = BetterText("In case you did not know, you accessed this page \n by pressing B A B B A successively.", self.BasicFont)

        self.ReqTitle : BetterText = BetterText("Requirements", self.BasicFont)
        self.ReqText : BetterText = BetterText("There are few requirements needed to be able to play. \n Here is a list of them in case you didn't read the ReadMe."
                                               "\n\n 1. You need Tkinter installed system-wide, which you have since \n you are reading this."
                                               "\n You also need the serial module to establish the communication"
                                               "\n\n 2. You need Thonny to run a file to let your card communicate \n with the computer don't"
                                               " forget to choose BBC Microbit \n as your intrepreter."
                                               "\n\n 3. You also need at least 3 MicroBit card (V1) to be able to play."
                                               "\n\n 4. You must use Linux, it might not work on all Distros \n so prefer using the latest version of Xubuntu."
                                               "\n\n 5. You may need some particulars coding skill to do the debug \n of this project for us, you won't get paid.",
                                               self.BasicFont)
        
        self.TryTitle : BetterText = BetterText("Wanna try ?", self.BasicFont)

        self.TryRock : BetterButton = BetterButton(self.Root, " Rock: \n ----- \n -###- \n -###- \n -###- \n ----- ", self.BasicFont)
        self.TryPaper : BetterButton = BetterButton(self.Root, " Paper: \n ----- \n ##### \n ##### \n ##### \n ----- ", self.BasicFont)
        self.TryScissors : BetterButton = BetterButton(self.Root, " Scissors: \n ##--# \n ##-#- \n --#-- \n ##-#- \n ##--# ", self.BasicFont)
        self.TryLizard : BetterButton = BetterButton(self.Root, " Lizard: \n --#-- \n ##-## \n -#-#- \n ##-## \n --#-- ", self.BasicFont)
        self.TrySpock : BetterButton = BetterButton(self.Root, " Spock: \n --### \n -#### \n ###-- \n -#### \n --### ", self.BasicFont)
        self.TryChoice : BetterText = BetterText("", self.BasicFont)

        self.TryResults : BetterText = BetterText("", self.BasicFont)

        self.CreditsTitle : BetterText = BetterText("Credits", self.BasicFont)
        self.Creditstext : BetterText = BetterText("    User Interface : \n Yolked64\n\n"
                                                   "   MicroBit Programming : \n Mostly Soka7 & Hellio Yolked64 helped a bit\n\n"
                                                   "  Communication between card and computer : \n ChatGPT & Yolked64\n\n"
                                                   "  Communication between cards : \n Hellio \n\n"
                                                   "  Supervising : \n M. DALDEGAN",
                                                   self.BasicFont)

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
    
    def _SetPlayerChoice(self, PlayerChoice : str) -> None:
        """
        Set the player choice with a string being its choice.
        """
        self.PlayerChoice = PlayerChoice
        return None
    
    def _ResultsToDisplay(self) -> str:
        """
        Choose the result to display.
        """

        RandomChoice : int = randint(0, 4)
        self.ComputerChoice = Matching[RandomChoice]
        self.TryChoice.EditText("The computer has chosen : " + self.ComputerChoice)

        Results : str = CheckWinner(self.PlayerChoice, self.ComputerChoice)
        TextToDisplay : str = ""

        if Results[0] == "1":
            TextToDisplay = "Stars have lined up and the glory of the victory came. \n You won."
        elif Results[0] == "2":
            TextToDisplay = "Your weakness costed you your fall the computer won."
        elif Results[0] == "T":
            TextToDisplay = "You two were so strong that you ended on a Tie !"
        else:
            TextToDisplay = "You were so strong that we couldn't find the result."

        return TextToDisplay
    
    def _UpdateTry(self, PlayerChoice : str) -> None:
        """
        Update the Demo tab after a button has been pressed.
        """
        self._SetPlayerChoice(PlayerChoice)
        self.TryResults.EditText(self._ResultsToDisplay())
        return None
    
    def _ClearTab(self) -> None:
        """
        Clear all the text from a speficied Tab.
        """
        CurrentTab : str = self.CurrentMenu.ToUnStack()
        if CurrentTab == "Info":
            self.InfoTitle.HideText()
            self.Infotext.HideText()
        elif CurrentTab == "Rules":
            self.RulesText.HideText()
            self.RulesTitle.HideText()
        elif CurrentTab == "Reqs":
            self.ReqTitle.HideText()
            self.ReqText.HideText()
        elif CurrentTab == "Credits":
            self.Creditstext.HideText()
            self.CreditsTitle.HideText()
        elif CurrentTab == "Demo":
            self.TryTitle.HideText()
            self.TryChoice.HideText()
            self.TryResults.HideText()
            self.TryRock.HideButton()
            self.TryPaper.HideButton()
            self.TryScissors.HideButton()
            self.TryLizard.HideButton()
            self.TrySpock.HideButton()
        return None
    
    def _SetCommands(self) -> None:
        """
        Set the commands for all buttons.
        """
        self.RulesButton.NewButton.config(command = self._ShowRules)
        self.InfoButton.NewButton.config(command = self._ShowInfo)
        self.ReqButton.NewButton.config(command = self._ShowReqs)
        self.CreditButton.NewButton.config(command = self._ShowCredits)
        self.TryButton.NewButton.config(command = self._ShowDemo)
        self.TryRock.NewButton.config(command = lambda: self._UpdateTry("Rock"))
        self.TryPaper.NewButton.config(command = lambda: self._UpdateTry("Paper"))
        self.TryScissors.NewButton.config(command = lambda: self._UpdateTry("Scissors"))
        self.TryLizard.NewButton.config(command = lambda: self._UpdateTry("Lizard"))
        self.TrySpock.NewButton.config(command = lambda: self._UpdateTry("Spock"))
        return None
    
    def _ShowDemo(self) -> None:
        """
        Show the Demo Tab.
        """
        self._ClearTab()
        self.CurrentMenu.ToStack("Demo")
        self.TryTitle.PlaceText(0.5, 0.2, "center", True)
        self.TryChoice.PlaceText(0.5, 0.65, "center", True)
        self.TryResults.PlaceText(0.5, 0.75, "center", True)
        self.TryRock.PlaceButton(0.1, 0.4, "center", True)
        self.TryPaper.PlaceButton(0.3, 0.4, "center", True)
        self.TryScissors.PlaceButton(0.5, 0.4, "center", True)
        self.TryLizard.PlaceButton(0.7, 0.4, "center", True)
        self.TrySpock.PlaceButton(0.9, 0.4, "center", True)
        return None

    def _ShowRules(self) -> None:
        """
        Show the rules Tab.
        """
        self._ClearTab()
        self.CurrentMenu.ToStack("Rules")
        self.RulesTitle.PlaceText(0.5, 0.2, "center", True)
        self.RulesText.PlaceText(0.5, 0.55, "center", True)
        return None

    def _ShowInfo(self) -> None:
        """
        Show the informations Tab.
        """
        self._ClearTab()
        self.CurrentMenu.ToStack("Info")
        self.InfoTitle.PlaceText(0.5, 0.2, "center", True)
        self.Infotext.PlaceText(0.5, 0.55, "center", True)
        return None
    
    def _ShowReqs(self) -> None:
        """
        Show the requirements Tab.
        """
        self._ClearTab()
        self.CurrentMenu.ToStack("Reqs")
        self.ReqTitle.PlaceText(0.5, 0.2, "center", True)
        self.ReqText.PlaceText(0.5, 0.6, "center", True)
        return None
    
    def _ShowCredits(self) -> None:
        """
        Show the credits Tab.
        """
        self._ClearTab()
        self.CurrentMenu.ToStack("Credits")
        self.CreditsTitle.PlaceText(0.5, 0.2, "center", True)
        self.Creditstext.PlaceText(0.5, 0.55, "center", True)
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

        self.InfoTitle.DesignText("#161616", "#FFFFFF", ("Courier", 25))
        self.Infotext.DesignText("#161616", "#FFFFFF", self.HoverFont)

        self.ReqButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.ReqButton.Enhance("#FFFFFF", self.HoverFont, "#FFFFFF", self.BasicFont)

        self.ReqTitle.DesignText("#161616", "#FFFFFF", ("Courier", 25))
        self.ReqText.DesignText("#161616", "#FFFFFF", self.HoverFont)

        self.TryButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.TryButton.Enhance("#FFFFFF", self.HoverFont, "#FFFFFF", self.BasicFont)

        self.TryTitle.DesignText("#161616", "#FFFFFF", ("Courier", 25))
        self.TryResults.DesignText("#161616", "#FFFFFF", self.HoverFont)
        self.TryChoice.DesignText("#161616", "#FFFFFF", self.HoverFont)

        self.TryRock.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.TryPaper.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.TryScissors.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.TryLizard.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.TrySpock.SetAppearence("#1A1A1A", "#FFFFFF", 10)

        self.CreditButton.SetAppearence("#1A1A1A", "#FFFFFF", 10)
        self.CreditButton.Enhance("#FFFFFF", self.HoverFont, "#FFFFFF", self.BasicFont)

        self.CreditsTitle.DesignText("#161616", "#FFFFFF", ("Courier", 25))
        self.Creditstext.DesignText("#161616", "#FFFFFF", self.HoverFont)
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