#from c_Logic.A_LL_API import LL_API
from Model.employee import Employee
from c_Logic.A_LL_API import LL_API
from d_Data.Data_Employee import Employee_Data


class Employee_UI :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in

    def register_employee_UI(self):
        ssn = input("SSN: ")
        name = input("Name: ")
        address = input("Address: ")
        role = input("Role: ")
        rank = input("Rank: ")
        licence = input("Licence: ")
        phonenumber = input("Mobile: ")
        #de = Employee_Data()
        #emp_id = self.la.new_emp_id()
        #emp_id = la.new_emp_id()
        #new_emp = Employee(ssn, name, role, rank, licence, address, phonenumber, emp_id)
        self.la.addnewemplyee(ssn, name, role, rank, licence, address, phonenumber)
