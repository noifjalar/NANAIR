from c_Logic.A_LL_API import LL_API 
import datetime

class Display_UI :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in
    
    def display_info(self) :
        ''' Lets the user pick which information he wants to see from the main menu '''

        choice = ""

        while choice != "q" : 
            print("\n" + "-=x="*15)
            print(" "*20 +"Display information")
            print("-=x="*15 + "\n")
            print("\t(1) - Display employee information")
            print("\t(2) - Display destinations")
            print("\t(3) - Display voyages")
            print("\t(4) - Display aircraft's status")
            print("\tPress Q to go back\n")
            
            choice = input("Select an operation with a corresponding number: ").lower()
            print()

            if choice == "1" :
                next_choice = ""
                while next_choice != "q" :
                    print("\n" + "-=x="*15)
                    print(" "*20 +"Employee information")
                    print("-=x="*15 + "\n")
                    print("\t(1) - Display all employees") 
                    print("\t(2) - Display pilots") 
                    print("\t(3) - Display cabin crew") 
                    print("\t(4) - Display certain employee")
                    print("\t(5) - Display off-duty employees") 
                    print("\t(6) - Display on-duty employees")  
                    print("\t(7) - Display certain employees weekly worksheet")
                    print("\t(8) - Display pilots with certain licences")
                    print("\t(9) - Display pilots ordered by aircraft type")
                    print("\tPress Q to go back\n")
                    next_choice = input("Select an operation with a corresponding number: ").lower()
                    print()
                
                    if next_choice == "1" :
                        print("Employee list: \n")
                        all_emp = self.la.get_all_emp()
                        for name in all_emp :
                            print("\t",name)  
                    elif next_choice == "2" :
                        print("Pilot list: \n")
                        pilot_list = self.la.get_pilots()
                        for name in pilot_list:
                            print("\t",name)
                    elif next_choice == "3" :
                        print("Cabin list: \n")
                        self.la.get_cabin()
                        cabin_list = self.la.get_cabin()
                        for name in cabin_list:
                            print("\t",name)
                    elif next_choice == "4" :
                        # self.la.display_cert_emp()
                        emp_ssn = input("Input the employee's ssn: ")
                        print()
                        wow = self.la.print_chosen_emp(emp_ssn)
                        print("SSN: {}\nName: {} \nRole: {}\nRank: {}\nLicence: {}\nAddress: {}\nPhonenumber: {}\n".format(emp_ssn,wow[0],wow[1],wow[2],wow[3],wow[4],wow[5]))  
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
                        print("\t(3) - NAFokkerF100\n")
                        pick = input("Choose licence: ")
                        print()
                        while pick != "q" :
                            if pick == "1":
                                nabae_list = self.la.get_pilots_with_NABAE146() 
                                print("Pilots with NABAE146 licence: \n")
                                for pilot in nabae_list:
                                    print("\t",pilot)
                            elif pick == "2":
                                nafokkerf28_list = self.la.get_pilots_with_NAFokkerF28()
                                print("Pilots with NAFokkerF28 licence: \n")
                                for pilot in nafokkerf28_list:
                                    print("\t",pilot)
                            elif pick == "3":
                                nafokker100_list = self.la.get_pilots_with_NAFokker100()
                                print("Pilots with NAFokkerF100 licence: \n")
                                for pilot in nafokker100_list:
                                    print("\t",pilot)
                        
                            else:
                                print("Invalid input!")

                        
                    elif next_choice == "9" :
                        nabae_list = self.la.get_pilots_with_NABAE146() 
                        nafokkerf28_list = self.la.get_pilots_with_NAFokkerF28()
                        nafokker100_list = self.la.get_pilots_with_NAFokker100()
                        print("\nPilots with NABAE146 licence: \n")
                        for pilot in nabae_list :
                            print("\t{}".format(pilot))
                        print("\nPilots with NAFokkerF28 licence: \n")
                        for pilot in nafokkerf28_list :
                            print("\t{}".format(pilot))
                        print("\nPilots with NAFokkerF100 licence: \n")
                        for pilot in nafokker100_list :
                            print("\t{}".format(pilot))
                    elif next_choice == "q" :
                        pass       
                    else: 
                        print("Invalid input!")

            elif choice == "2" :
                print("\n" + "-=x="*15)
                print(" "*24 +"Destinations")
                print("-=x="*15 + "\n")
                dest_list = self.la.get_dest()
                for destination in dest_list :
                    print("\t{}\n".format(destination))

            elif choice == "3" :
                print("\n" + "-=x="*15)
                print(" "*26 +"Voyages")
                print("-=x="*15 + "\n")
                voyage_dict = self.la.display_voy()
                counter = 1
                for key, value in voyage_dict.items() :
                    if counter > 1 :
                        print(key, *value)
                    counter += 1

            elif choice == "4" :
                self.la.display_status()
                pass

            elif choice == "q" :
                pass
            else :
                print("Invalid input")
 
