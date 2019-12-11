from Model.destination import Destination 

class Destination_Data :
    def __init__(self):
        self.filename = "./a_csv/Destinations.csv"

    def register_destination_Data(self,identity, destination, flight_time):
        ''' Opens the CSV file and appends input from user '''
        new_destination= Destination(identity, destination, flight_time)
        try :
            with open( self.filename ,"a") as destination_file:
                destination_file.write("\n")
                destination_file.write(new_destination.dest_comma_to_string())
                destination_file.close()      
        except FileNotFoundError :
            return None       

       
    def get_dest_dict(self) :
        ''' Reads the file and returns the contents in a dictionary '''
        dest_dict = {}
        try :
            with open( self.filename , "r" ) as dest_file:
                header = True
                for line in dest_file :
                    if header :
                        header = False
                        continue
                    else:
                        identity, destination, flight_time = line.strip().split(",")
                        dest = Destination(identity, destination, flight_time)
                        dest_list = [dest.identity, dest.flight_time]
                        key = dest.destination
                        dest_dict[key] = (dest_list)
                return dest_dict
                dest_file.close()
        except FileNotFoundError :
            return None

    def get_dest(self) :
        ''' Uses the dictionary and returns the key (destination) in a sorted list '''
        dest_list = [] 
        dest_dict = self.get_dest_dict()
        for key in dest_dict.keys() :
            dest_list.append(key) 
        return sorted(dest_list)