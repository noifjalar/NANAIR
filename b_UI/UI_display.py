from c_Logic.A_LL_API import LL_API 

class Display_UI :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in
    
    def display_info(self) :

        choice = ""

        while choice != "q" : 
            print("Display information")
            print("")
            print("\t(1) - Display employee information")
            print("\t(2) - Display destinations")
            print("\t(3) - Display voyages")
            print("\t(4) - Display aircraft's status")
            print("\tPress Q to go back")
            
            choice = input("Select an operation with a corresponding number: ").lower()

            if choice == "1" :
                next_choice = ""
                while next_choice != "q" :
                    print("Employee information")
                    print("\t(1) - Display all employees") 
                    print("\t(2) - Display pilots") 
                    print("\t(3) - Display cabin crew") 
                    print("\t(4) - Display certain employee")
                    print("\t(5) - Display off-duty employees") 
                    print("\t(6) - Display on-duty employees")  
                    print("\t(7) - Display certain employees weekly worksheet")
                    print("\t(8) - Display pilots with certain licences")
                    print("\t(9) - Display pilots ordered by aircraft type")
                    print("\tPress Q to go back")
                    next_choice = input("Select an operation with a corresponding number: ").lower()
                
                    if next_choice == "1" :
                        print("Employee list: ")
                        all_emp = self.la.get_all_emp()
                        for name in all_emp :
                            print(name)
                    elif next_choice == "2" :
                        print("Pilot list: ")
                        pilot_list = self.la.get_pilots()
                        for name in pilot_list:
                            print(name)
                    elif next_choice == "3" :
                        print("Cabin list: ")
                        self.la.get_cabin()
                        cabin_list = self.la.get_cabin()
                        for name in cabin_list:
                            print(name)
                    elif next_choice == "4" :
                        # self.la.display_cert_emp()
                        emp_ssn = input("Input the employee's ssn: ")
                        print()
                        wow = self.la.print_chosen_emp(emp_ssn)
                        print("SSN: {}, Name: {} - Role: {}, Rank: {}, Licence: {}, Address: {}, Phonenumber: {}\n".format(emp_ssn,wow[0],wow[1],wow[2],wow[3],wow[4],wow[5]))  
                    elif next_choice == "5" :
                        self.la.display_off_emp() #VANTAR 
                    elif next_choice == "6" :
                        self.la.display_on_emp() #VANTAR 
                    elif next_choice == "7" :
                        self.la.display_cert_worksheet() #VANTAR 
                    elif next_choice == "8" :
                        print("Available licences: ")
                        print("\t(1) - NABAE146")
                        print("\t(2) - NAFokkerF28")
                        print("\t(3) - NAFokkerF100")
                        pick = input("Choose licence: ")
                        if pick == "1":
                            nabae_list = self.la.get_pilots_with_NABAE146() 
                            for pilot in nabae_list:
                                print("Pilots with NABAE146 licence: ")
                                print(pilot)
                        elif pick == "2":
                            nafokkerf28_list = self.la.get_pilots_with_NAFokkerF28()
                            for pilot in nafokkerf28_list:
                                print("Pilots with NAFokkerF28 licence: ")
                                print(pilot)
                        elif pick == "3":
                            nafokker100_list = self.la.get_pilots_with_NAFokker100()
                            for pilot in nafokker100_list:
                                print("Pilots with NAFokkerF100 licence: ")
                                print(pilot)
                        else:
                            print("Invalid input!")

                        
                    elif next_choice == "9" :
                        nabae_list = self.la.get_pilots_with_NABAE146() 
                        nafokkerf28_list = self.la.get_pilots_with_NAFokkerF28()
                        nafokker100_list = self.la.get_pilots_with_NAFokker100()
                        print("Pilots with NABAE146 licence: ")
                        for pilot in nabae_list :
                            print("\t{}".format(pilot))
                        print("Pilots with NAFokkerF28 licence: ")
                        for pilot in nafokkerf28_list :
                            print("\t{}".format(pilot))
                        print("Pilots with NAFokkerF100 licence: ")
                        for pilot in nafokker100_list :
                            print("\t{}".format(pilot))
                            
                    else: 
                        print("Invalid input!")

            elif choice == "2" :
                print()
                print("Destinations: ")
                dest_list = self.la.get_dest()
                for destination in dest_list :
                    print("\t{}".format(destination))
                print()

            elif choice == "3" :
                self.la.display_voy()
                pass

            elif choice == "4" :
                self.la.display_status()
                pass

            else:
                print("Invalid input!")
                pass
 
