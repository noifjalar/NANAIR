from Model.aircraft import Aircraft 

class Aircraft_Data :
    def __init__(self):
        self.filename = "./a_csv/Aircraft.csv"
        self.trash_file = "./a_csv/Aircraft_Trash.csv"

    def register_aircraft_Data(self,nickname,planeTypeId,capacity,manufacturer):
        ''' Opens the CSV file and appends input from user '''
        new_aircraft = Aircraft(nickname,planeTypeId,capacity,manufacturer)
        try :
            with open( self.filename ,"a") as aircraft_file:
                aircraft_file.write("\n")
                aircraft_file.write(new_aircraft.aircraft_comma_to_string())
                aircraft_file.close()      
        except FileNotFoundError :
            return None       
            
    def get_aircraft_dict(self) :
        '''creates a dictionary with all the aircrafts'''
        aircraft_dict = {}
        try :
            with open (self.filename, "r") as aircraft_file:
                for line in aircraft_file:
                    nickname,aircraftID,planeTypeId,capacity,manufacturer = line.strip().split(",")
                    airc = Aircraft(nickname,aircraftID,planeTypeId,capacity,manufacturer)
                    aircraft_list = [airc.aircraftID, airc.planeTypeId, airc.capacity, airc.manufacturer]
                    key = airc.nickname
                    aircraft_dict[key] = aircraft_list
                return aircraft_dict
                aircraft_file.close()
        except FileNotFoundError:
            return None

    