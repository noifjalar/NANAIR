from d_Data.A_Data_API import DataAPI
from d_Data.Data_Voyage import Voyage_Data
import datetime


class Voyage_LL :
    def __init__ (self):
        #self.dapi = dapi_in
        self.dvoy = Voyage_Data()

def addnewvoyage(self, flightNumber, departingFrom, arrivingAt, departure, arrival):
        '''Vantar að tékka hvort emp sé til með ssn tékki'''
        self.dvoy.register_voyage_data(flightNumber, departingFrom, arrivingAt, departure, arrival)
