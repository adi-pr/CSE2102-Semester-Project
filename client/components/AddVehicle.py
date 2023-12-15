# pylint:  disable=invalid-name
""" Module providing functions to interact with view """
from tkinter import ttk


class AddVehicleTab:
    # pylint:  disable=too-few-public-methods
    """Class representing add vehicle tab"""

    def __init__(self, tab_control, controller):
        self.tab = ttk.Frame(tab_control)
        tab_control.add(self.tab, text="Add Vehicle")
        self.controller = controller

        self.labels = {
            "district": "District:",
            "section": "Section:",
            "insurance_exp": "Insurance Exp yyyy/mm/dd:",
            "fitness_exp": "Fitness Exp yyyy/mm/dd:",
            "license_exp": "License Exp yyyy/mm/dd:",
            "vehicle_num": "Vehicle Number Plate",
            "fuel_type": "Fuel Type:",
            "unladen_weight": "Unladen Weight:",
            "model": "Model:",
            "make": "Make:",
            "engine_id": "Engine ID:",
            "chassis_id": "Chassis ID:",
            "driver_id": "Driver ID",
        }

        self.entries = [ttk.Entry(self.tab) for _ in self.labels]

        # pylint:  disable=unused-variable
        for i, (key, label_text) in enumerate(self.labels.items()):
            label = ttk.Label(self.tab, text=label_text, anchor="e")
            label.grid(row=i, column=0, padx=15, pady=15)
            self.entries[i].grid(row=i, column=1, padx=15, pady=15)

        # Create and place the submit button
        button_commit = ttk.Button(self.tab, text="Add Vehicle", command=self.add_vehicle)
        button_commit.grid(
            row=len(self.labels), column=0, columnspan=2, padx=15, pady=15
        )

    def add_vehicle(self):
        """Function to extract form data and commit to database"""
        form_data = {}

        for key, entry in zip(self.labels.keys(), self.entries):
            form_data[key] = entry.get()

        print(form_data)

        self.controller.write_vehicle_to_database(form_data)
