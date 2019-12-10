from Model.voyage import Voyage
from c_Logic.A_LL_API import LL_API
import datetime
from datetime import timedelta


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
        
        counter = 1
        for key, value in dest_dict.items():
            if key == "Keflavik": 
                pass
            else:
                if val == counter:
                    print('bagg')
                    arriving_at = value[0]
                    voy_dest_time = int(value[1])
                counter += 1
       
            
        year, month, day = input("Input date of flight (YYYY MM DD): ").split()
        hour, minute = input("Input time of flight (hour minute): ").split()

        year = int(year)
        month = int(month)
        day = int(day)
        hour = int(hour)
        minute = int(minute)
        
        departure_not_iso = datetime.datetime(year, month, day, hour, minute)
        arrival_not_iso = departure_not_iso + timedelta(hours= voy_dest_time)
        departure = departure_not_iso.isoformat()
        arrival = arrival_not_iso.isoformat()
   
        self.la.addnewvoyage(flight_number, departing_from, arriving_at, departure, arrival)

        flight_number_return = input("Enter a flight number for return flight: ")

        departure_return = (arrival_not_iso + timedelta(hours= 1)).isoformat()
        arrival_return = (arrival_not_iso + timedelta(hours= 1) + timedelta(hours= voy_dest_time)).isoformat()

        departing_from_return = arriving_at
        arriving_return = departing_from
        
        self.la.addnewvoyage(flight_number_return, departing_from_return, arriving_return, departure_return, arrival_return)
