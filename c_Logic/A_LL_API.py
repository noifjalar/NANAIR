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

    def change_empl_address(self, new_address) :
        self.empll.change_employee_address(new_address)
    
    def change_empl_role(self, new_role) :
        self.empll.change_employee_role(new_role)

    def change_empl_rank(self, new_rank) :
        self.empll.change_employee_rank(new_rank)

    def change_empl_licence(self, new_licence) :
        self.empll.change_employee_licence(new_licence)

    def change_empl_phonenumber(self, new_phonenumber) :
        self.empll.change_employee_phonenumber(new_phonenumber)

    def new_emp_id(self):
        bla = Employee_LL()
        the_new_emp_id = bla.new_emp_id()
        return the_new_emp_id
        
    def addnewaircraft(self, planeInsignia, planeTypeId):
        self.airc.addnewaircraft(nickname,planeTypeId,capacity,manufacturer)