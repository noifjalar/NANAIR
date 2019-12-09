from c_Logic.LL_Employee import Employee_LL
from d_Data.A_Data_API import DataAPI
from c_Logic.LL_Aircraft import Aircraft_LL
from c_Logic.LL_Destination import Destination_LL
from d_Data.Data_Employee import Employee_Data
from c_Logic.LL_display import Display_LL
#import os

class LL_API :
    def __init__(self) :
        self.__dapi = DataAPI( )
        #self.empll = Employee_LL( self.__dapi )
        self.empll = Employee_LL()
        self.airc = Aircraft_LL()
        self.dest = Destination_LL()
        self.disp = Display_LL()


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

    def change_empl_phonenumber(self, new_phonenumber, emp_snn) :
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

    def display_dest(self):
        self.disp.disp_dest() :)

    def display_voy():
        pass

    def display_status():
        pass

    def display_all_emp():
        pass

    def display_pilots():
        pass

    def display_cabin():
        pass

    def display_cert_emp():
        pass

    def display_off_emp():
        pass

    def display_on_emp():
        pass

    def display_cert_worksheet():
        pass

    def display_pilot_licence():
        pass

    def display_pilot_by_aircraft():
        pass

    