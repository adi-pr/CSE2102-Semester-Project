""" Module providing functions to interact with view """
from AddVehicle import AddVehicleTab


class Tabs:
    tab_control = None
    controller = None

    def __init__(self, tab_control, controller):
        Tabs.controller = controller
        Tabs.tab_control = tab_control

        self.add_vehicle_tab = AddVehicleTab(tab_control, controller)
