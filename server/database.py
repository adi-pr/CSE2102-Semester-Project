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
            "vehicle_table": """
            CREATE TABLE IF NOT EXISTS vehicle (
                VID INT(6) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                district VARCHAR(20),
                section VARCHAR(40),
                insuranceExp DATE,
                fitnessExp DATE,
                licenseExp DATE,
                vehicleNum VARCHAR(10),
                fuelType VARCHAR(15),
                unladenWeight INT(6),
                model VARCHAR(50),
                make VARCHAR(20),
                engineId VARCHAR(30),
                chassisId VARCHAR(30),
                driverID INT(6),
                FOREIGN KEY (driverID) REFERENCES driver(DID)
            );
        """,
            "driver_table": """
            CREATE TABLE IF NOT EXISTS driver (
                DID INT(6) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                phoneNumber INT(10),
                firstName VARCHAR(20),
                lastName VARCHAR(20),
                address VARCHAR(125),
                department VARCHAR(30)
            );
        """,
            "repair_table": """
            CREATE TABLE IF NOT EXISTS repair (
                RID INT(6) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                price DECIMAL(7,2),
                description TEXT,
                repairText TEXT,
                vehicleID INT(6),
                FOREIGN KEY (vehicleID) REFERENCES vehicle(VID)
            );
        """,
            "mechanic_table": """
            CREATE TABLE IF NOT EXISTS mechanic (
                MID INT(6) PRIMARY KEY NOT NULL AUTO_INCREMENT,
                name VARCHAR(50),
                phoneNumber INT(10),
                address VARCHAR(125)
            );
        """,
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
                "INSERT INTO vehicle (district, section, insuranceExp, fitnessExp, licenseExp, vehicleNum, fuelType, unladenWeight, model, make, engineId, chassisId, driverId) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (
                    vehicle.district,
                    vehicle.section,
                    vehicle.insurance_exp,
                    vehicle.fitness_exp,
                    vehicle.license_exp,
                    vehicle.vehicle_num,
                    vehicle.fuel_type,
                    vehicle.unladen_weight,
                    vehicle.model,
                    vehicle.make,
                    vehicle.engine_id,
                    vehicle.chassis_id,
                    vehicle.driver_id,
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

    def find_vehicle_number(self, vehicle_number):
        """Find a vehicle number based on the given vehicle number."""

        try:
            query = "SELECT * FROM vehicle WHERE vehicleNum = %s"
            self.cursor.execute(query, (vehicle_number,))
            result = self.cursor.fetchall()

            if result:
                print(result[0])

            else:
                print("No vehicle found with the given criteria.")
                return None

        except mysql.connector.Error as e:
            print(f"Error executing SQL for finding vehicle number: {e}")

    def delete_field(self, table, field_id):
        """Code to delete a record form the specified table"""

        try:
            query = f"DELETE FROM {table} WHERE ID = %s"
            self.cursor.execute(query, (field_id))
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
                "INSERT INTO repair (price, description, repairText, vehicleID) VALUES (%s, %s, %s, %s)",
                (
                    repair.price,
                    repair.description,
                    repair.repair_text,
                    repair.vehicle_id,
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

    def calculate_total_repair_cost(self, vehicle_num):
        """Get the total repair cost for a specific vehicle based on the given vehicle number."""

        try:
            # Query repairs for the specified vehicle number and calculate the total cost using SUM
            repairs_query = """
                    SELECT SUM(price) FROM repair
                    WHERE vehicleID = (SELECT VID FROM vehicle WHERE vehicleNum = %s)
                """
            self.cursor.execute(repairs_query, (vehicle_num,))
            total_cost_res = self.cursor.fetchone()

            if total_cost_res[0] is not None:
                total_cost = total_cost_res[0]
                print(total_cost)
            else:
                print("No repairs found for the given vehicle.")
                return 0

        except mysql.connector.Error as e:
            print(f"Error executing SQL for getting total repair cost: {e}")
            return 0

    def get_vehicle_repairs(self, vehicle_number):
        """Get repairs for a specific vehicle based on the given vehicle number."""

        try:
            vehicle_query = "SELECT VID FROM vehicle WHERE vehicleNum = %s"
            self.cursor.execute(vehicle_query, (vehicle_number,))
            vehicle_res = self.cursor.fetchone()

            print(vehicle_res)

            if vehicle_res:
                vehicle_id = vehicle_res[0]

                print(vehicle_id)

                # Consume any remaining results from the previous query
                self.cursor.fetchall()

                # Query repairs for the found vehicle ID
                repairs_query = "SELECT * FROM repair WHERE vehicleID = %s"
                self.cursor.execute(repairs_query, (vehicle_id,))
                repair_res = self.cursor.fetchall()

                print(repair_res)

                if repair_res:
                    for repair in repair_res:
                        print(repair)
                else:
                    print("No repairs found for the given vehicle.")

            else:
                print("No vehicle found with the given vehicle number.")

        except mysql.connector.Error as e:
            print(f"Error executing SQL for getting vehicle repairs: {e}")
