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

    def change_empl_address(self) :
        '''passa að employeeinn sé til'''
        pass
    
    def change_empl_role(self) :
        pass

    def change_empl_rank(self) :
        pass

    def change_empl_licence(self) :
        pass

    def change_empl_phonenumber(self) :
        pass

    def new_emp_id(self):
        bla = Employee_LL()
        the_new_emp_id = bla.new_emp_id()
        return the_new_emp_id
        
    def addnewaircraft(self, planeInsignia, planeTypeId):
        self.airc.addnewaircraft(nickname,planeTypeId,capacity,manufacturer)