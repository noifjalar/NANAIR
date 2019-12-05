from c_Logic.A_LL_Manager import LogicManager

class Main_Menu_UI :
    def main_menu(self) :
        choice = ""
        the_instance = LogicManager()
        while choice != "q" :
            print("\tMain Menu")
            print("")
            print("Shift manager:")
            print("\t(1) - Register employee") #1
            print("\t(2) - Change employee info") #2
            print("\t(3) - Assign cabin/pilot to voyage") #3
            print("\t(4) - Display voyage") #4
            print("")
            print("Registration manager:")
            print("\t(5) - Register destination") #5
            print("\t(6) - Register airplanes") #6
            print("\t(7) - Create voyage") #7
            print("\t Press q to quit")
            
            choice = input("Select an operation with a corresponding number: ").lower()

            if choice == "1":
                the_instance.register_employee_LL()
            elif choice == "2":
                the_instance.change_employee_info()
            elif choice == "3":
                the_instance.assing_cabin_pilot_to_voyage()
            elif choice == "4":
                the_instance.display_voyage()
            elif choice == "5":
                the_instance.register_destination()
            elif choice == "6":
                the_instance.register_airplanes()
            elif choice == "7":
                the_instance.create_voyage()
            else:
                print("Input error! Try again")
                self.main_menu()