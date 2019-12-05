#from Data.DataManager import DataManager
from Model.employee import Employee
import os


class LogicManager :
    def __init__(self) :
        #self.__ = DataManager()
        pass 


    def register_employee(self):
        
        #new_emp = Employee()
        #name, ssn, address, role, rank, mobile, licence

        ssn = input("SSN: ")
        #new_emp.ssn(ssn)
        
        name = input("Name: ")
        #new_emp.name = name

        address = input("Address: ")
        #new_emp.address(address)

        role = input("Role: ")
        #new_emp.role(role)

        rank = input("Rank: ")
        #new_emp.rank(rank)

        licence = input("Licence: ")
        #new_emp.licence(licence)
         
        phonenumber = input("Mobile: ")
        #new_emp.mobile(mobile)

        new_emp = Employee(ssn, name, role, rank, licence, address, phonenumber)

        print(new_emp.name + new_emp.address)
        print( os.getcwd() )
        print( new_emp.toCommaSparatedString() )
        smu = input("halting ")

        #emp = Employee(name, ssn, address)
        #emp.write_to_csv("Crew.csv")



        new_emp4print = new_emp.toCommaSparatedString()
        # # print(new_emp4print)
         
        # # crew_file = open("./Crew.csv","a")
       
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