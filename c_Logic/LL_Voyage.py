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

