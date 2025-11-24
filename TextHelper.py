from tkinter import *
import tkinter as tk

class BetterText:
    def __init__(self, Text : str, Font : tuple) -> None:
        """
        Initialise the label by giving, the text to display and its font.
        """
        assert type(Text) == str, "The Text must be a string."
        assert type(Font) == tuple, "The Font must be a tuple containing the font and its size."
        
        self.NewLabel : Label = Label(text = Text,
                                      font = Font)
        return None

    def EditText(self, Text : str) -> None:
        """
        Edit the Text of the label.
        """
        assert type(Text) == str, "Text must ba string."

        self.NewLabel.config(text = Text)
        return None
        
    def DesignText(self, Background : str, Foreground : str, Font : tuple) -> None:
        """
        Apply a specified background and foreground to the text along with a font.
        Background and Foreground must be hexacode strings.
        Font must be a tuple containing the font and its size.
        """
        self.NewLabel.config(background = Background,
                             foreground = Foreground,
                             font = Font)
        return None

    def PlaceText(self, PosX : int, PosY : int, Anchor : str = "center", Relative : bool = False) -> None:
        """
        Place the text at the given coordinates.
        PosX and PosY must be integers and the anchor has to be s string.
        Relative being a toggle to set relative position. Default is False.
        """
        assert type(Relative) == bool, "Relative must be a boolean I.e True or False."
        assert type(Anchor) == str, "The anchor must be a string and from Tkinter's anchor."
        if Relative:
            assert type(PosX) == float and type(PosY) == float, "The relative size must be a float from 0 to 1."
            self.NewLabel.place(relx = PosX, rely = PosY, anchor = Anchor)
        else:
            assert type(PosX) == int and type(PosY) == int, "Coordinates must be integers."
            self.NewLabel.place(x = PosX, y = PosY, anchor = Anchor)

        return None
    
    def HideText(self) -> None:
        """
        Hide the text using the place_forget() method of tkinter.
        """
        self.NewLabel.place_forget()
        return None