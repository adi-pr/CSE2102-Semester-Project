from database import Database
from controllers import VehicleController, DriverController, RepairController, MechanicController

if __name__ == "__main__":
    # Test data
    vehicle_data = {
        "district": "TestDistrict",
        "section": "TestSection",
        "insurance_exp": "2023-12-31",
        "fitness_exp": "2023-12-31",
        "license_exp": "2023-12-31",
        "fuel_type": "TestFuel",
        "unladen_weight": 1500,
        "model": "TestModel",
        "make": "TestMake",
        "engine_id": "TestEngine123",
        "chassis_id": "TestChassis456"
    }

    driver_data = {
        "first_name": "TestFirstName",
        "last_name": "TestLastName",
        "address": "TestAddress",
        "phone_number": 1234567890,
        "department": "TestDepartment"
    }

    repair_data = {
        "price": 75.0,
        "description": "TestRepairDescription",
        "repair_text": "TestRepairText"
    }

    mechanic_data = {
        "name": "TestMechanicName",
        "phone_number": 987654321,
        "address": "TestMechanicAddress"
    }

    # Write test data to the database
    VehicleController.write_vehicle_to_database(vehicle_data)
    DriverController.write_driver_to_database(driver_data)
    RepairController.write_repair_to_database(repair_data)
    MechanicController.write_mechanic_to_database(mechanic_data)

    # Fetch and print data from the database
    db = Database()

    db.cursor.execute("SELECT * FROM vehicle")
    print("Vehicle Table:")
    print(db.cursor.fetchall())

    db.cursor.execute("SELECT * FROM driver")
    print("\nDriver Table:")
    print(db.cursor.fetchall())

    db.cursor.execute("SELECT * FROM repair")
    print("\nRepair Table:")
    print(db.cursor.fetchall())

    db.cursor.execute("SELECT * FROM mechanic")
    print("\nMechanic Table:")
    print(db.cursor.fetchall())
