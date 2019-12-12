from c_Logic.A_LL_API import LL_API
import datetime



class voyage_UI :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in


    def register_voyage_UI(self):
    ''' Registers new flights for voyages and adds it to CSV '''
        
        flight_number = input("Enter a flight number: ")
        departing_from = "KEF"

        dest_dict = self.la.voy_dest()
        counter = 1
        for key,value in dest_dict.items():
            if key == "Keflavik":
                pass
            else:
                print("({}) - {}".format(counter, key))
                counter += 1
        val = int(input("Choose a destination: "))
        
        arriving_at, voy_dest_time = self.la.voy_dest_and_arriving_at(val)
            
        year, month, day = input("Input date of flight (YYYY MM DD): ").split()
        hour, minute = input("Input time of flight (hour minute): ").split()

        year = int(year)
        month = int(month)
        day = int(day)
        hour = int(hour)
        minute = int(minute)

        flight_number_return = input("Enter a flight number for return flight: ")
        departure_not_iso = datetime.datetime(year, month, day, hour, minute)
        ''' Send the input information down to LL_Voyage for calculation '''
        departure, arrival, departing_from_return, arriving_return, departure_return, arrival_return = self.la.voy_calculating_flight_times(val, departure_not_iso, departing_from)
        ''' Send the input and calculated information to the model class '''
        self.la.addnewvoyage(flight_number, departing_from, arriving_at, departure, arrival)
        self.la.addnewvoyage(flight_number_return, departing_from_return, arriving_return, departure_return, arrival_return)

    def create_crew_air_voyage(self):
        ''' allows us to append planes and employees to flights to create voyages'''
        flightNumber = input("Input flight number (e.g. NA1234): ")
        aircraftID = input("Choose an airplane: ")
        # þarf að birta lista af lausum flugvélum

        header_list = ['Captain','Copilot','Flight Service Manager','Flight Attendant','Flight Attendant']
        header_counter = 0
        fa2 = None
        emps_picked_for_voyage = []
        print_chosen_emps = []
        
        while header_counter < len(header_list):
            emps_available = self.la.find_staff_with_chosen_rank(header_list[header_counter])
            numb_of_emp = 1
            print("{}:".format(header_list[header_counter]))
            for name in emps_available:
                print("\t({}) - {}".format(numb_of_emp, name[1]))
                numb_of_emp += 1
            val = int(input("Choose a {}: ".format(header_list[header_counter])))
            print("")
            emps_picked_for_voyage.append(emps_available[val-1][0])
            print_chosen_emps.append(emps_available[val-1][1])
            header_counter += 1

        print("Crew you have chosen for current voyage:")
        print("\tCaptain: {} - Copilot: {},".format(print_chosen_emps[0], print_chosen_emps[1]))
        print("\tFlight Service Manager: {} - Flight Attendant: {} - Flight Attendant: {}.".format(print_chosen_emps[2], print_chosen_emps[3], print_chosen_emps[4]))
        input("Press ENTER to continue..")

        self.la.picked_emp_for_voyage(emps_picked_for_voyage, aircraftID, flightNumber)
