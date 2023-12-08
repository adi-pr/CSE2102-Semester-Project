"""Module providing database function to preform operations to the database."""
from database import Database
from models import Vehicle, Driver, Repair, Mechanic

class VehicleController:
    """Class representing a vehicle controller"""
    @staticmethod
    def write_vehicle_to_database(vehicle_data):
        """Function writing vehicle to database"""
        db = Database()
        vehicle = Vehicle(**vehicle_data)
        db.write_vehicle(vehicle)

class DriverController:
    """Class representing a driver controller"""
    @staticmethod
    def write_driver_to_database(driver_data):
        """Function writing driver to database"""
        db = Database()
        driver = Driver(**driver_data)
        db.write_driver(driver)

class RepairController:
    """Class representing a repair controller"""
    @staticmethod
    def write_repair_to_database(repair_data):
        """Function writing repairs to database"""
        db = Database()
        repair = Repair(**repair_data)
        db.write_repair(repair)

class MechanicController:
    """Class representing a mechanic controller"""
    @staticmethod
    def write_mechanic_to_database(mechanic_data):
        """Function writing a mechanic to database"""
        db = Database()
        mechanic = Mechanic(**mechanic_data)
        db.write_mechanic(mechanic)
