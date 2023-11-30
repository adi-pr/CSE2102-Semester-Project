""" Module providing functions to interact with database """

import mysql.connector


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
            "vehicle_table": "CREATE TABLE IF NOT EXISTS Vehicle (VID INT(6) PRIMARY KEY, District VARCHAR(20), Section VARCHAR(40), `Insurance Exp` DATE, `Fitness Exp` DATE, `License Exp` DATE, `Vehicle Num` INT(9), Type VARCHAR(15), `Fuel Type` VARCHAR(15), `Unladen Weight` INT(6), Model VARCHAR(50), Make VARCHAR(20), `Engine ID` VARCHAR(30), `Chassis ID` VARCHAR(30));",
            "driver_table": "CREATE TABLE IF NOT EXISTS Driver (DID INT(6) PRIMARY KEY, `Phone Number` INT(10), `First Name` VARCHAR(20), `Last Name` VARCHAR(20), Address VARCHAR(20), Department VARCHAR(30));",
            "repair_table": "CREATE TABLE IF NOT EXISTS Repair (RID INT(6) PRIMARY KEY, Price DECIMAL(7,2), Descp TEXT, `Repair Type` TEXT);",
            "mechanic_table": "CREATE TABLE IF NOT EXISTS Mechanic (MID INT(6) PRIMARY KEY, Name VARCHAR(50), `Phone Number` INT(10), Address VARCHAR(40));",
        }

        print("Creating Tables")

        # Iterate through the "tables" dictionary and executes each SQL statement
        for table_name, sql_statement in tables.items():
            try:
                self.cursor.execute(sql_statement)
            except mysql.connector.Error as e:
                print(f"Error executing SQL for table {table_name}: {e}")
                self.connection.rollback()


if __name__ == "__main__":
    db = Database()
