"""Module to test database code"""


from database import Database
from controllers import Controller

if __name__ == "__main__":
    # Test data
    vehicle_data = {
        "district": "TestDistrict",
        "section": "TestSection",
        "insurance_exp": "2023-12-31",
        "fitness_exp": "2023-12-31",
        "license_exp": "2023-12-31",
        "vehicle_num": "PRR8494",
        "fuel_type": "TestFuel",
        "unladen_weight": 1500,
        "model": "TestModel",
        "make": "TestMake",
        "engine_id": "TestEngine123",
        "chassis_id": "TestChassis456",
    }

    driver_data = {
        "first_name": "TestFirstName",
        "last_name": "TestLastName",
        "address": "TestAddress",
        "phone_number": 1234567890,
        "department": "TestDepartment",
    }

    repair_data = {
        "price": 75.0,
        "description": "TestRepairDescription",
        "repair_text": "TestRepairText",
    }

    mechanic_data = {
        "name": "TestMechanicName",
        "phone_number": 987654321,
        "address": "TestMechanicAddress",
    }

    # Write test data to the database
    # Controller.write_vehicle_to_database(vehicle_data)
    # Controller.write_driver_to_database(driver_data)
    # Controller.write_repair_to_database(repair_data)
    # Controller.write_mechanic_to_database(mechanic_data)

    # Fetch and print data from the database
    db = Database()

    db.find_vehicle_number("PRR8494")

    # db.cursor.execute("SELECT * FROM vehicle")
    # print("Vehicle Table:")
    # print(db.cursor.fetchall())

    # db.cursor.execute("SELECT * FROM driver")
    # print("\nDriver Table:")
    # print(db.cursor.fetchall())

    # db.cursor.execute("SELECT * FROM repair")
    # print("\nRepair Table:")
    # print(db.cursor.fetchall())

    # db.cursor.execute("SELECT * FROM mechanic")
    # print("\nMechanic Table:")
    # print(db.cursor.fetchall())
