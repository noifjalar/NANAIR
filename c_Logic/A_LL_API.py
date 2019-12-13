from c_Logic.LL_Employee import Employee_LL
from c_Logic.LL_Aircraft import Aircraft_LL
from c_Logic.LL_Destination import Destination_LL
from d_Data.Data_Employee import Employee_Data
from c_Logic.LL_Voyage import Voyage_LL
#import os


class LL_API :
    def __init__(self) :
        self.empll = Employee_LL()
        self.airc = Aircraft_LL()
        self.dest = Destination_LL()
        self.demp = Employee_Data()
        self.voy = Voyage_LL()
        
    def addnewvoyage( self, flight_number, departing_from, arriving_at, departure, arrival):
        self.voy.addnewvoyage(flight_number, departing_from, arriving_at, departure, arrival ) 
    #  Main menu selected 1
    def addnewemplyee( self, ssn, name, role, rank, licence, address, phonenumber):
        self.empll.addnewemployee( ssn, name, role, rank, licence, address, phonenumber ) 

    def print_chosen_emp(self, emp_ssn) :
        return self.empll.get_chosen_emp(emp_ssn)

    def change_empl_address(self, new_address, emp_ssn) :
        self.empll.change_employee_address(new_address, emp_ssn)
    
    def change_empl_role_rank(self, new_role, new_rank, emp_ssn) :
        self.empll.change_employee_role_rank(new_role, new_rank, emp_ssn)

    def change_empl_licence(self, new_licence, emp_ssn) :
        self.empll.change_employee_licence(new_licence, emp_ssn)

    def change_empl_phonenumber(self, new_phonenumber, emp_ssn) :
        self.empll.change_employee_phonenumber(new_phonenumber, emp_ssn)

    def addnewdestination(self, identity, destination, flight_time):
        self.dest.addnewdestination(identity, destination, flight_time)
    #  Main menu selected 6   

    def addnewaircraft(self, nickname,aircraftID,planeTypeId,capacity,manufacturer):
        self.airc.addnewaircraft(nickname,aircraftID,planeTypeId,capacity,manufacturer)

    def voy_dest(self):
        return self.voy.voy_dest()

    def display_voy(self):
        pass

    def get_dest(self):
        return self.dest.get_dest()

    def display_voy(self):
        return self.voy.get_voyage()

    def display_status(self):
        pass

    def get_all_emp(self):
        return self.demp.get_all_emp()

    def get_pilots(self):
        return self.empll.get_pilots()

    def get_cabin(self):
        return self.empll.get_cabin()

    def display_off_emp(self):
        self.disp.disp_off_emp()

    def display_on_emp(self):
        self.disp.disp_on_emp()

    def display_cert_worksheet(self):
        self.disp.disp_cert_worksheet()

    def get_pilots_with_NABAE146(self):
        return self.empll.get_pilots_with_NABAE146()

    def get_pilots_with_NAFokkerF28(self):
        return self.empll.get_pilots_with_NAFokkerF28()

    def get_pilots_with_NAFokker100(self):
        return self.empll.get_pilots_with_NAFokker100()

    def display_pilot_by_aircraft(self):
        self.disp.disp_pilot_by_aircraft()

    def voy_dest_and_arriving_at(self, val):
        return self.voy.voy_dest_and_arriving_at(val)

    def voy_calculating_flight_times(self, val, departure_not_iso, departing_from):
        return self.voy.voy_calculating_flight_times(val, departure_not_iso, departing_from)

    def create_crew_voyage(self):
        pass

    def find_staff_with_chosen_rank(self, rank):
        return self.voy.find_staff_with_chosen_rank(rank)

    def picked_emp_for_voyage(self, picked, aircraftID, flightNumber):
        self.voy.picked_emp_for_voyage(picked, aircraftID, flightNumber)
        
    def find_aircrafts(self):
        return self.voy.find_aircrafts()

    def certain_date_voy(self, date) :
        return self.voy.certain_date_voy(date)