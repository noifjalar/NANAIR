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

    def change_employee_info(self) :
        print("\tChange employee info")
        print("(1) - Address") 
        print("(2) - Role")
        print("(3) - Rank")
        print("(4) - Licence")
        print("(5) - Phonenumber")
        print("Press q to quit")
        choice = input("Select an operation with a corresponding number: ").lower()

        if choice == "1":
            self.la.change_empl_address()
        elif choice == "2":
            self.la.change_empl_role()
        elif choice == "3":
            self.la.change_empl_rank()
        elif choice == "4":
            self.la.change_empl_licence()
        elif choice == "5":
            self.la.change_empl_phonenumber()
        else :
            print("Input error! Try again")
            self.change_employee_info()
        pass

        

