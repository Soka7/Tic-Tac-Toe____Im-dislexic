from tkinter import *
import tkinter as tk

from Assertions import *

class BetterText:
    def __init__(self, Text : str, Font : tuple) -> None:
        """
        Initialise the label by giving, the Text to display and its Font.
        """
        #region Assertion
        assert IsGoodType(Text, str), "The text argument must be a string."
        assert IsGoodType(Font, tuple) and IsEqual(len(Font), 2), "The Font must be a tuple containing the font and its size."
        assert IsGoodType(Font[0], str) and IsGoodType(Font[1], int), "The tuple must contains a string being the Font-family and its size as an integer."
        assert IsGreater(Font[1], 0), "The size of the font must be a whole number more than 0."
        #endregion
        
        self.NewLabel : Label = Label(text = Text,
                                      font = Font)
        return None

    def EditText(self, Text : str) -> None:
        """
        Edit the Text of the label.
        """
        assert type(Text) == str, "Text must be a string."

        self.NewLabel.config(text = Text)
        return None
        
    def DesignText(self, Background : str, Foreground : str, Font : tuple) -> None:
        """
        Apply a specified Background and Foreground to the text along with a Font.
        Background and Foreground must be hexacode strings.
        Font must be a tuple containing the font and its size.
        """
        #region Assertion
        assert IsGoodType(Background, str) and IsGoodType(Foreground, str), "The Background and Foreground must be strings."
        assert FirstElementEqual(Background[0], "#") and FirstElementEqual(Foreground[0], "#"), "The hexacodes must start with a '#'."
        assert IsEqual(len(Background), 7) and IsEqual(len(Foreground), 7), "The hexacodes must have 7 characters, # and 6 for colors (hexadecimal)."
        assert IsGoodType(Font, tuple) and IsEqual(len(Font), 2), "The font must be a tuple of 2 elements."
        assert IsGoodType(Font[0], str), "The Font-family must be a string."
        assert IsGoodType(Font[1], int) and IsGreater(Font[1], 0), "The size of the Font must be an integer greater than 0."
        #endregion
        self.NewLabel.config(background = Background,
                             foreground = Foreground,
                             font = Font)
        return None

    def PlaceText(self, PosX : int, PosY : int, Anchor : str = "center", Relative : bool = False) -> None:
        """
        Place the Label at the given coordinates.
        PosX and PosY must be integers and the Anchor has to be a string.
        Relative being a toggle to set relative position. Default is False.
        """
        RelPlace : bool = False
        PossiblesAnchors : list = ["nw", "n", "ne", "e", "se", "s", "sw", "w", "center"]
        #region Assertion
        assert IsGoodType(Anchor, str), "The Anchor must be one of these strings: nw, n, ne, e, se, s, sw, w, center"
        assert IsGoodType(Relative, bool), "The Relative argument must be a boolean."
        if Relative:
            assert IsGoodType(PosX, float) and IsGoodType(PosY, float), "The Relative positions must be floats."
            assert IsBetween(0, PosX, 1) and IsBetween(0, PosY, 1), "The Relative positions must be between 0 and 1 included."
            RelPlace = True
        else:
            assert IsGoodType(PosX, int) and IsGoodType(PosY, int), "The positions must be integers."
            assert IsGreater(PosX, -1) and IsGreater(PosY, -1), "The position must be a positive number, avoid putting more than your screen height and width."
        assert Anchor in PossiblesAnchors, "This anchor isn't valid, possibles anchors: nw, n, ne, e, se, s, sw, w, center"
        #endregion
        if RelPlace:
            self.NewLabel.place(relx = PosX,
                                 rely = PosY,
                                 anchor = Anchor)
        else:
            self.NewLabel.place(x = PosX,
                                 y = PosY,
                                 anchor = Anchor)
        return None
    
    def HideText(self) -> None:
        """
        Hide the text using the place_forget() method of tkinter.
        """
        self.NewLabel.place_forget()
        return None