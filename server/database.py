""" Module providing functions to interact with database """

import mysql.connector


# pylint: disable=line-too-long
class Database:
    """Class representing a database"""

    _instance = None
    connection = mysql.connector.connect(
        host="localhost", user="root", password="root", database="vehicle"
    )
    cursor = connection.cursor()

    def __new__(cls, *args, **kwargs):
        #  Checks if an instance exist already
        if not Database._instance:
            #  Creates Database class if there isn't an existing instance and creates tables
            Database._instance = super(Database, cls).__new__(cls, *args, **kwargs)
            Database.create_tables(cls)

        return Database._instance  #  Returns the instance if one exists already

    def create_tables(self):
        """Code to add tables to database"""

        # Dictionary for tables and the query used to create them
        tables = {
            "vehicle_table": "CREATE TABLE IF NOT EXISTS vehicle (VID INT(6) PRIMARY KEY NOT NULL AUTO_INCREMENT, district VARCHAR(20), section VARCHAR(40), insuranceExp DATE, fitnessExp DATE, licenseExp DATE, vehicleNum INT(9), type VARCHAR(15), fuelType VARCHAR(15), unladenWeight INT(6), model VARCHAR(50), make VARCHAR(20), engineId VARCHAR(30), chassisId VARCHAR(30));",
            "driver_table": "CREATE TABLE IF NOT EXISTS driver (DID INT(6) PRIMARY KEY NOT NULL AUTO_INCREMENT, phoneNumber INT(10), firstName VARCHAR(20), lastName VARCHAR(20), address VARCHAR(125), department VARCHAR(30));",
            "repair_table": "CREATE TABLE IF NOT EXISTS repair (RID INT(6) PRIMARY KEY NOT NULL AUTO_INCREMENT, price DECIMAL(7,2), description TEXT, repairText TEXT);",
            "mechanic_table": "CREATE TABLE IF NOT EXISTS mechanic (MID INT(6) PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(50), phoneNumber INT(10), address VARCHAR(125));",
        }

        print("Creating Tables")

        # Iterate through the "tables" dictionary and executes each SQL statement
        for table_name, sql_statement in tables.items():
            try:
                self.cursor.execute(sql_statement)
            except mysql.connector.Error as e:
                print(f"Error executing SQL for table {table_name}: {e}")
                self.connection.rollback()

    def write_vehicle(self, vehicle):
        """Code to add a vehicle to the vehicle table"""
        try:
            self.cursor.execute(
                "INSERT INTO vehicle (district, section, insuranceExp, fitnessExp, licenseExp, fuelType, unladenWeight, model, make, engineId, chassisId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    vehicle.district,
                    vehicle.section,
                    vehicle.insurance_exp,
                    vehicle.fitness_exp,
                    vehicle.license_exp,
                    vehicle.fuel_type,
                    vehicle.unladen_weight,
                    vehicle.model,
                    vehicle.make,
                    vehicle.engine_id,
                    vehicle.chassis_id,
                ),
            )
            self.connection.commit()

        except mysql.connector.Error as e:
            print(f"Error executing SQL for table vehicle: {e}")
            self.connection.rollback()

    def update_vehicle(self, vehicle_id, field_name, new_value):
        """Update a specific field for a vehicle in the vehicle table"""
        try:
            # Construct the SQL query dynamically based on the provided field name
            update_query = f"UPDATE vehicle SET {field_name} = %s WHERE VID = %s"

            # Execute the update query with the new value and vehicle ID
            self.cursor.execute(update_query, (new_value, vehicle_id))

            # Commit the changes
            self.connection.commit()

            print(
                f"Field '{field_name}' updated successfully for vehicle with ID {vehicle_id}"
            )
        except mysql.connector.Error as e:
            print(
                f"Error executing SQL for updating field '{field_name}' in vehicle table: {e}"
            )
            self.connection.rollback()

    def delete_field(self, table, id):
        """Code to delete a record form the specified table"""

        try:
            query = f"DELETE FROM {table} WHERE ID = %s"
            self.cursor.execute(query, (id))
            self.connection.commit()
            print("Record added")

        except mysql.connector.Error as e:
            print(f"Error executing SQL for table '{table}': {e}")
            self.connection.rollback()

    def write_driver(self, driver):
        """Code to add a driver to the driver table"""
        try:
            self.cursor.execute(
                "INSERT INTO driver (firstName, lastName, address, phoneNumber, department) VALUES (%s, %s, %s, %s, %s)",
                (
                    driver.first_name,
                    driver.last_name,
                    driver.address,
                    driver.phone_number,
                    driver.department,
                ),
            )
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error executing SQL for table driver: {e}")
            self.connection.rollback()

    def write_repair(self, repair):
        """Code to add a repair to the repair table"""
        try:
            self.cursor.execute(
                "INSERT INTO repair (price, description, repairText) VALUES (%s, %s, %s)",
                (
                    repair.price,
                    repair.description,
                    repair.repair_text,
                ),
            )
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error executing SQL for table repair: {e}")
            self.connection.rollback()

    def write_mechanic(self, mechanic):
        """Code to add a mechanic to the mechanic table"""
        try:
            self.cursor.execute(
                "INSERT INTO mechanic (name, phoneNumber, address) VALUES (%s, %s, %s)",
                (
                    mechanic.name,
                    mechanic.phone_number,
                    mechanic.address,
                ),
            )
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error executing SQL for table mechanic: {e}")
            self.connection.rollback()
