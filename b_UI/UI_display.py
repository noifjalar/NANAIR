    
class Display_UI :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in
    
    def display_info() :
        choice == "" 
        while choice != "q" :
            print("Display information")
            print("")
            print("\t(1)Display employee information")
            print("\t(2) - Display destinations")
            print("\t(3) - Display voyages")
            print("\t(4) - Display aircraft's status")
            print("\t Press q to quit")
            
            choice = input("Select an operation with a corresponding number: ").lower()

            if choice == "1" :
                while next_choice != "q"
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
                    next_choice = input("Select an operation with a corresponding number: ").lower()
                
                    if next_choice == "1" :
                        self.la.display_all_emp()
                    elif next_choice == "2" :
                        self.la.display_pilots()
                    elif next_choice == "3" :
                        self.la.display_cabin()
                    elif next_choice == "4" :
                        self.la.display_cert_emp()
                    elif next_choice == "5" :
                        self.la.display_off_emp()
                    elif next_choice == "6" :
                        self.la.display_on_emp()
                    elif next_choice == "7" :
                        self.la.display_cert_worksheet()
                    elif next_choice == "8" :
                        self.la.display_pilot_licence() 
                    elif next_choice == "9" :
                        self.la.display_pilot_by_licene()
                    else: 
                        print("Invalid input!")

            elif choice == "2" :
                self.la.display_dest()

            elif choice == "3" :
                self.la.display_voy()

            elif choice == "4" :
                self.la.display_status()

            else:
                print("Invalid input!")
 
