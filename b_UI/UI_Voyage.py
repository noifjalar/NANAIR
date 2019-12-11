from Model.voyage import Voyage
from c_Logic.A_LL_API import LL_API
import datetime



class voyage_UI :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in


    def register_voyage_UI(self):
        
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

    def create_crew_voyage(self):
        aircraftID = input("Aircraft ID: ")
        captains = self.la.find_staff_with_chosen_rank("Captain")
        counter = 1
        for name in captains:
            print("({}) - {}".format(counter, name[1]))
            counter += 1
        val = input("Choose a captain: ")
        self.la.pick_emp_for_voyage(val)
        x = input("h")