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
                    print("\t(9) - Display pilots ordered by licence")
                    print("\tPress Q to go back\n")
                    next_choice = input("Select an operation with a corresponding number: ").lower()
                    print()
                
                    if next_choice == "1" :
                        print("-=x="*15)
                        print(" "*24 +"Employee list")
                        print("-=x="*15 + "\n")
                        all_emp = self.la.get_all_emp()
                        for name in all_emp :
                            print("\t",name)  
                    elif next_choice == "2" :
                        print("-=x="*15)
                        print(" "*25 +"Pilot list")
                        print("-=x="*15 + "\n")
                        pilot_list = self.la.get_pilots()
                        for name in pilot_list:
                            print("\t",name)
                    elif next_choice == "3" :
                        print("-=x="*15)
                        print(" "*25 +"Cabin list")
                        print("-=x="*15 + "\n")
                        self.la.get_cabin()
                        cabin_list = self.la.get_cabin()
                        for name in cabin_list:
                            print("\t",name)
                    elif next_choice == "4" :
                        print("-=x="*15)
                        print(" "*22 +"Certain employee")
                        print("-=x="*15 + "\n")
                        emp_ssn = input("Input the employee's ssn: ")
                        print()
                        wow = self.la.print_chosen_emp(emp_ssn)
                        print("\tSSN: {}\n\tName: {} \n\tRole: {}\n\tRank: {}\n\tLicence: {}\n\tAddress: {}\n\tPhonenumber: {}\n".format(emp_ssn,wow[0],wow[1],wow[2],wow[3],wow[4],wow[5]))  
                    elif next_choice == "5" :
                        self.la.display_off_emp() #VANTAR 
                        print("-=x="*15)
                        print(" "*21 +"Employees off-duty")
                        print("-=x="*15 + "\n")
                        off_list = [] = self.la.get_off_emp()

                    elif next_choice == "6" :
                        print("-=x="*15)
                        print(" "*21 +"Employees on-duty")
                        print("-=x="*15 + "\n")
                        date = input("Input date to look up working employees (YYYY-MM-DD): ")
                        on_list = self.la.get_on_emp(date)
                        for listinn in on_list :
                            print("\nEmployees flying to {}:".format(listinn[5]))
                            print("Employee: {} is flying to {}".format(listinn[0],listinn[5]))
                            print("Employee: {} is flying to {}".format(listinn[1],listinn[5]))
                            print("Employee: {} is flying to {}".format(listinn[2],listinn[5]))
                            print("Employee: {} is flying to {}".format(listinn[3],listinn[5]))
                            print("Employee: {} is flying to {}".format(listinn[4],listinn[5]))
                            

                    elif next_choice == "7" :
                        self.la.display_cert_worksheet() #VANTAR 
                        print("-=x="*15)
                        print(" "*20 +"Employees worksheet")
                        print("-=x="*15 + "\n")
                    elif next_choice == "8" :
                        print("-=x="*15)
                        print(" "*16 +"Pilots with certain licences")
                        print("-=x="*15 + "\n")
                        print("\nAvailable licences:\n")
                        print("\t(1) - NABAE146")
                        print("\t(2) - NAFokkerF28")
                        print("\t(3) - NAFokkerF100\n")
                        pick = input("Choose licence: ")
                        print()
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
                        print("-=x="*15)
                        print(" "*17 +"Pilots ordered by licence")
                        print("-=x="*15 + "\n")
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
                print("\t(1) - Display all voyages") 
                print("\t(2) - Display voyages on a certain date") 
                print("\t(3) - Display voyages in a certain week\n") 
                next_choice = input("Select an operation with a corresponding number: ").lower()
                print()
                if next_choice == "1" :
                    voyage_dict = self.la.display_voy()
                    counter = 1
                    for key, value in voyage_dict.items() :
                        if counter > 1 :
                            print(key, *value)
                        counter += 1
                elif next_choice == "2" :
                    counter = 1
                    date = input("Input date to look up voyages (YYYY-MM-DD): ")
                    manned_voy_list, unmanned_voy_list = self.la.certain_date_voy(date)
                    print("\nVoyages with assigned crew: ")
                    for listinn in manned_voy_list :
                        print(*listinn)
                        if counter % 2 == 0 :
                            print()
                        counter +=1
                    counter = 1
                    print("\nVoyages without assigned crew: ")
                    for listinn in unmanned_voy_list :
                        print(*listinn)
                        if counter % 2 == 0 :
                            print()
                        counter +=1
                        

                elif next_choice == "3" :
                    counter = 1 
                    

                else: 
                    print("Invalid input!")    

            elif choice == "4" :
                print("-=x="*15)
                print(" "*17 + "Display aircraft's status")
                print("-=x="*15 + "\n")
                self.la.display_status()
                pass

            elif choice == "q" :
                pass
            else :
                print("Invalid input")
 
