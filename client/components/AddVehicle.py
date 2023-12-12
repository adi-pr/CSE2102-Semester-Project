# pylint:  disable=invalid-name
""" Module providing functions to interact with view """
from tkinter import ttk

class AddVehicleTab:
    # pylint:  disable=too-few-public-methods
    """Class representing add vehicle tab"""

    def __init__(self, tab_control, controller):
        self.tab = ttk.Frame(tab_control)
        tab_control.add(self.tab, text="Add Vehicle")

        self.labels = [
            "District:",
            "Section:",
            "Insurance Exp:",
            "Fitness Exp:",
            "License Exp:",
            "Fuel Type:",
            "Unladen Weight:",
            "Model:",
            "Make:",
            "Engine ID:",
            "Chassis ID:",
        ]

        self.entries = [ttk.Entry(self.tab) for _ in self.labels]

        for i, labels_text in enumerate(self.labels):
            label = ttk.Label(self.tab, text=labels_text, anchor="e")
            label.grid(row=i, column=0, padx=15, pady=15)
            self.entries[i].grid(row=i, column=1, padx=15, pady=15)

        # Create and place the submit button
        button_commit = ttk.Button(self.tab, text="Add Book", command=self.add_vehicle)
        button_commit.grid(
            row=len(self.labels), column=0, columnspan=2, padx=15, pady=15
        )

    def add_vehicle(self):
        pass
        # Tabs.controller.write_vehicle_to_database()

