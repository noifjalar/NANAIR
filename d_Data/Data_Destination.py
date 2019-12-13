from Model.destination import Destination 
import os
import csv
import re

class Destination_Data :
    def __init__(self):
        self.filename = "./a_csv/Destinations.csv"
        self.file = "./a_csv/Emergency_contacts.csv"
        self.trash_file = "./a_csv/Emergency_Trash.csv"

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

    def get_emergency_dict(self) :
        '''creates a dictionary with all the emergency contacts'''
        emer_dict = {}
        try :
            with open( self.file ,"r") as emer_file:
                for line in emer_file :
                    identity,name,phonenumber = line.strip().split(",")
                    emer_list = [name, phonenumber]
                    key = identity
                    emer_dict[key] = (emer_list)
                return emer_dict     
                emer_file.close()      
        except FileNotFoundError :
            return None    

    def overwrite_emer_file(self, emer_dict):
        '''Creates a backup emergency csv file, then overwrites the original file with the new information
        and deletes the backup file after overwriting'''
        string = ""

        dest = self.trash_file
        source = self.file
        os.rename(source, dest)

        for key,value in emer_dict.items() :
            string = ''.join('{},{},{}'.format(key, value[0], value[1]))

            with open( self.file ,"a") as emer_file:
                emer_file.write(string)
                emer_file.write("\n")
        
        os.remove(self.trash_file)

    def get_chosen_emer(self, des_id) :
        '''gets the countyr id from user input for changing emergency info'''
        emer_dict = self.get_emergency_dict()
        for key, value in emer_dict.items():
            if key == des_id :
                return value

    def change_emer_name(self, new_name ,des_id) :
        '''changes the name of an emergency contact'''
        emer_dict = self.get_emergency_dict()
        for key, value in emer_dict.items():
            if key == des_id :
                value[0] = new_name
                self.overwrite_emer_file(emer_dict)

    def change_emer_number(self, new_number, des_id) :
        '''changes the number of an emergency contact'''
        emer_dict = self.get_emergency_dict()
        for key, value in emer_dict.items():
            if key == des_id :
                value[1] = new_number
                self.overwrite_emer_file(emer_dict)
