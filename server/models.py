"""Module providing data classes for representing entities in a database."""
from dataclasses import dataclass


@dataclass
class Vehicle:
    """Class representing a vehicle"""
    # pylint: disable=too-many-instance-attributes
    def __init__(
        self,
        district,
        section,
        insurance_exp,
        fitness_exp,
        license_exp,
        vehicle_num,
        fuel_type,
        unladen_weight,
        model,
        make,
        engine_id,
        chassis_id,
    ):
        # pylint: disable=too-many-arguments
        self.district = district
        self.section = section
        self.insurance_exp = insurance_exp
        self.fitness_exp = fitness_exp
        self.license_exp = license_exp
        self.fuel_type = fuel_type
        self.vehicle_num = vehicle_num
        self.unladen_weight = unladen_weight
        self.model = model
        self.make = make
        self.engine_id = engine_id
        self.chassis_id = chassis_id


@dataclass
class Driver:
    """Class representing a driver"""

    def __init__(self, first_name, last_name, address, phone_number, department):
        # pylint: disable=too-many-arguments
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone_number = phone_number
        self.department = department


@dataclass
class Repair:
    """Class representing the repair"""

    def __init__(self, price, description, repair_text):
        self.price = price
        self.description = description
        self.repair_text = repair_text


@dataclass
class Mechanic:
    """Class representing a mechanic"""

    def __init__(self, name, phone_number, address):
        self.name = name
        self.phone_number = phone_number
        self.address = address
