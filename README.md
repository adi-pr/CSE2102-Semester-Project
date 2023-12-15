# Vehicle Budgeting Application
### CSE2102 Semester Project

This application is designed to streamline vehicle budgeting and maintenance management for transport managers in telecommunications companies. It utilizes Python, Tkinter, and MySQL to provide a user-friendly interface, automated data entry and reporting, and comprehensive data analysis capabilities.

## Features

* **Maintain** a list of vehicles with their details (type, registration number).
* **Record** maintenance events for each vehicle, including date, type, and cost.
* **Track** repair expenses for each vehicle, including date, description, and cost.
* **Generate** detailed vehicle budgeting reports.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed.
- MySQL server installed and running.
- Required Python libraries installed. You can install them using pip:

```pip install mysql-connector-python tkinter```

## Installation
1. Clone the repository:
 ``` git clone https://github.com/adi-pr/CSE2102-Semester-Project.git ```

3. Navigate to the project directory:  
   ```cd CSE2102-Semester-Project```

4. Update the database connection settings in the Database class to match your MySQL server configuration:  
```
  # Inside the Database class in server/database.py  
  connection = mysql.connector.connect(
        host="localhost", user="root", password="root", database="vehicle"
    )
```
## Usage
1. Run the main application script:
  ```python client/main.py``` 
## License
