from Model.voyage import Voyage
from Model.voyage import Voyage_2
import csv
import re
import os


class Voyage_Data :
    def __init__(self):
        self.filename = "./a_csv/UpcomingFlights.csv"
        self.trash_file = "./a_csv/UpcomingFlights_Trash.csv"    
    
    def register_voyage_data(self, flightNumber, departingFrom, arrivingAt, departure, arrival):
            new_voy = Voyage(flightNumber, departingFrom, arrivingAt, departure, arrival)
            try :
                with open( self.filename ,"a") as upcoming_file:
                    upcoming_file.write("\n")
                    upcoming_file.write(new_voy.voy_comma_to_string())
                    upcoming_file.close()      
            except FileNotFoundError :
                return None    

    def get_voy_dict(self) :
        voy_dict = {}
        try: 
            with open(self.filename, "r" ) as voy_file:
                for line in voy_file :
                    check_len = line.split(",")
                    if len(check_len) == 5 :
                        flightNumber, departingFrom, arrivingAt, departure, arrival =  line.strip().split(",")
                        voy = Voyage(flightNumber, departingFrom, arrivingAt, departure, arrival)  
                        voy_list = [voy.departingFrom, voy.arrivingAt, voy.departure, voy.arrival]  
                        key = voy.flightNumber
                        voy_dict[key] = (voy_list) 
                    elif len(check_len) == 11 :
                        flightNumber, departingFrom, arrivingAt, departure, arrival, aircraftID,captain,copilot,fsm,fa1,fa2 = line.strip().split(",")
                        voy = Voyage(flightNumber, departingFrom, arrivingAt, departure, arrival)
                        voy_list = [voy.departingFrom, voy.arrivingAt, voy.departure, voy.arrival, aircraftID, captain, copilot, fsm, fa1, fa2]
                        key = voy.flightNumber
                        voy_dict[key] = (voy_list)
                return voy_dict
                voy_file.close()  
        except FileNotFoundError :
            return None     

    def get_voyage(self) :
        voy_dict = self.get_voy_dict()
        return voy_dict
            
    def assign_crew_to_voyage(self, aircraftID, captain, copilot, fsm, fa1, fa2):
        print(aircraftID)
        print(captain)
        print(copilot)
        print(fsm)
        print(fa1)
        print(fa2)
        new_crew_voy = Voyage_2(aircraftID, captain, copilot, fsm, fa1, fa2)
        f=input("f")
        return None