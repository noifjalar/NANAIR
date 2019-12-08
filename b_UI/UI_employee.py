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
        choice = ""
        while choice != "q" :
            emp_ssn = input("Input the employee's ssn: ")
            wow = self.la.print_chosen_emp(emp_ssn)
            print(*wow)
            #print("SSN: {}, Name: {} - Address: {}, Role: {}, Rank: {}, Licence: {}, Phonenumber: {}".format())
            print("\tChange employee info")
            print("(1) - Address") 
            print("(2) - Role")
            print("(3) - Rank")
            print("(4) - Licence")
            print("(5) - Phonenumber")
            print("Press q to quit")
            choice = input("Select an operation with a corresponding number: ").lower()
            #emp_ssn = input("Input the employee's ssn: ")

            if choice == "1":
                new_address = input("New address: ")
                self.la.change_empl_address(new_address, emp_ssn)
            elif choice == "2":
                new_role = input("New role: ")
                self.la.change_empl_role(new_role, emp_ssn)
            elif choice == "3":
                new_rank = input("New rank: ")
                self.la.change_empl_rank(new_rank, emp_ssn)
            elif choice == "4":
                new_licence = input("New licence: ")
                self.la.change_empl_licence(new_licence, emp_ssn)
            elif choice == "5":
                new_phonenumber = input("New phonenumber: ")
                self.la.change_empl_phonenumber(new_phonenumber,emp_ssn)
            else :
                print("Input error! Try again")
                self.change_employee_info()
        

        

