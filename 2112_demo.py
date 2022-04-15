import os
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="____",
    database="VPSD_database"
)

mycursor = db.cursor()

def create_directories(employee_id):
    parent_dir = "/usr/local/mysql-8.0.28/EmployeeData"
    directory = str(employee_id)
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

    parent_dir = "/usr/local/mysql-8.0.28/EmployeeData" + "/" + directory
    directory_1 = "Uploaded"
    path = os.path.join(parent_dir, directory_1)
    os.mkdir(path)

def register_Employee(firstname, lastname, email, role):
    mycursor.execute("ALTER TABLE Employee AUTO_INCREMENT = 1")
    mycursor.execute("INSERT INTO Employee (firstname, lastname, email, role) VALUES (%s, %s, %s, %s)", (firstname, lastname, email, role))
    db.commit()
    id = mycursor.lastrowid
    create_directories(id)

def remove_Employee(employee_id):
    mycursor.execute("DELETE FROM VPSD_database.Employee WHERE (employeeID = '2')")
    db.commit()

def print_table():
    for x in mycursor:
        print(x)

register_Employee("Cane", "Smith", "csmith41@vpsd.org", "ESL")
register_Employee("Mike", "Morris", "mmorris101@vpsd.org", "HEALTH")
register_Employee("Megan", "Park", "mpark@vpsd.org", "BUS")

remove_Employee(2);
register_Employee("Margaret", "Newell", "tnewell10@vpsd.org", "ENGLISH")

mycursor.execute("SELECT * FROM EMPLOYEE")
print_table()
