from Model.destination import Destination 

class Destination_Data :
    def __init__(self):
        self.filename = "./a_csv/Destinations.csv"

    def register_destination_Data(self,identity, destination, flight_time):
        new_destination= Destination(identity, destination, flight_time)
        try :
            with open( self.filename ,"a") as destination_file:
                destination_file.write("\n")
                destination_file.write(new_destination.dest_comma_to_string())
                destination_file.close()      
        except FileNotFoundError :
            return None       

       
        # with open("./csv/Destinations.csv","a") as destination_file:
        #     destination_file.write("\n")
        #     destination_file.write(new_destination_ready_for_print)