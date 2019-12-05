

class Main_Manu_LL :
    def main_menu_choice():
        choice = str(choice)
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
        elif choice == "q":
            break
        else:
            print("Input error! Try again")
            self.main_menu()