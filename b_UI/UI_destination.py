from c_Logic.A_LL_API import LL_API

class UI_Destination:
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in

    def register_destination_UI(self):
        ''' Registers destinations and appends it to CSV '''
        print("-=x="*15)
        print(" "*20 + "Register destination")
        print("-=x="*15 + "\n")
        identity = input("ID: ")
        destination = input("Destination: ")
        flight_time = input("Flight time: ")
        # new_destination = Destination(identity, destination, flight_time)
        self.la.addnewdestination(identity, destination, flight_time)

    def change_em_info(self) :
        choice = ""
        pick = "n"
        while pick == "n" :
            print("-=x="*15)
            print(" "*12 + "Change emergency contact information")
            print("-=x="*15 + "\n")
            des_id = input("Destination ID: ")
            print()
            des_info = self.la.print_chosen_emer(des_id)
            print("\tDestination ID: {}\n\tName: {} \n\tPhonenumber: {}\n".format(des_id,des_info[0],des_info[1]))
            pick = "s"

            while pick == "s" :                
                print("Change emergency contact info:")
                print("\t(1) - Name") 
                print("\t(2) - Phonenumber")
                choice = input("Select an operation with a corresponding number: ").lower()
                print()

                if choice == "1":
                    new_name = input("New name: ")
                    self.la.change_emer_name(new_name, des_id)
                elif choice == "2":
                    new_number = input("New phonenumber: ")
                    self.la.change_emer_number(new_number, des_id)
                else :
                    print("Input error! Try again")
                    self.change_em_info()

                des_info = self.la.print_chosen_emer(des_id)
                print("\tDestination ID: {}\n\tName: {} \n\tPhonenumber: {}\n".format(des_id,des_info[0],des_info[1]))
                print("Do you want to change:")
                print("(S) - More info about the same employee,")
                print("(N) - change a new employee,")
                print("(R) - or return to main menu")
                pick = input("Select: ").lower()
                print()    
