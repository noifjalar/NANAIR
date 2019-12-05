

class Destination_Data :
    def register_destination_Data():
       
        with open("./csv/Destinations.csv","a") as destination_file:
            destination_file.write("\n")
            destination_file.write(new_destination_ready_for_print)