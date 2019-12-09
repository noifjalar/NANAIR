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
            #print(*wow)
            print("SSN: {}, Name: {} - Address: {}, Role: {}, Rank: {}, Licence: {}, Phonenumber: {}".format(emp_ssn,wow[0],wow[1],wow[2],wow[3],wow[4],wow[5]))
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
                print("\t(1) - Cabin") 
                print("\t(2) - Pilot")
                pick = input("Pick a new role: ")
                if pick == "1":
                    new_role = "Cabincrew"
                elif pick == "2":
                    new_role = "Pilot"
                # else:??
                #     print("ertu mönni??")
                # new_role = input("New role: ")
                self.la.change_empl_role(new_role, emp_ssn)
            elif choice == "3":
                print("\t(1) - Captain") 
                print("\t(2) - Copilot")
                print("\t(3) - Flight Service Manager") 
                print("\t(4) - Flight Attendant")
                pick = input("Pick a new rank: ")
                if pick == "1":
                    new_rank = "Captain"
                elif pick == "2":
                    new_rank = "Copilot"
                elif pick == "3":
                    new_rank = "Flight Service Manager"
                elif pick == "4":
                    new_rank = "Flight Attendant"
                # else:??
                #     print("ertu mönni??")
                # new_rank = input("New rank: ")
                self.la.change_empl_rank(new_rank, emp_ssn)
            elif choice == "4":
                print("\t(1) - NAFokkerF100") 
                print("\t(2) - NABAE146")
                print("\t(3) - NAFokkerF28") 
               
                pick = input("Pick new licence: ")
                if pick == "1":
                    new_rank = "NAFokkerF100"
                elif pick == "2":
                    new_rank = "NABAE146"
                elif pick == "3":
                    new_rank = "NAFokkerF28"
                else:
                    print("ertu mönni??")
                new_licence = input("New licence: ")
                self.la.change_empl_licence(new_licence, emp_ssn)
            elif choice == "5":
                new_phonenumber = input("New phonenumber: ")
                self.la.change_empl_phonenumber(new_phonenumber,emp_ssn)
            else :
                print("Input error! Try again")
                self.change_employee_info()
            
        

        

