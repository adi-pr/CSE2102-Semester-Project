import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk


# Import Controller & Tabs Class
sys.path.append('/home/ruben/Documents/uni/CSE2102/server')
from controllers import Controller

sys.path.append('/home/ruben/Documents/uni/CSE2102/client/components')
from Tabs import Tabs

class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Vehicle Management System")
        
        self.controller = Controller()
        
        self.tab_control = ttk.Notebook(root)
        self.tabs = Tabs(self.tab_control, self.controller) 
        self.tab_control.pack(expand=1, fill="both")

        
if __name__ == "__main__":
    root = tk.Tk()
    interface = Interface(root)

    root.mainloop()
