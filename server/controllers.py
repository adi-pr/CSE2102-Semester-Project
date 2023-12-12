"""Module providing database function to preform operations to the database."""
from database import Database
from models import Vehicle, Driver, Repair, Mechanic

db = Database()


class VehicleController:
    """Class representing a vehicle controller"""

    # pylint: disable=too-few-public-methods
    @staticmethod
    def write_vehicle_to_database(vehicle_data):
        """Function writing vehicle to database"""
        vehicle = Vehicle(**vehicle_data)
        db.write_vehicle(vehicle)

    @staticmethod
    def update_vehicle_to_database(vehicle_id, field_name, new_value):
        """Function writing vehicle to database"""
        db.update_vehicle(vehicle_id, field_name, new_value)

    @staticmethod
    def get_repair(vehicle_num):
        """Function to get the repairs done on a vehicle"""
        db.get_vehicle_repairs(vehicle_num)

    @staticmethod
    def get_total_repair_cost(vehicle_num):
        """Function to get the total repair cst of a vehicle"""
        db.calculate_total_repair_cost(vehicle_num)


class DriverController:
    """Class representing a driver controller"""

    # pylint: disable=too-few-public-methods
    @staticmethod
    def write_driver_to_database(driver_data):
        """Function writing driver to database"""
        driver = Driver(**driver_data)
        db.write_driver(driver)


class RepairController:
    """Class representing a repair controller"""

    # pylint: disable=too-few-public-methods
    @staticmethod
    def write_repair_to_database(repair_data):
        """Function writing repairs to database"""
        repair = Repair(**repair_data)
        db.write_repair(repair)


class MechanicController:
    """Class representing a mechanic controller"""

    # pylint: disable=too-few-public-methods
    @staticmethod
    def write_mechanic_to_database(mechanic_data):
        """Function writing a mechanic to database"""
        mechanic = Mechanic(**mechanic_data)
        db.write_mechanic(mechanic)


class Controller(
    VehicleController, DriverController, RepairController, MechanicController
):
    """Class representing a controller for various entities"""
