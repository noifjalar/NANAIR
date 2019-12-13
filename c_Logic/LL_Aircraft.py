from d_Data.Data_Aircraft import Aircraft_Data

class Aircraft_LL :
    def __init__ (self):
        self.dapi = Aircraft_Data()

    def addnewaircraft(self, nickname, aircraftID, planeTypeId,capacity,manufacturer):
        self.dapi.register_aircraft_Data(nickname,aircraftID,planeTypeId,capacity,manufacturer)

    def check_aircraftid(self, aircraftID) :
        if len(aircraftID.split("-")) != 2 :
            return False 
        else :
            one, two = aircraftID.split("-")
            if one !=  "TF" or len(two) != 3 or two.isdigit() :
                return False
        return True        
