from d_Data.A_Data_API import DataAPI
from d_Data.Data_Destination import Destination_Data

class Destination_LL:
    def __init__ (self):
        #self.dapi = dapi_in
        self.dapi = Destination_Data()

    # def addnewdestination(self, identity, destination, flight_time)):
    #     new_destination_ready_for_print = new_destination.dest_comma_to_string

    def addnewdestination(self, identity, destination, flight_time):
        self.dapi.register_destination_Data(identity, destination, flight_time)

    def get_dest(self) :
        return self.dapi.get_dest()

    def get_chosen_emer(self, des_id):
        return self.dapi.get_chosen_emer(des_id)

    def change_emer_name(self, new_name, des_id):
        return self.dapi.change_emer_name(new_name, des_id)
    
    def change_emer_number(self, new_number, des_id) :
        return self.dapi.change_emer_number(new_number, des_id)