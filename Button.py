from tkinter import *
import tkinter as tk

class BetterButton:
    def __init__(self, Root : tk, Text : str, Font : tuple) -> None:
        """
        Create a button using root argument for the root of the button.
        Along with the text you want the button to display and its font.
        """

        assert type(Text) == str, "The text argument must be a string."
        assert type(Font) == tuple, "The Font must be a tuple containing the font and its size."

        self.NewButton : Button = Button(Root, 
                                        text = Text, 
                                        cursor = "star",
                                        font = Font)
        return None
    
    def Enhance(self, UsedColorActive : str, UsedFontActive : tuple, UsedColorIdle : str, UsedFontIdle : tuple) -> None:
        """
        Enhance the button by giving its bidings.
        Used colors must be string hexacode.
        Used fonts must be tuple where the first element is the font as a string and second is the size as an integer.
        """

        assert type(UsedColorActive) == str and type(UsedColorIdle) == str, "The used color must be an hexacode as a string date type."
        assert type(UsedFontActive) == tuple and type(UsedFontIdle) == tuple, "The used font must be a tuple."

        self.NewButton.bind('<Enter>', lambda E : self._OnHover(E, UsedColorActive, UsedFontActive))
        self.NewButton.bind('<Leave>', lambda E : self._OnDefault(E, UsedColorIdle, UsedFontIdle))
        return None
    
    def SetAppearence(self, Background : str, Foreground : str, Border : int = 2) -> None:
        """
        Change the appearance of the button.
        Background and Foreground being the background and foregroud of the button, both must be a str hexacode.
        The active background and foregroud are also set according to the Background and Foreground arguments.
        Border is the border in pixel of the Label, so it should be an integer, as default the border is set to 2 pixels.
        """

        assert type(Background) == str and type(Foreground) == str, "Background and Foreground must be hexacode as strings."
        assert type(Border) == int, "The border must be an integer."

        self.NewButton.config(background = Background,
                              foreground = Foreground,
                              activebackground = Background,
                              activeforeground = Foreground,
                              border = Border)
        return None
    
    def SetSize(self, Width : int, Height : int) -> None:
        """
        Set the size of the button.
        The width and height parameters must be integers.
        """
        assert type(Width) == int and type(Height) == int, "The height and width must be integers."

        self.NewButton.config(width = Width, height = Height)
        return None
    
    def PlaceButton(self, PosX : int, PosY : int, Anchor : str = "center", Relative : bool = False) -> None:
        """
        Place a button at the PosX x position and PosY y position.
        Along with the anchor being one of the base anchor of tkinter, as a string.
        Relative is whether or not the position should be relative to the screen size.
        As default, Anchor is set to center and Relative to False.
        """
        assert type(Relative) == bool, "Relative must be a boolen, I.e True or False."
        assert type(Anchor) == str, "The anchor has to be a string, and one of tkinter's anchor."
        if Relative:
            assert type(PosX) == float and type(PosY) == float, "The relative coordinates must be float between 0 and 1."
            self.NewButton.place(relx = PosX, rely = PosY, anchor = Anchor)
        else:
            assert type(PosX) == int and type(PosY) == int, "The coordinates must be integers."
            self.NewButton.place(x = PosX, y = PosY, anchor = Anchor)
        return None

    def HideButton(self) -> None:
        """
        Hide the button using the place_forget() method.
        """
        self.NewButton.place_forget()
        return None

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
    
