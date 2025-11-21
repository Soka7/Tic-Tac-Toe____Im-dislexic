from tkinter import *
import tkinter as tk

class BetterButton:
    def __init__(self, root : tk) -> None:
        """
        Create a button with the biding already done when the mouse hover it.
        """
        self.NewButton : Button = Button(root, text = "I got created")
        return None
    
    def Enhance(self, UsedColorActive : str, UsedFontActive : tuple, UsedColorIdle : str, UsedFontIdle : tuple) -> None:
        """
        Enhance the button by giving its bidings.
        """
        self.NewButton.bind('<Enter>', lambda e : self._OnHover(e, UsedColorActive, UsedFontActive))
        self.NewButton.bind('<Leave>', lambda e : self._OnDefault(e, UsedColorIdle, UsedFontIdle))
        return None
    
    def PlaceButton(self, PosX : int, PosY : int, anchor : str) -> None:
        """
        Place a button.
        """
        self.NewButton.place(x = PosX, y = PosY, anchor = anchor)
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
    
