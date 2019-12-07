from Model.aircraft import Aircraft 

class Aircraft_Data :
    def __init__(self):
        self.filename = "./a_csv/Aircraft.csv"

    def register_aircraft_Data(self,nickname,planeTypeId,capacity,manufacturer):
        new_aircraft = Aircraft(nickname,planeTypeId,capacity,manufacturer)
        try :
            with open( self.filename ,"a") as aircraft_file:
                aircraft_file.write("\n")
                aircraft_file.write(new_aircraft.aircraft_comma_to_string())
                aircraft_file.close()      
        except FileNotFoundError :
            return None       