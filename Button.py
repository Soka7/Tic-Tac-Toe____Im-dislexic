from tkinter import *
import tkinter as tk

from Assertions import *

class BetterButton:
    def __init__(self, Root : tk, Text : str, Font : tuple) -> None:
        """
        Create a button using root argument for the root of the button.
        Along with the text you want the button to display and its font.
        Each button has a star cursor when hovering it.
        """
        #region Assertion
        assert IsGoodType(Text, str), "The text argument must be a string."
        assert IsGoodType(Font, tuple) and IsEqual(len(Font), 2), "The Font must be a tuple containing the font and its size."
        assert IsGoodType(Font[0], str) and IsGoodType(Font[1], int), "The tuple must contains a string being the Font-family and its size as an integer."
        assert IsGreater(Font[1], 0), "The size of the font must be a whole number more than 0."
        #endregion

        self.NewButton : Button = Button(Root, 
                                        text = Text, 
                                        cursor = "star",
                                        font = Font)
        return None
    
    def Enhance(self, UsedColorActive : str, UsedFontActive : tuple, UsedColorIdle : str, UsedFontIdle : tuple) -> None:
        """
        Enhance the button by giving its bidings.
        Used colors must be hexacode as string.
        Used fonts must be tuple where the first element is the font as a string and second is the size as an integer.
        """
        #region Assertion
        assert IsGoodType(UsedColorActive, str) and IsGoodType(UsedColorIdle, str), "The used colors must be hexacode put as strings, example #00FF8A"
        assert IsEqual(len(UsedColorActive), 7) and IsEqual(len(UsedColorIdle), 7), "The hexacode must have 6 characters for the color (hexadecimal) and starts with '#'."
        assert FirstElementEqual(UsedColorActive, "#") and FirstElementEqual(UsedColorIdle, "#"), "The hexacode of the colors must start with '#'."
        assert IsGoodType(UsedFontActive, tuple) and IsEqual(len(UsedFontIdle), 2), "The font used when hovering must be a 2 elements tuple. Font-family : string and size : int."
        assert IsGoodType(UsedFontIdle, tuple) and IsEqual(len(UsedFontIdle), 2), "The font used as default must be a 2 elements tuple. Font-family : string and size : int."
        assert IsGoodType(UsedFontActive[0], str) and IsGoodType(UsedFontActive[0], str), "The first element of the tuple must be a string being the Font-family."
        assert IsGoodType(UsedFontActive[1], int) and IsGoodType(UsedFontIdle[1], int), "The second element of the font must be an integer being the size of the font."
        assert IsGreater(UsedFontActive[1], 0) and IsGreater(UsedFontIdle[1], 0), "The size of the font must be a whole number more than 0."
        #endregion
        # Make a small effect when hovering a button.
        self.NewButton.bind('<Enter>', lambda E : self._OnHover(E, UsedColorActive, UsedFontActive))
        self.NewButton.bind('<Leave>', lambda E : self._OnDefault(E, UsedColorIdle, UsedFontIdle))
        return None
    
    def SetAppearence(self, Background : str, Foreground : str, Border : int = 2) -> None:
        """
        Change the appearance of the button.
        Background and Foreground being the background and foregroud of the button, both must be a str hexacode.
        The active background and foreground are also set according to the Background and Foreground arguments.
        Border is the border in pixel of the Label, so it should be an integer, as default the border is set to 2 pixels.
        """
        #region Assertion
        assert IsGoodType(Background, str) and IsGoodType(Foreground, str), "The Background and Foreground must be strings."
        assert FirstElementEqual(Background[0], "#") and FirstElementEqual(Foreground[0], "#"), "The hexacodes must start with a '#'."
        assert IsEqual(len(Background), 7) and IsEqual(len(Foreground), 7), "The hexacodes must have 7 characters, # and 6 for colors (hexadecimal)."
        #endregion

        self.NewButton.config(background = Background,
                              foreground = Foreground,
                              activebackground = Background,
                              activeforeground = Foreground,
                              border = Border)
        return None
    
    def SetSize(self, Width : int, Height : int) -> None:
        """
        Set the size of the button.
        The Width and Height parameters must be integers.
        """
        assert IsGoodType(Width, int) and IsGoodType(Height, int), "The Width and Height must be integers."
        assert IsGreater(Width, 0) and IsGreater(Height, 0), "The Width and Height must be more than 0."

        self.NewButton.config(width = Width,
                              height = Height)
        return None
    
    def PlaceButton(self, PosX : int, PosY : int, Anchor : str = "center", Relative : bool = False) -> None:
        """
        Place a button at the PosX x position and PosY y position.
        Along with the anchor being one of the base anchor of tkinter, as a string.
        Relative is True if the position should be relative to the screen size.
        As default, Anchor is set to center and Relative to False.
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
            self.NewButton.place(relx = PosX,
                                 rely = PosY,
                                 anchor = Anchor)
        else:
            self.NewButton.place(x = PosX,
                                 y = PosY,
                                 anchor = Anchor)

        return None

    def HideButton(self) -> None:
        """
        Hide the button using the place_forget() method from Tkinter.
        """
        self.NewButton.place_forget()
        return None
    #region Helper Methods
    # No assertion needed as they are used only by the previous methods.
    def _OnHover(self, Event, UsedColor : str, UsedFont : tuple) -> None:
        """
        Apply a small animation when the mouse hover a widget.
        """
        Event.widget["foreground"] = UsedColor
        Event.widget["font"] = UsedFont
        return None

    def _OnDefault(self, Event, UsedColor : str, UsedFont : tuple) -> None:
        """
        Apply a small animation when the mouse is no longer hovering a widget.
        """
        Event.widget["foreground"] = UsedColor
        Event.widget["font"] = UsedFont

        return None
    #endregion
    
