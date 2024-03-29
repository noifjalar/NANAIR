from Model.voyage import Voyage
from Model.voyage import Voyage_2
import datetime
from datetime import timedelta
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
        new_crew_voy = Voyage_2(aircraftID, captain, copilot, fsm, fa1, fa2)
        return None


    def overwrite_voy_file(self, voy_dict):
        string = ""

        dest = self.trash_file
        source = self.filename
        os.rename(source, dest)
        #print(voy_dict)
        for key, value in voy_dict.items():
            if len(value) == 4:
                string = ''.join('{},{},{},{},{}'.format(key, value[0], value[1], value[2], value[3]))
            elif len(value) == 10:
                string = ''.join('{},{},{},{},{},{},{},{},{},{},{}'.format(key, value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9]))
            with open(self.filename, "a") as voy_dict:
                voy_dict.write(string)
                voy_dict.write("\n")
        os.remove(self.trash_file)

    
    def get_date_voy(self, date) :
        ''' Get voyages for a selected date '''
        manned_voy_list = []
        unmanned_voy_list = []
        counter = 1 
        voy_dict = self.get_voy_dict()
        for key, value in voy_dict.items() :
            if counter > 1:
                dep_date, dep_time = value[2].split("T")
                ar_date, ar_time = value[3].split("T")
                if date == dep_date or date == ar_date :
                    if len(value) == 10 :
                        temp_list = [key,value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9]]
                        manned_voy_list.append(temp_list)
                    else: 
                        temp_list = [key,value[0],value[1],value[2],value[3]]
                        unmanned_voy_list.append(temp_list)
            counter += 1
        return manned_voy_list, unmanned_voy_list


    def get_week_voy(self, week):
        ''' Get voyages for a selected week '''
        manned_voy_list = []
        unmanned_voy_list = []
        counter = 1 
        voy_dict = self.get_voy_dict()
        for key, value in voy_dict.items():
            if counter > 1:
                monday, sunday = self.get_selected_week_days(week)
                dep_date, dep_time = value[2].split("T")
                ar_date, ar_time = value[3].split("T")
                if dep_date >= monday and dep_date <= sunday:
                    if len(value) == 10 :
                        temp_list = [key,value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9]]
                        manned_voy_list.append(temp_list)
                    else: 
                        temp_list = [key,value[0],value[1],value[2],value[3]]
                        unmanned_voy_list.append(temp_list)
                if dep_date < monday or dep_date > sunday:
                    if ar_date >= monday and ar_date <= sunday:
                        if len(value) == 10 :
                            temp_list = [key,value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9]]
                            manned_voy_list.append(temp_list)
                        else: 
                            temp_list = [key,value[0],value[1],value[2],value[3]]
                            unmanned_voy_list.append(temp_list)
            counter += 1
        return manned_voy_list, unmanned_voy_list

    def get_selected_week_days(self, week):
        start_of_year = datetime.datetime(2018, 12, 31)
        monday = start_of_year + timedelta(days=week*7)
        sunday = start_of_year + timedelta(days=(week*7)+6)
        monday, na = str(monday).split()
        sunday, na = str(sunday).split()
        return monday, sunday

    def get_on_emp(self, date) :
        on_list = []
        counter = 1 
        voy_dict = self.get_voy_dict()
        for key, value in voy_dict.items() :
            if counter > 1 :
                dep_date, dep_time = value[2].split("T")
                ar_date,ar_time = value[3].split("T")
                if date == dep_date or date == ar_date :
                    if len(value) == 10 :
                        temp_list = [value[5], value[6], value[7], value[8], value[9], value[1]]
                        
                        on_list.append(temp_list)
            counter += 1
        return on_list

    def get_off_emp(self,date):
        allEmps = self
        off_list = []
        counter = 1
        voy_dict = self.get_voy_dict()
        for key, value in voy_dict.items():
            if counter > 1 :
                dep_date, dep_time = value[2].split("T")
                ar_date,ar_time = value[3].split("T")
                if date != dep_date or date != ar_date :
                    print("No voyages on this day!")
                if date == dep_date or date == ar_date:
                    if len(value) == 10:
                        temp_list = [value[5], value[6], value[7], value[8], value[9], value[1]]
                        off_list.append(temp_list)
                        # compare off_list to crew.csv and print out those who are not on the list
            counter += 1
        return off_list


    def get_date(self, flightnumber) :
        voy_dict = self.get_voy_dict()
        for key, value in voy_dict.items() :
            if flightnumber == key :
                dep_time, dep_hour = value[2].split("T")
                ar_time, ar_hour = value[2].split("T")
        return dep_time, ar_time
        



