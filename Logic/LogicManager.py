#from Data.DataManager import DataManager
from Model.employee import Employee
from UI.UI_register_employee import EmployeeUI
import os

class LogicManager :
    def __init__(self) :
        #self.__ = DataManager()
        pass 

    def register_employee_LL(self):
    

        # ssn = input("SSN: ")
        # name = input("Name: ")
        # #new_emp.name = name
        # address = input("Address: ")
        # role = input("Role: ")
        # rank = input("Rank: ")
        # licence = input("Licence: ")
        # phonenumber = input("Mobile: ")

        UI = UI_register_employee()
        ssn, name, role, rank, licence, address, phonenumber = UI.register_employee_UI()
        new_emp = Employee(ssn, name, role, rank, licence, address, phonenumber)

        #os.getcwd()
        print( new_emp.toCommaSparatedString() )

        new_emp4print = new_emp.toCommaSparatedString()
       
        with open("./csv/Crew.csv","a") as crew_file:
            crew_file.write("\n")
            crew_file.write(new_emp4print)

    
    def change_employee_info(self):
        pass
    def assign_cabin_pilot_to_voyage(self):
        pass
    def display_voyage(self):
        pass
    def register_destination(self):
        pass
    def register_airplanes(self):
        pass
    def create_voyage(self):
        pass