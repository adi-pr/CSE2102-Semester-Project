""" Module providing functions to interact with view """

import sys
import tkinter as tk
from tkinter import *  # pylint: disable=wildcard-import disable=unused-wildcard-import
from tkinter import ttk

# Import Controller & Tabs Class pylint: disable=wrong-import-position
sys.path.append("/home/ruben/Documents/uni/CSE2102/server")
from controllers import Controller

sys.path.append("/home/ruben/Documents/uni/CSE2102/client/components")
from Tabs import Tabs


class Interface:
    """Class to represent the interface"""

    def __init__(self, core):
        self.core = core
        self.core.title("Vehicle Management System")
        self.controller = Controller()
        self.tab_control = ttk.Notebook(core)
        self.tabs = Tabs(self.tab_control, self.controller)
        self.tab_control.pack(expand=1, fill="both")


if __name__ == "__main__":
    root = tk.Tk()
    interface = Interface(root)

    root.mainloop()
