from c_Logic.LL_Employee import Employee_LL
from d_Data.A_Data_API import DataAPI
from c_Logic.LL_Aircraft import Aircraft_LL
from c_Logic.LL_Destination import Destination_LL
from d_Data.Data_Employee import Employee_Data
from c_Logic.LL_Voyage import Voyage_LL
#import os


class LL_API :
    def __init__(self) :
        self.__dapi = DataAPI( )
        #self.empll = Employee_LL( self.__dapi )
        self.empll = Employee_LL()
        self.airc = Aircraft_LL()
        self.dest = Destination_LL()
        self.demp = Employee_Data()
        self.voy = Voyage_LL()
        

    # 
    def addnewvoyage( self, flight_number, departing_from, arriving_at, departure, arrival):
        self.voy.addnewvoyage(flight_number, departing_from, arriving_at, departure, arrival )
    # 
    #  Main menu selected 1
    def addnewemplyee( self, ssn, name, role, rank, licence, address, phonenumber):
        self.empll.addnewemployee( ssn, name, role, rank, licence, address, phonenumber ) 

    def print_chosen_emp(self, emp_ssn) :
        return self.empll.get_chosen_emp(emp_ssn)
        #print(*wow)

    def change_empl_address(self, new_address, emp_ssn) :
        self.empll.change_employee_address(new_address, emp_ssn)
    
    def change_empl_role_rank(self, new_role, new_rank, emp_ssn) :
        self.empll.change_employee_role_rank(new_role, new_rank, emp_ssn)

    def change_empl_licence(self, new_licence, emp_ssn) :
        self.empll.change_employee_licence(new_licence, emp_ssn)

    def change_empl_phonenumber(self, new_phonenumber, emp_ssn) :
        self.empll.change_employee_phonenumber(new_phonenumber, emp_ssn)

    def new_emp_id(self):
        bla = Employee_LL()
        the_new_emp_id = bla.new_emp_id()
        return the_new_emp_id
    #  Main menu selected 5
    def addnewdestination(self, identity, destination, flight_time):
        self.dest.addnewdestination(identity, destination, flight_time)
    #  Main menu selected 6   
    def addnewaircraft(self, nickname,planeTypeId,capacity,manufacturer):
        self.airc.addnewaircraft(nickname,planeTypeId,capacity,manufacturer)

    def display_voy(self):
        pass

    def get_dest(self):
        return self.dest.get_dest()

    def display_voy(self):
        pass

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

