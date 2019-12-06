from c_Logic.A_LL_API import LL_API
from b_UI.UI_employee import Employee_UI
from b_UI.UI_Aircraft import UI_Aircraft

class Manager_UI :
    def __init__(self) :
        self.__la = LL_API()
        self.em = Employee_UI( self.__la )
        self.aircraft = UI_Aircraft(self.__la )
        
    def main_menu(self) :
    
        choice = ""

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
                self.em.register_employee_UI()
            #elif choice == "2":
                #the_instance.change_employee_info()
            #elif choice == "3":
                #the_instance.assing_cabin_pilot_to_voyage()
            #elif choice == "4":
                #the_instance.display_voyage()
            #elif choice == "5":
                #the_instance.register_destination()
            elif choice == "6":
                self.aircraft.register_aircraft_UI()
            #elif choice == "7":
                #the_instance.create_voyage()
            else:
                print("Input error! Try again")
                self.main_menu()