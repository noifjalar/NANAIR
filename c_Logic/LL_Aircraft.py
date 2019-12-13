from d_Data.Data_Aircraft import Aircraft_Data

class Aircraft_LL :
    def __init__ (self):
        self.dapi = Aircraft_Data()

    def addnewaircraft(self, nickname, aircraftID, planeTypeId,capacity,manufacturer):
        self.dapi.register_aircraft_Data(nickname,aircraftID,planeTypeId,capacity,manufacturer)
