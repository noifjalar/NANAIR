from Model.employee import Employee

class EmployeeUI :
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
        return ssn, name, role, rank, licence, address, phonenumber
