from tkinter import *
import tkinter as tk

from StackFile import Stack
from Button import BetterButton

class Ui:
    def __init__(self) -> None:
        """
        Create the UI.
        """
        self.root = tk.Tk()
        self.CurrentMenu = Stack()

        self.root.geometry('1200x760')
        self.root.title("Helper")
        return None

    def ShowUi(self) -> None:
        """
        Display and place the UI on the screen.
        """
        self.root.mainloop()
        return None
    
ui = Ui()
ui.ShowUi()