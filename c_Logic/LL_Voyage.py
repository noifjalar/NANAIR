from d_Data.A_Data_API import DataAPI
from d_Data.Data_Voyage import Voyage_Data
from d_Data.Data_Destination import Destination_Data
import datetime


class Voyage_LL :
    def __init__ (self):
        #self.dapi = dapi_in
        self.dvoy = Voyage_Data()
        self.ddata = Destination_Data()

    def addnewvoyage(self, flight_number, departing_from, arriving_at, departure, arrival):
        '''Vantar að tékka hvort emp sé til með ssn tékki'''
        self.dvoy.register_voyage_data(flight_number, departing_from, arriving_at, departure, arrival)

    def voy_dest(self):
        return self.ddata.get_dest_dict()

        #x = input("sdfg")
    def get_voyage(self) :
        self.dvoy.get_voyage()

    def voy_dest_and_arriving_at(self, val):
        dest_dict = self.ddata.get_dest_dict()
        counter = 1
        for key, value in dest_dict.items():
            if key == "Keflavik": 
                pass
            else:
                if val == counter:
                    arriving_at = value[0]
                    voy_dest_time = int(value[1])
                counter += 1
        return arriving_at, voy_dest_time

    def voy_calculating_flight_times(self):
        #arriving_at,voy_dest_time = self.voy_dest_and_arriving_at(val)
        print(self.voy_dest_and_arriving_at)
        print(self.voy_dest_and_arriving_at)