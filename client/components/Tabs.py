""" Module providing functions to interact with view """
from AddVehicle import AddVehicleTab
from AddDriver import AddDriverTab
from AddRepair import AddRepairTab
from AddMechanic import AddMechanicTab


class Tabs:
    """Class representing tabs in view"""
    tab_control = None
    controller = None

    def __init__(self, tab_control, controller):
        Tabs.controller = controller
        Tabs.tab_control = tab_control

        self.add_vehicle_tab = AddVehicleTab(tab_control, controller) 
        self.add_vehicle_tab = AddDriverTab(tab_control, controller) 
        self.add_vehicle_tab = AddRepairTab(tab_control, controller) 
        self.add_vehicle_tab = AddMechanicTab(tab_control, controller) 
