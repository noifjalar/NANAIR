from d_Data.A_Data_API import DataAPI
from d_Data.Data_Voyage import Voyage_Data
from d_Data.Data_Destination import Destination_Data
from d_Data.Data_Employee import Employee_Data
from d_Data.Data_Aircraft import Aircraft_Data
import datetime
from datetime import timedelta


class Voyage_LL :
    def __init__ (self):
        #self.dapi = dapi_in
        self.dvoy = Voyage_Data()
        self.ddata = Destination_Data()
        self.demp = Employee_Data()
        self.dair = Aircraft_Data()

    def addnewvoyage(self, flight_number, departing_from, arriving_at, departure, arrival):
        '''Vantar að tékka hvort emp sé til með ssn tékki'''
        self.dvoy.register_voyage_data(flight_number, departing_from, arriving_at, departure, arrival)

    def voy_dest(self):
        return self.ddata.get_dest_dict()

        #x = input("sdfg")
    def get_voyage(self) :
        return self.dvoy.get_voyage()

    def voy_dest_and_arriving_at(self, val):
        dest_dict = self.ddata.get_dest_dict()
        counter = 1
        for key, value in dest_dict.items():
            if key == "Keflavik": 
                pass
            else:
                if val == counter:
                    arriving_at = value[0]
                    voy_dest_time = int(value[1])
                counter += 1
        return arriving_at, voy_dest_time

    def voy_calculating_flight_times(self, val, departure_not_iso, departing_from):
        arriving_at,voy_dest_time = self.voy_dest_and_arriving_at(val)


        arrival_not_iso = departure_not_iso + timedelta(hours= voy_dest_time)
        departure = departure_not_iso.isoformat()
        arrival = arrival_not_iso.isoformat()

        departure_return = (arrival_not_iso + timedelta(hours= 1)).isoformat()
        arrival_return = (arrival_not_iso + timedelta(hours= 1) + timedelta(hours= voy_dest_time)).isoformat()

        departing_from_return = arriving_at
        arriving_return = departing_from

        return departure, arrival, departing_from_return, arriving_return, departure_return, arrival_return

    def create_crew_voyage(self):
        voy_dict = self.dvoy.get_voyage

    def find_staff_with_chosen_rank(self, rank):
        crew_dict = self.demp.get_crew_dict()
        emps_with_chosen_rank = []
        #for line in crew_dict.items():
        for key, value in crew_dict.items():
            temp_list = []
            if value[2] == rank:
                temp_list.append(key)
                temp_list.append(value[0])
                emps_with_chosen_rank.append(temp_list)
        return emps_with_chosen_rank

    def picked_emp_for_voyage(self, picked, aircraftID, flightNumber):
        captain, copilot, fsm, fa1, fa2 = picked
        self.dvoy.assign_crew_to_voyage(aircraftID, captain, copilot, fsm, fa1, fa2)
        self.overwrite_voy_dict(flightNumber, aircraftID, captain, copilot, fsm, fa1, fa2)
        flightNumber = self.find_next_flightnumber(flightNumber)
        self.dvoy.assign_crew_to_voyage(aircraftID, captain, copilot, fsm, fa1, fa2)
        self.overwrite_voy_dict(flightNumber, aircraftID, captain, copilot, fsm, fa1, fa2)

        
    def overwrite_voy_dict(self, flightNumber, aircraftID, captain, copilot, fsm, fa1, fa2):
        voy_dict = self.dvoy.get_voy_dict()
        for key, value in voy_dict.items():
            if key == flightNumber:
                value.append(aircraftID)
                value.append(captain)
                value.append(copilot)
                value.append(fsm)
                value.append(fa1)
                value.append(fa2)
        self.dvoy.overwrite_voy_file(voy_dict)

    def find_aircrafts(self):
        return self.dair.get_aircraft_dict()

    def find_next_flightnumber(self, flightNumber):
        voy_dict = self.dvoy.get_voy_dict()
        return_flight = False
        for key, value in voy_dict.items():
            if return_flight == True:
                return key
            if key == flightNumber:
                return_flight = True
        return None

    def certain_date_voy(self, date) :
        return self.dvoy.get_date_voy(date)

    def get_on_emp(self, date) :
        name_list = []
        onEmps = self.dvoy.get_on_emp(date)
        allEmps =Employee_Data().get_crew_dict()
        for onemp in onEmps:
            temp_list = []
            for key, value in allEmps.items():
                for ssn in onemp :
                    if key == ssn:
                        temp_list.append(value[0])
            if temp_list != [] :
                name_list.append(temp_list)
        return self.dvoy.get_on_emp(date), name_list

    def get_off_emp(self,date):
        allEmps =Employee_Data().get_crew_dict()
        
        onEmps, name_list = self.get_on_emp(date)
        # print(onEmps)
        offEmps = []
        i = 0
        for emp, value in allEmps.items():
            if i != 0:
                isOff = True
                
                for onemp in onEmps:
                    if emp in onemp:
                        isOff = False
                if isOff == True:

                    offEmps.append(value[0])
            i+=1

        return offEmps
