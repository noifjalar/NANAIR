from c_Logic.A_LL_API import LL_API

class UI_Aircraft :
    def __init__(self, logicAPI_in ) :
        self.la = logicAPI_in

    def register_aircraft_UI(self):
        ''' Registers aircrafts and adds it to CSV '''
        register = True
        while register == True :
            print("-=x="*15)
            print(" "*21 +"Register airplanes")
            print("-=x="*15 + "\n")
            nickname = input("Plane nickname: ").upper()
            aircraftID = input("Aircraft ID (e.g TF-XXX): ").upper()
            if self.la.check_aircraftid(aircraftID) == False :
                print("\nNot a valid aircraftID!\n")
                break
            print("\t(1) - NAFokkerF100") 
            print("\t(2) - NABAE146")
            print("\t(3) - NAFokkerF28")
            pick = input("Pick a new licence: ") 
            if pick == "1":
                planeTypeId = "NAFokkerF100"
                capacity = "100"
                manufacturer = "Fokker"
                print("Plane type ID: {} - Capacity: {} - Manufacturer: {}".format(planeTypeId, capacity, manufacturer))
            elif pick == "2":
                planeTypeId = "NABAE146"
                capacity = "82"
                manufacturer = "BAE"
                print("Plane type ID: {} - Capacity: {} - Manufacturer: {}".format(planeTypeId, capacity, manufacturer))
            elif pick == "3":
                planeTypeId = "NAFokkerF28"
                capacity = "65"
                manufacturer = "Fokker"
                print("Plane type ID: {} - Capacity: {} - Manufacturer: {}".format(planeTypeId, capacity, manufacturer))
            input("\nPress ENTER to continue..")
            print()
            self.la.addnewaircraft(nickname,aircraftID,planeTypeId,capacity,manufacturer)
            break