from c_Logic.A_LL_API import LL_API

class UI_Aircraft :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in

    def register_aircraft_UI(self):
        ''' Registers aircrafts and adds it to CSV '''
        print("Register airplanes")
        print()
        nickname = input("Plane nickname: ")
        planeTypeId = input("Plane Type ID: ")
        capacity = input("Capacity: ")
        manufacturer = input("Manufacturer: ")

        self.la.addnewaircraft(nickname,planeTypeId,capacity,manufacturer)