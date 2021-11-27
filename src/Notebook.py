import tkinter as tk
from tkinter import ttk

class Notebook(ttk.Notebook):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

    def addTab(self, tabName, tab):
        self.add(tab, text=tabName)