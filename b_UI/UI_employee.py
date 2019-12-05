from c_Logic.A_LL_Manager import A_LL_Manager

class Employee_UI :
    def __init__(self) :
        pass

    def register_employee_UI(self):
        ssn = input("SSN: ")
        name = input("Name: ")
        #new_emp.name = name
        address = input("Address: ")
        role = input("Role: ")
        rank = input("Rank: ")
        licence = input("Licence: ")
        phonenumber = input("Mobile: ")
        new_emp = Employee(ssn, name, role, rank, licence, address, phonenumber)
        
