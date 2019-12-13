from Model.employee import Employee
from c_Logic.A_LL_API import LL_API
from d_Data.Data_Employee import Employee_Data


class Employee_UI :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in
    
    def register_employee_UI(self):       
        ''' Registers employees and adds them to CSV '''
        print("-=x="*15)
        print(" "*21 + "Register employee")
        print("-=x="*15 + "\n")
        ssn = input("SSN: ")
        if self.la.check_emp_ssn(ssn) == True :
            name = input("Name: ")
            print("Available roles: ")
            print("\t(1) - Cabin") 
            print("\t(2) - Pilot\n")
            pick = input("Pick a new role: ")
            print()
            if pick == "1":
                role = "Cabincrew"
                print("\nAvailable ranks: ")
                print("\t(1) - Flight Service Manager") 
                print("\t(2) - Flight Attendant\n")
                new_pick = input("Pick a new rank: ")
                if new_pick == "1":
                    rank = "Flight Service Manager"
                elif new_pick == "2":
                    rank = "Flight Attendant"
            elif pick == "2":
                role = "Pilot"
                print("Available ranks: ")
                print("\t(1) - Captain") 
                print("\t(2) - Copilot\n")
                pick = input("Pick a new rank: ")
                if pick == "1":
                    rank = "Captain"
                elif pick == "2":
                    rank = "Copilot"       
            print("\nAvailable licences: ")
            print("\t(1) - NAFokkerF100") #ef við registerum nýja flugvél þarf húna að koma hér inn(megum ekki harð kóða)
            print("\t(2) - NABAE146")
            print("\t(3) - NAFokkerF28") 
            print("\t(4) - N/A\n") 
            pick = input("Pick a new licence: ") 
            print()
            if pick == "1":
                licence = "NAFokkerF100"
            elif pick == "2":
                licence = "NABAE146"
            elif pick == "3":
                licence = "NAFokkerF28"
            elif pick == "4":
                licence = "N/A"
            else:
                print("Invalid input!")   
            address = input("Address: ")
            phonenumber = input("Mobile: ")
            input("\nPress ENTER to continue..\n")
            self.la.addnewemplyee(ssn, name, role, rank, licence, address, phonenumber)
        else: 
            print("Employee already exists\n")

    
    def change_employee_info(self) :
        '''Allows you to change certain informations about an employee, though not his name or ssn'''
        choice = ""
        pick = "n"
        while pick == "n" :
            print("-=x="*15)
            print(" "*17 + "Change employee information")
            print("-=x="*15 + "\n")
            emp_ssn = input("Input the employee's ssn: ")
            print()
            wow = self.la.print_chosen_emp(emp_ssn)
            print("\tSSN: {}\n\tName: {} \n\tRole: {}\n\tRank: {}\n\tLicence: {}\n\tAddress: {}\n\tPhonenumber: {}\n".format(emp_ssn,wow[0],wow[1],wow[2],wow[3],wow[4],wow[5]))
            pick = "s"

            while pick == "s" :                
                print("Change employee info:")
                print("\t(1) - Address") 
                print("\t(2) - Role and Rank")
                print("\t(3) - Licence")
                print("\t(4) - Phonenumber")
                choice = input("Select an operation with a corresponding number: ").lower()
                print()

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
                        print("\nAvailable ranks: ")
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
                    

                    #búa til model fyrir töfluna
                    pick = input("Pick a new licence: ") 
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

                wow = self.la.print_chosen_emp(emp_ssn)
                print("SSN: {}, Name: {} - Role: {}, Rank: {}, Licence: {}, Address: {}, Phonenumber: {}\n".format(emp_ssn,wow[0],wow[1],wow[2],wow[3],wow[4],wow[5]))
                print("Do you want to change:")
                print("(S) - More info about the same employee,")
                print("(N) - change a new employee,")
                print("(R) - or return to main menu")
                pick = input("Select: ").lower()
                print()


    



        
            
        

        

