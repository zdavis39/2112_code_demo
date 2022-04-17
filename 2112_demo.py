import os
import mysql.connector
import json

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="_______",
    database="VPSD_database"
)

mycursor = db.cursor()

def create_directories(employee_id):
    parent_dir = "/usr/local/mysql-8.0.28-macos11-x86_64/EmployeeData"
    directory = str(employee_id)
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    parent_dir = "/usr/local/mysql-8.0.28-macos11-x86_64/EmployeeData" + "/" + directory
    directory_1 = "Uploaded"
    path = os.path.join(parent_dir, directory_1)
    os.mkdir(path)

def register_Employee(firstname, lastname, email, role):
    mycursor.execute("ALTER TABLE Employee AUTO_INCREMENT = 1")
    role_array = {"role" : role}
    role_array = json.dumps(role_array)
    mycursor.execute("INSERT INTO Employee (firstname, lastname, email, role) VALUES (%s, %s, %s, %s)", (firstname, lastname, email, role_array))
    db.commit()
    employee_id = mycursor.lastrowid
    create_directories(employee_id)

def remove_Employee(employee_id):
    mycursor.execute("DELETE FROM VPSD_database.Employee WHERE (employeeID = %s)", [employee_id])
    db.commit()

def print_table_descriptions():
    employee_table = mycursor
    for x in employee_table:
        firstname, lastname, email, role, employee_id = x
        f = json.loads(role)
        roles = f['role']
        print("Employee #{2} is {0} {1} who has role: {3}".format(firstname, lastname, employee_id, roles))

def change_email(employee_id, new_email):
    mycursor.execute("UPDATE VPSD_database.Employee SET email = %s WHERE (employeeID = %s)", (new_email, employee_id))
    db.commit()

# remove_Employee(2);
# change_email(1, "csmith20@gmail.com")
# register_Employee("Cane", "Smith", "csmith41@vpsd.org", ["ESL"])
# register_Employee("Mike", "Morris", "mmorris101@vpsd.org", ["ENGLISH", "BUS"])
# register_Employee("Megan", "Park", "mpark@vpsd.org", ["HEALTH"])
# register_Employee("Shelly", "Newell", "snewell10@vpsd.org", ["ENGLISH"])

mycursor.execute("SELECT * FROM EMPLOYEE")
print_table_descriptions()
