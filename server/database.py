class Database:
    _instance = None
    connection = None # TODO: code to initialize database connection here | replace "None"
    cursor = None # ! Database cursor object code goes here
    
    def __new__(cls, *args, **kwargs):
        # * Checks if an instance exist already
        if not Database._instance: 
            # * Creates Database class if there isn't an existing instance and creates tables
            Database._instance = super(Database, cls).__new__(cls, *args, **kwargs)
            Database.createTables(cls)
        
        return Database._instance # * Returns the instance if one exists already
    
    def create_tables(self):
        # Code to add tables to database
        pass