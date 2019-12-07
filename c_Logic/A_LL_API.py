from c_Logic.LL_Employee import Employee_LL
from d_Data.A_Data_API import DataAPI
from c_Logic.LL_Aircraft import Aircraft_LL

#import os

class LL_API :
    def __init__(self) :
        self.__dapi = DataAPI( )
        #self.empll = Employee_LL( self.__dapi )
        self.empll = Employee_LL()
        self.airc = Aircraft_LL()

    def addnewemplyee( self, ssn, name, role, rank, licence, address, phonenumber):
        self.empll.addnewemployee( ssn, name, role, rank, licence, address, phonenumber ) 

    def change_empl_address(self, new_address, emp_ssn) :
        self.empll.change_employee_address(new_address, emp_ssn)
    
    def change_empl_role(self, new_role, emp_ssn) :
        self.empll.change_employee_role(new_role, emp_ssn)

    def change_empl_rank(self, new_rank, emp_ssn) :
        self.empll.change_employee_rank(new_rank, emp_ssn)

    def change_empl_licence(self, new_licence, emp_ssn) :
        self.empll.change_employee_licence(new_licence, emp_ssn)

    def change_empl_phonenumber(self, new_phonenumber, emp_snn) :
        self.empll.change_employee_phonenumber(new_phonenumber, emp_ssn)

    def new_emp_id(self):
        bla = Employee_LL()
        the_new_emp_id = bla.new_emp_id()
        return the_new_emp_id
        
    def addnewaircraft(self, nickname,planeTypeId,capacity,manufacturer):
        self.airc.addnewaircraft(nickname,planeTypeId,capacity,manufacturer)