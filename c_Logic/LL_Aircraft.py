from d_Data.A_Data_API import DataAPI
from d_Data.Data_Aircraft import Aircraft_Data

class Aircraft_LL :
    def __init__ (self):
        #self.dapi = dapi_in
        self.dapi = Aircraft_Data()

    def addnewaircraft(self, planeInsignia, planeTypeId):
        self.dapi.register_aircraft_Data(planeInsignia, planeTypeId)






    # def register_destination(self):
    #     pass
    # def register_airplanes(self):
    #     pass
    # def create_voyage(self):
    #     pass