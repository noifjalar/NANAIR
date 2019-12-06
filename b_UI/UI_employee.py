from c_Logic.A_LL_API import A_LL_API
from Model.employee import Employee

class Employee_UI :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in
        pass

    def register_employee_UI(self):
        ssn = input("SSN: ")
        name = input("Name: ")
        address = input("Address: ")
        role = input("Role: ")
        rank = input("Rank: ")
        licence = input("Licence: ")
        phonenumber = input("Mobile: ")
        new_emp = Employee(ssn, name, role, rank, licence, address, phonenumber)
        la.addnewemplyee( new_emp )
