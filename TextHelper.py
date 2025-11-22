from tkinter import *
import tkinter as tk

class BetterText:
    def __init__(self, Root : tk, Text : str) -> None:
        """
        Initialse the label by giving its root.
        """
        assert type(Text) == str, "The text must be a string."
        
        self.NewLabel : Label = Label(root = Root)
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

    def PlaceText(self, PosX : int, PosY : int, Anchor : str = "center") -> None:
        """
        Place the text at the given coordinates.
        PosX and PosY must be integers and the anchor has to be s string.
        """

        assert type(PosX) == int and type(PosY) == int, "Coordinates must be integers."
        assert type(Anchor) == str, "The anchor must be a string and from Tkinter's anchor."

        self.NewLabel.place(x = PosX, y = PosY, anchor = Anchor)
        return None