from tkinter import *
import tkinter as tk

class BetterText:
    def __init__(self, Text : str) -> None:
        """
        Initialse the label by giving its root.
        """
        assert type(Text) == str, "The text must be a string."
        
        self.NewLabel : Label = Label(text = Text)
        return None

    def EditText(self, Width : int, Height : int, Wraplenght : int = 0) -> None:
        """
        Configure the label with the given parameters.
        """
        assert type(Width) == int and type(Height) == int, "The size must be set in integers."
        assert type(Wraplenght) == int, "The wraplenght must be an integer."

        self.NewLabel.config(width = Width,
                             height = Height,
                             wraplength = Wraplenght)
        
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