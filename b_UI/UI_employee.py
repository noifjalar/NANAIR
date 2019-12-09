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
            print("(2) - Role and Rank")
            #print("(3) - Rank")
            print("(3) - Licence")
            print("(4) - Phonenumber")
            print("Press q to quit")
            choice = input("Select an operation with a corresponding number: ").lower()

            if choice == "1":
                new_address = input("New address: ")
                self.la.change_empl_address(new_address, emp_ssn)
            elif choice == "2":
                print("Available roles: ")
                print("\t(1) - Cabin") 
                print("\t(2) - Pilot")
                pick = input("Pick a new role: ")
                if pick == "1":
                    new_role = "Cabincrew"
                    print("Available ranks: ")
                    print("\t(1) - Flight Service Manager") 
                    print("\t(2) - Flight Attendant")
                    pick = input("Pick a new rank: ")
                    if pick == "1":
                        new_rank = "Flight Service Manager"
                    elif pick == "2":
                        new_rank = "Flight Attendant"
                elif pick == "2":
                    new_role = "Pilot"
                    print("Available ranks: ")
                    print("\t(1) - Captain") 
                    print("\t(2) - Copilot")
                    pick = input("Pick a new rank: ")
                    if pick == "1":
                        new_rank = "Captain"
                    elif pick == "2":
                        new_rank = "Copilot"
                
                self.la.change_empl_role_rank(new_role, new_rank, emp_ssn)

            elif choice == "3":
                print("Available licences: ")
                print("\t(1) - NAFokkerF100") 
                print("\t(2) - NABAE146")
                print("\t(3) - NAFokkerF28") 
                print("\t(4) - N/A") 
               
                pick = input("Pick new licence: ") 
                if pick == "1":
                    new_licence = "NAFokkerF100"
                elif pick == "2":
                    new_licence = "NABAE146"
                elif pick == "3":
                    new_licence = "NAFokkerF28"
                elif pick == "4":
                    new_licence = "N/A"
                else:
                    print("Invalid input!")
                    break
                self.la.change_empl_licence(new_licence, emp_ssn)
            elif choice == "4":
                new_phonenumber = input("New phonenumber: ")
                self.la.change_empl_phonenumber(new_phonenumber,emp_ssn)
            else :
                print("Input error! Try again")
                self.change_employee_info()

    def display_info() :
        choice == "" 
        while choice != "q" :
            print("\tDisplay information")
            print("")
            print("\t(1) - Display employees") #1
            print("\t(2) - Display pilots") #2
            print("\t(3) - Display cabin crew") #3
            print("\t(4) - Display certain employee") #4
            print("\t(5) - Display destinations")#5
            print("\t(6) - Display voyages") #6
            print("\t(7) - Display off-duty employees") #7
            print("\t(8) - Display on-duty employees") #8
            print("\t(9) - Display certain employees weekly worksheet")
            print("\t Press q to quit")
            
            choice = input("Select an operation with a corresponding number: ").lower()

            if choice ==



        
            
        

        

