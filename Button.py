from tkinter import *
import tkinter as tk

class BetterButton:
    def __init__(self, root : tk, Text : str) -> None:
        """
        Create a button using root argument for the root of the button.
        Along with the text you want the button to display.
        """

        assert type(Text) == str, "The text argument must be a string."

        self.NewButton : Button = Button(root, text = Text)
        return None
    
    def Enhance(self, UsedColorActive : str, UsedFontActive : tuple, UsedColorIdle : str, UsedFontIdle : tuple) -> None:
        """
        Enhance the button by giving its bidings.
        Used colors must be string hexacode.
        Used fonts must be tuple where the first element is the font as a string and second is the size as an integer.
        """

        assert type(UsedColorActive) == str and type(UsedColorIdle) == str, "The used color must be an hexacode as a string date type."
        assert type(UsedFontActive) == tuple and type(UsedFontIdle) == tuple, "The used font must be a tuple."

        self.NewButton.bind('<Enter>', lambda e : self._OnHover(e, UsedColorActive, UsedFontActive))
        self.NewButton.bind('<Leave>', lambda e : self._OnDefault(e, UsedColorIdle, UsedFontIdle))
        return None
    
    def SetAppearence(self, Background : str, Foreground : str, Border : int) -> None:
        """
        Change the appearance of the button.
        Background and Foreground being the background and foregroud of the button, both must be a str hexacode.
        """

        assert type(Background) == str and type(Foreground) == str, "Background and Foreground must be hexacode as strings."

        self.NewButton.config(background = Background,
                              foreground = Foreground,
                              border = Border)
        return None
    
    def SetSize(self, width : int, height : int) -> None:
        """
        Set the size of the button.
        The width and height parameters must be integers.
        """
        assert type(width) == int and type(height) == int, "The height and width must be integers."

        self.NewButton.config(width = width, height = height)
        return None
    
    def PlaceButton(self, PosX : int, PosY : int, anchor : str) -> None:
        """
        Place a button at the PosX x position and PosY y position.
        Along with the anchor being one of the base anchor of tkinter, as a string.
        """

        assert type(PosX) == int and type(PosY) == int, "The coordinates must be integers."
        assert type(anchor) == str, "The anchor has to be a string, and one of tkinter's anchor."

        self.NewButton.place(x = PosX, y = PosY, anchor = anchor)
        return None

    def HideButton(self) -> None:
        """
        Hide the button using the place_forget() method.
        """
        self.NewButton.place_forget()
        return None

    def _OnHover(self, event, UsedColor : str, UsedFont : tuple) -> None:
        """
        Apply a small animation when the mouse hover a widget.
        """
        event.widget["foreground"] = UsedColor
        event.widget["font"] = UsedFont
        return None

    def _OnDefault(self, event, UsedColor : str, UsedFont : tuple) -> None:
        """
        Apply a small animation when the mouse is no longer hovering a widget.
        """
        event.widget["foreground"] = UsedColor
        event.widget["font"] = UsedFont

        return None
    
