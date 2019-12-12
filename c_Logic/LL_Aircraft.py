from d_Data.Data_Aircraft import Aircraft_Data

class Aircraft_LL :
    def __init__ (self):
        self.dapi = Aircraft_Data()

    def addnewaircraft(self, nickname,planeTypeId,capacity,manufacturer):
        self.dapi.register_aircraft_Data(nickname,planeTypeId,capacity,manufacturer)



    # def register_destination(self):
    #     pass
    # def register_airplanes(self):
    #     pass
    # def create_voyage(self):
    #     pass