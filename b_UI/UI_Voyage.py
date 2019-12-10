from Model.voyage import Voyage
from c_Logic.A_LL_API import LL_API
import datetime


class voyage_UI :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in


    def register_voyage_UI(self):
        

        flight_number = input("Enter a flight number: ")

        departing_from = "KEF"


        #voy_dest_time = ""
        #arriving_at = ""

        dest_dict = self.la.voy_dest()
        counter = 1
        for key,value in dest_dict.items():
            if key == "Keflavik":
                pass
            else:
                print("({}) - {}".format(counter, key))
                counter += 1
        val = int(input("Choose a destination: "))
        #print(val)
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
        #arriving_at = voy_destination
        # print(voy_dest_time)
        print(arriving_at)
        input
            
        


        year, month, day = int(input("Input date of flight (YYYY MM DD): ").split("."))
        hour, minute = int(input("Input time of flight (hour.minute): ").split(":"))
        print(year)
        print(month)
        print(day)
        print(hour)
        print(minute)
        #hour= int(input('input a hour:'))
        #minute= int(input('input a minute:'))


        #year, month, day, hour, minute = year, month, day, hour, minute
        departure = datetime.datetime(year, month, day, hour, minute).isoformat()
        print(departure)
        arrival = datetime.datetime(year, month, day, hour + voy_dest_time, minute).isoformat()

        self.la.addnewvoyage(flight_number, departing_from, arriving_at, departure, arrival)

