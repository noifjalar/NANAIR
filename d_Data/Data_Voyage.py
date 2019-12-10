from Model.voyage import Voyage
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

    def get_voy_dict():
        voy_dict = []
        for line in self.filename:
            voy_
            voy_dict = line.append()

    def get_voyage(self) :
        voy_dict = self.get_voy_dict()
        